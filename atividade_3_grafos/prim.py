from __future__ import annotations

import heapq


def prim(adj_list: list[list[tuple[int, int]]], start: int = 0) -> tuple[int, list[tuple[int, int, int]]]:
    n = len(adj_list)
    if n == 0:
        return 0, []

    visited = [False] * n
    visited[start] = True
    mst_weight = 0
    mst_edges: list[tuple[int, int, int]] = []
    heap: list[tuple[int, int, int]] = []

    for neighbor, weight in adj_list[start]:
        heapq.heappush(heap, (weight, start, neighbor))

    while heap and len(mst_edges) < n - 1:
        weight, u, v = heapq.heappop(heap)
        if visited[v]:
            continue

        visited[v] = True
        mst_weight += weight
        mst_edges.append((u, v, weight))

        for neighbor, edge_weight in adj_list[v]:
            if not visited[neighbor]:
                heapq.heappush(heap, (edge_weight, v, neighbor))

    if len(mst_edges) != n - 1:
        raise ValueError("O grafo nao e conexo; nao foi possivel construir a MST.")

    return mst_weight, mst_edges
