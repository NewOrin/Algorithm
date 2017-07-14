import random


# 插入排序
def insert_sort(sort_lists):
    length = len(sort_lists)
    for j in range(1, length):
        key = sort_lists[j]
        i = j - 1
        # 向前查找插入位置
        while i >= 0 and sort_lists[i] > key:
            sort_lists[i + 1] = sort_lists[i]
            i = i - 1
        sort_lists[i + 1] = key
    print("排序后数组")
    print(sort_lists)


def generate_lists(numbers, max):
    lists = []
    while numbers > 0:
        n = random.randint(0, max)
        lists.append(n)
        numbers = numbers - 1
    return lists


l = generate_lists(5, 10)
print("排序前数组")
print(l)
insert_sort(l)
