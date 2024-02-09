import sys

try:
    f = open('sample.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise



# Exception can be used as a wildcard that catches (almost) everything. 
# However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, 
# and to allow any unexpected exceptions to propagate on.

# The most common pattern for handling Exception is to print or log the exception and then re-raise it 
# (allowing a caller to handle the exception as well):
