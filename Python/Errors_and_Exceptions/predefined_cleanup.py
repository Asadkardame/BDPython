# Some objects define standard clean-up actions to be undertaken when the object is no longer needed, 
# regardless of whether or not the operation using the object succeeded or failed. 
# Look at the following example, which tries to open a file and print its contents to the screen.



# for line in open("sample.txt"):
#     print(line, end="")

#-------------------------------------------------------

# The problem with this code is that it leaves the file open for an indeterminate 
# amount of time after this part of the code has finished executing. This is not 
# an issue in simple scripts, but can be a problem for larger applications. 
# The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
        


with open("sample.txt") as f:
    for line in f:
        print(line, end="")

 
