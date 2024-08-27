# there is a list of [6,5,4,3,9,8,0] in this there is only 2 value equals 10 find which one?

# arr = [6,5,3,9,8,0]

# i = 0
# found = False
# while i < len(arr):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] + arr[j] == 10:
#             print(f"the first value is {arr[i]} and  the second value is {arr[j]}")   
#             found = True
#         j += 1
#     i += 1 

# if not found:
#     print("No pairs found that sum to 10.")      


# arr = [6, 5, 4, 3, 9, 8, 0]

# i = 0
# found = False  # To track if we have found at least one pair

# while i < len(arr):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] + arr[j] == 10:
#             print(f"The first value is {arr[i]} and the second value is {arr[j]}")    # now this complexity is o(n^2)
#             found = True
#         j += 1
#     i += 1

# if not found:
#     print("No pairs found that sum to 10.")