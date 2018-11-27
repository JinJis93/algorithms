import os
import random
from statistics import median

file_dir = os.path.abspath("") + "/files"
integer_set: str = open(file_dir + "/quicksort.txt", "r", encoding="utf-8").readlines()
integer_list = list(map(lambda integer: int(integer), integer_set))


class QuickSortCompCounter:

    def __init__(self):
        self.comp_count = 0

    def compute_quick_sort(self, input_array: list) -> list:
        if len(input_array) < 2:
            return input_array

        # randomly pick pivot index
        # pivot_index = random.randint(0, len(input_array) - 1)

        # always use first elem
        # pivot_index = 0

        # always use last elem
        # pivot_index = (len(input_array) - 1)

        # median-of-three pivot index

        first = input_array[0]
        middle = input_array[int((len(input_array) + 1) / 2) - 1]
        last = input_array[-1]
        pivot_index = input_array.index(median([first, middle, last]))

        # move pivot to first index
        if not pivot_index == 0:
            pivot_val = input_array[pivot_index]
            input_array[pivot_index] = input_array[0]
            input_array[0] = pivot_val

        # do partition
        i = 0
        j = i + 1
        pivot_val = input_array[0]
        while j < len(input_array):
            if input_array[j] < pivot_val:
                cur_small = input_array[j]
                boundary = input_array[i + 1]
                # switch
                input_array[i + 1] = cur_small
                input_array[j] = boundary
                i += 1
                j += 1
                continue
            j += 1
            continue

        # count comparison
        self.comp_count += (len(input_array) - 1)

        # finally switch pivot with boundary
        boundary = input_array[i]
        input_array[0] = boundary
        input_array[i] = pivot_val

        # recursive calls
        smaller = self.compute_quick_sort(input_array[:i])
        bigger = self.compute_quick_sort(input_array[i + 1:])
        pivot = [pivot_val]

        return smaller + pivot + bigger


tester = QuickSortCompCounter()
result = tester.compute_quick_sort(integer_list)
print(result)
print(tester.comp_count)
