# stack is working on LIFO order that means last in first out.
# stack is a user defined data structure so we want to first create one 
# in there is two way of create stack
# 1.using list 
# 2.using modules

# usingi list:

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

