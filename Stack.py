# stack is working on LIFO order that means last in first out.
# stack is a user defined data structure so we want to first create one 
# in there is two way of create stack
# 1.using list 
# 2.using modules

# usingi list:
# //////////////////////////////////////////////////////////////////////////////////////////////////

# example 1:
# //////////////////////////////////////

# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)

# print(stack)

# stack.pop()
# stack.pop()

# print(stack)


# example 2:
# /////////////////////////////////////
# stack = []

# def push():
#     element = input("Enter a element")
#     stack.append(element)
#     print(stack)

# def pop():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("Removed Element:",e)
#         print(stack)

# while True:
#     print("Select Choice 1.push 2.pop 3.quite")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         break
#     else:
#         print("Enter the correct choice")


# example 3:       make a limit in the stack
# //////////////////////////////////////////

# stack = []

# def push():
#     if len(stack)==n:
#         print("The stack is full")
#     else:    
#         element = input("Enter a element")
#         stack.append(element)
#         print(stack)

# def pop():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("Removed Element:",e)
#         print(stack)
        
# n = int(input("Enter limit of the list"))        # this will now set the limit of the stack

# while True:
#     print("Select Choice 1.push 2.pop 3.quite")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         break
#     else:
#         print("Enter the correct choice")





# Using collections.deque :

# this one is more efficiant for stack operations
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# from collections import deque

# stack = deque()
# print(stack)

# stack.append(10)
# stack.append(20)
# stack.append(30)

# stack.pop()                               # this will now remove the last element of the stack 
# stack.pop()

# print(stack)


# //////////////////////////////////////////////////////////////////////////

# import queue

# stack = queue.LifoQueue(3)   # we can also set the limit of the stack by give a number for limit
# stack.put(10)
# stack.put(20)
# stack.put(30)
# stack.put(40,timeout=1)         # by using timeout this will show the error of queue limit when the limit is full that will show here

# print(stack)


