from __future__ import annotations

from pathlib import Path


def read_graph_file(path: str | Path) -> tuple[int, list[list[int]], list[list[tuple[int, int]]], list[tuple[int, int, int]]]:
    file_path = Path(path)
    tokens = file_path.read_text(encoding="utf-8-sig").split()

    if not tokens:
        raise ValueError(f"Arquivo vazio: {file_path}")

    n = int(tokens[0])
    if n <= 0:
        raise ValueError("O numero de vertices deve ser positivo.")

    weights = [int(token) for token in tokens[1:]]
    expected_weights = n * (n - 1) // 2
    validate_weights_count(n, len(weights))

    adj_matrix = build_adjacency_matrix(n, weights)
    adj_list = build_adjacency_list(adj_matrix)
    edges = build_edges_list(adj_matrix)
    return n, adj_matrix, adj_list, edges


def validate_weights_count(n: int, count: int) -> None:
    expected = n * (n - 1) // 2
    if count != expected:
        raise ValueError(
            "Quantidade de pesos invalida: "
            f"esperado {expected}, encontrado {count}."
        )


def build_adjacency_matrix(n: int, weights: list[int]) -> list[list[int]]:
    adj_matrix = [[0] * n for _ in range(n)]
    index = 0

    for u in range(n):
        for v in range(u + 1, n):
            weight = weights[index]
            adj_matrix[u][v] = weight
            adj_matrix[v][u] = weight
            index += 1

    return adj_matrix


def build_adjacency_list(adj_matrix: list[list[int]]) -> list[list[tuple[int, int]]]:
    n = len(adj_matrix)
    adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u != v:
                adj_list[u].append((v, adj_matrix[u][v]))

    return adj_list


def build_edges_list(adj_matrix: list[list[int]]) -> list[tuple[int, int, int]]:
    n = len(adj_matrix)
    edges: list[tuple[int, int, int]] = []

    for u in range(n):
        for v in range(u + 1, n):
            edges.append((u, v, adj_matrix[u][v]))

    return edges
