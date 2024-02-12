# 8.3. Handling Exceptions¶
# It is possible to write programs that handle selected exceptions. Look at the following example, 
# which asks the user for input until a valid integer has been entered, 
# but allows the user to interrupt the program (using Control-C or whatever the operating system supports); 
# note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

#----------------------------------------------------------------------------------------------

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

#-------------------------------------------------------------------------------------------------

# The try statement works as follows.

# First, the try clause (the statement(s) between the try and except keywords) is executed.

# If no exception occurs, the except clause is skipped and execution of the try statement is finished.

# If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
# Then, if its type matches the exception named after the except keyword, the except clause is executed, 
# and then execution continues after the try/except block.

# If an exception occurs which does not match the exception named in the except clause, 
# it is passed on to outer try statements; if no handler is found, 
# it is an unhandled exception and execution stops with an error message.
        
        # MULTIPLE EXCEPTION CLAUSE IN ONE CATCH

# A try statement may have more than one except clause, to specify handlers for different exceptions. 
# At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, 
# not in other handlers of the same try statement. 
# An except clause may name multiple exceptions as a parenthesized tuple, for example:
        

#----------------------------------------------------------------------------------------------------------

# ... except (RuntimeError, TypeError, NameError):
# ...     pass
        
#-----------------------------------------------------------------------------------------------------------



# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


#----------------------------------------------------------------------------------
        
        # Channge in order

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#     except D:
#         print("D")
#     except C:
#         print("C")


# he output will be different from the first example due to the order of the except blocks:

# When raising B(), the exception matches the except B: block, so "B" is printed.
# When raising C(), the exception matches the except B: block (since C is a subclass of B), so "B" is printed.
# When raising D(), the exception matches the except B: block (since D is a subclass of both B and C), so "B" is printed.
# The output is "B" for all three exceptions because the except B: block is defined before the other except blocks. 
# Therefore, it gets matched first for any exception raised, regardless of its subclass.




#----------------------------------------------------------------------------------------
        
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
 