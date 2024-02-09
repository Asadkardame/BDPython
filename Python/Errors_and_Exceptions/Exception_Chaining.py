# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")


# If an unhandled exception occurs inside an except section, 
# it will have the exception being handled attached to it and included in the error message:


# raise RuntimeError from exc
#---------------------------------------------------------

#This can be useful when you are transforming exceptions. For example:



# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


#--------------------------------------------------------------------------


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None