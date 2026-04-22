from __future__ import annotations


def selection_sort(values: list[int]) -> list[int]:
    result = list(values)
    size = len(result)

    for index in range(size):
        min_index = index
        for candidate in range(index + 1, size):
            if result[candidate] < result[min_index]:
                min_index = candidate

        result[index], result[min_index] = result[min_index], result[index]

    return result
