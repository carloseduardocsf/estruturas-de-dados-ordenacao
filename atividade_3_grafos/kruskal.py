from __future__ import annotations


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex: int) -> int:
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(n: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    union_find = UnionFind(n)
    mst_weight = 0
    mst_edges: list[tuple[int, int, int]] = []

    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        if union_find.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) != n - 1:
        raise ValueError("O grafo nao e conexo; nao foi possivel construir a MST.")

    return mst_weight, mst_edges
