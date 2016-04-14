__author__ = 'alsodeep'


def main():
    # a = [5,2,4,6,1,3]
    # a = [31,41,59,26,41,58]
    a = [1, 0, 1]
    b = [1, 0, 1]
    c = binarry_addition(a, b)
    # insertion_sort_reverse(a)
    print c


def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
            array[i + 1] = key
    return array


def insertion_sort_reverse(a):
    for i in range(1, len(a)):
        j = i - 1
        key = a[i]
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


def binarry_addition(a, b):
    n = len(a)
    c = [0] * (n + 1)
    i = 0
    while i < len(a):
        if a[i] == 1 and b[i] == 1:
            c[i + 1] = 1
        elif (a[i] == 1 and b[i] == 1) or (a[i] == 0 and b[i] == 1):
            if c[i] == 1:
                c[i + 1] = 1
                c[i] = 0
        i = i + 1
    return c


if __name__ == "__main__":
    main()
