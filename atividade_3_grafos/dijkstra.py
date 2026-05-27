from __future__ import annotations

import heapq
from math import inf


def dijkstra(
    adj_list: list[list[tuple[int, int]]],
    source: int = 0,
    target: int | None = None,
) -> tuple[float, list[int]]:
    n = len(adj_list)
    if n == 0:
        return 0, []

    if target is None:
        target = n - 1

    distances = [inf] * n
    predecessors = [-1] * n
    distances[source] = 0
    heap: list[tuple[float, int]] = [(0, source)]

    while heap:
        current_distance, vertex = heapq.heappop(heap)
        if current_distance > distances[vertex]:
            continue
        if vertex == target:
            break

        for neighbor, weight in adj_list[vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = vertex
                heapq.heappush(heap, (new_distance, neighbor))

    path = reconstruct_path(predecessors, source, target)
    return distances[target], path


def reconstruct_path(predecessors: list[int], source: int, target: int) -> list[int]:
    if source == target:
        return [source]

    path: list[int] = []
    current = target

    while current != -1:
        path.append(current)
        if current == source:
            break
        current = predecessors[current]

    if not path or path[-1] != source:
        return []

    path.reverse()
    return path
