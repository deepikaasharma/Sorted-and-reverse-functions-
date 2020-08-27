# numbers = [5, 7, 2, 19, 1]
# newly_sorted = sorted(numbers, reverse = True)
# print(newly_sorted)

# str_list = ['a', 'b', 'c', 'd']
# newly_reversed = reversed(str_list)

# # newly reversed iterable
# print(newly_reversed)
# # newly reversed iterable, made into a list
# print(list(newly_reversed))
# # original list, not affected
# print(str_list)

# numbers = [1, 2, 3, 4]
# newly_reversed = reversed(numbers)

# # newly reversed iterable
# print(newly_reversed)
# # newly reversed iterable, cast as a list
# print(list(newly_reversed))
# # original list, not affected
# print(numbers)


"""Given the following code, what would print to the console?"""

# lst = [5, 4, 9, 3, 1, 0]
# sorted(lst)
# print(lst)

"""Given the following code, what would print to the console?"""

#lst = [5, 4, 9, 3, 1, 0]
# print(list(reversed(lst)))

"""In the code cell below complete the following:

    Sort the list stored in random_list, and save it in a variable called sorted_lst
    Reverse the list stored in backwards_list and store it in a variable called forward_lst
    Sort and then reverse the list stored in all_scrambled_up and store the result of those operations in a variable called unscrambled"""

import random
random.seed(1)
random_lst      = [random.random() for i in range(1000)]
backwards_lst   = [random.random() for i in range(1200)]
all_scrambled_up = [random.random() for i in range(1500)]

sorted_lst = sorted(random_lst)
forward_lst = list(reversed(backwards_lst))
unscrambled = list(reversed(sorted(all_scrambled_up)))

print(sorted_lst)
print(forward_lst)
print(unscrambled)