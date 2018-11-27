import os
import random
from statistics import median

file_dir = os.path.abspath("") + "/files"
integer_set: str = open(file_dir + "/quicksort.txt", "r", encoding="utf-8").readlines()
integer_list = list(map(lambda integer: int(integer), integer_set))


class QuickSortCompCounter:

    def __init__(self, pivot_how: str):
        self.comp_count = 0
        self.pivot_how = pivot_how

    @staticmethod
    def get_random_pivot_index(input_array: list):
        # randomly pick pivot index
        return random.randint(0, len(input_array) - 1)

    @staticmethod
    def get_median_of_three_pivot_index(input_array: list):
        # median-of-three pivot index
        first = input_array[0]
        middle = input_array[int((len(input_array) + 1) / 2) - 1]
        last = input_array[-1]
        return input_array.index(median([first, middle, last]))

    def compute_quick_sort(self, input_array: list) -> list:
        if len(input_array) < 2:
            return input_array

        if self.pivot_how == "random":
            pivot_index = self.get_random_pivot_index(input_array)

        elif self.pivot_how == "first":
            pivot_index = 0

        elif self.pivot_how == "last":
            pivot_index = -1

        elif self.pivot_how == "median":
            pivot_index = self.get_median_of_three_pivot_index(input_array)
        else:
            raise Exception("Invalid 'pivot how': %s" % self.pivot_how)

        # move pivot to first index
        if not pivot_index == 0:
            input_array = self.swap_postion(input_array, pivot_index, 0)

        # do partition
        i = 0
        j = i + 1
        pivot_val = input_array[0]
        while j < len(input_array):
            if input_array[j] < pivot_val:
                input_array = self.swap_postion(input_array, j, i + 1)
                i += 1
                j += 1
                continue
            j += 1
            continue

        # count comparison
        self.comp_count += (len(input_array) - 1)

        # finally switch pivot with boundary
        input_array = self.swap_postion(input_array, i, 0)

        # recursive calls
        smaller = self.compute_quick_sort(input_array[:i])
        bigger = self.compute_quick_sort(input_array[i + 1:])
        pivot = [pivot_val]

        return smaller + pivot + bigger

    @staticmethod
    def swap_postion(input_array: list, target_index: int, counter_index: int):
        target_val = input_array[target_index]
        input_array[target_index] = input_array[counter_index]
        input_array[counter_index] = target_val
        return input_array


tester = QuickSortCompCounter("random")
result = tester.compute_quick_sort(integer_list)
print(result)
print(tester.comp_count)
