import os

file_path = os.path.abspath("") + "/files"
txt_list: list = open(file_path + "/integer.txt", "r", encoding="utf-8").readlines()

test_list = [int(integer) for integer in txt_list]


def count_inversion(int_list: list):
    # divide into subproblems
    n = len(int_list)
    a_set: list = int_list[:int(n / 2)]
    b_set: list = int_list[int(n / 2):]

    # recursive call
    a_inv_count = count_inversion(a_set) if not n == 1 else 0
    b_inv_count = count_inversion(b_set) if not n == 1 else 0

    a_sorted: list = sorted(a_set)
    b_sorted: list = sorted(b_set)

    # SplitInvCount
    split_inv_count = 0
    merged = []
    i = 0
    j = 0
    for k in range(n):

        if i > (len(a_sorted) - 1):
            merged.extend(b_sorted[j:])
            break
        elif j > (len(b_sorted) - 1):
            merged.extend((a_sorted[i:]))
            break

        if b_sorted[j] < a_sorted[i]:
            merged.append(b_sorted[j])
            j += 1
            split_inv_count += (len(a_sorted) - i)
        elif b_sorted[j] > a_sorted[i]:
            merged.append(a_sorted[i])
            i += 1

    return a_inv_count + b_inv_count + split_inv_count


a = count_inversion(test_list)
print(a)
