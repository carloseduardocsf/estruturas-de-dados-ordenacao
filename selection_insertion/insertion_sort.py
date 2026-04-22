from __future__ import annotations


def insertion_sort(values: list[int]) -> list[int]:
    result = list(values)

    for index in range(1, len(result)):
        key = result[index]
        position = index - 1

        while position >= 0 and result[position] > key:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = key

    return result
