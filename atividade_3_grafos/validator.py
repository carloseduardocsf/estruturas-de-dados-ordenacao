from __future__ import annotations


EXPECTED_MSTP = {
    "dij10": 7072,
    "dij20": 15238,
    "dij40": 26615,
    "dij50": 30424,
}

EXPECTED_DIJKSTRA = {
    "dij10": 5183,
    "dij20": 3190,
    "dij40": 8928,
    "dij50": 6764,
}


def compare_result(found: int | float | str, expected: int | None) -> str:
    if expected is None:
        return "SEM_GABARITO"
    return "OK" if found == expected else "ERRO"


def expected_mstp(instance_name: str) -> int | None:
    return EXPECTED_MSTP.get(instance_name)


def expected_dijkstra(instance_name: str) -> int | None:
    return EXPECTED_DIJKSTRA.get(instance_name)
