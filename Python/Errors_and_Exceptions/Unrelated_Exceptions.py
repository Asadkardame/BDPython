########### Raising and Handling Multiple Unrelated Exceptions

# There are situations where it is necessary to report several exceptions that have occurred. 
# This is often the case in concurrency frameworks, when several tasks may have failed in parallel, 
# but there are also other use cases where it is desirable to continue execution and collect 
# multiple errors rather than raise the first exception.

############ ecxept e (Group exception)


# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)

# f()

# try:
#     f()
# except Exception as e:
#     print(f'caught {type(e)}: e')


#-----------------------------------------------------------------------------------------
    
#By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type. 
#In the following example, which shows a nested exception group, each except* clause extracts from the 
#group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.
    

# def f():
#     raise ExceptionGroup(
#         "group1",
#         [
#             OSError(1),
#             SystemError(2),
#             ExceptionGroup(
#                 "group2",
#                 [
#                     OSError(3),
#                     RecursionError(4)
#                 ]
#             )
#         ]
#     )

# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")

#------------------------------------------------------------------------------
