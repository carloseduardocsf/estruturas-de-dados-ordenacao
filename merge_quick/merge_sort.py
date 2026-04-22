from __future__ import annotations


def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    left_index = 0
    right_index = 0
    current_index = left

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] <= right_part[right_index]:
            arr[current_index] = left_part[left_index]
            left_index += 1
        else:
            arr[current_index] = right_part[right_index]
            right_index += 1

        current_index += 1

    while left_index < len(left_part):
        arr[current_index] = left_part[left_index]
        left_index += 1
        current_index += 1

    while right_index < len(right_part):
        arr[current_index] = right_part[right_index]
        right_index += 1
        current_index += 1


def merge_sort(arr: list[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
