#Name: Jefferson Adjetey
#Date: 03/02/2021
# Purpose: Create a recursive function to quicksort through a list using partition


def compare_ints(a, b):  # comparison function for integers
    return a <= b


def compare_strings(a, b):  # comparison function for strings
    return a.lower() <= b.lower()


def partition(the_list, p, r, compare_func):  # partition function for quicksort recursion
    i = p - 1
    pivot = the_list[r]  # item to compare the list with

    for j in range(p, r):
        if compare_func(the_list[j], pivot):  # condition for if an item in the list is less than pivot
            # swap items i and j, increment i and j
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            j += 1
        else:
            # increment j if an item in the list is greater than pivot
            j += 1

    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]
    # swap pivot into the correct spot
    return i + 1
    # return pivot's index


def quicksort(the_list, p, r, compare_func):
    if r == len(the_list):
        return the_list
    # base case that occurs when the sublist has fewer than two items

    if p < r:
        q = partition(the_list, p, r, compare_func)  # partition the sublist
        quicksort(the_list, p, q - 1, compare_func)  # call the recursion on the sublist of items p up to q
        quicksort(the_list, q + 1, r, compare_func)  # call the recursion on the sublist of items q up to r


# calls quicksort and gives the type of comparison function
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)



s1 = [2, 8, 33, 69, 22, 18, 7, 6, 45, 42,  1, 3, 5, 6, 4]
s2 = ["a", "d", "z", "f", "b", "g", "e", "d", "x", "c", "a", "g"]
sort(s1, compare_ints)
sort(s2, compare_strings)
print(s1)
print(s2)