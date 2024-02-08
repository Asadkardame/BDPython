# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
# -------------------------------------------

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#-----------------------------------------------


# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active', 'Anu':5}

# print("V0", users)
# # Strategy:  Iterate over a copy
# # for user, status in users.copy().items():
#     # if status == 'inactive':
#     #     del users[user]

# for user in users.copy().values():
    
#     print('value', user)        
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         # print(users)
# print("V2", users)
# print(active_users)

#--------------------------------------------

# for i in range(5):
#     print(i)

#--------------------------------------------

# x= list(range(5, 10))
# print('X=', x)

# y= list(range(0, 10, 3))
# print('Y=', y)

# z= list(range(-10, -100, -30))
# print('Z=', z)
#---------------------------------------------

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

#-----------------------------------------------


# print(sum(range(4)))

#-----------------------------------------------


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#----------------------------------------------------


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)

#---------------------------------------------------


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
        
# print(http_error(int(input("Enter Port: "))))

#---------------------------------------------------


# def http_error(status):
#     match status:
#         case 401 | 403 | 404:
#             return "Not allowed"
        
# print(http_error(int(input("Enter Port: "))))

#----------------------------------------------------


# x=int(input("X Value: "))
# if(x==2)|(x==4):
#     print("Yes")
# else:
#     print("NO")

#----------------------------------------------------

# point is an (x, y) tuple
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")

# x= int(input("x: "))
# y=int(input("y: "))
# print(mpoint(x,y))
            

#----------------------------------------------------


# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# fib(2000)

# fib

# f = fib
# f(100)

# def fib2(n):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result

# f100 = fib2(100)    # call it
# print(f100)

#-------------------------------------------------


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

#---------------------------------------------------------------

# x= 'python'
# y='or'

# z=x[2:-2]+y
# print(z)

#----------------------------------------------------------

# x = [1, 4, 9, 16, 25]
# y=[7,6,9]

# x.extend(y)
# # for i in y:
#     # x.append(i)
# # new_list = [i+10 for i in x]
# print(x)

#--------------------------------------------------------------

# x=['a','b','c']
# y=[1,2,3]
# q=[5,6,7]
# z=[x,y,q]

# print(z[0][2],z[1][1],z[2][1])