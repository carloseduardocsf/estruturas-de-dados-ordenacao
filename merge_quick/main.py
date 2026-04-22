from __future__ import annotations

import sys
from pathlib import Path
from time import perf_counter

from merge_sort import merge_sort
from quick_sort import quick_sort


PROJECT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = PROJECT_DIR / "results"


def read_file(file_path: str | Path) -> list[int]:
    path = Path(file_path)
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines:
        raise ValueError("o arquivo de entrada esta vazio")

    # A primeira linha contem apenas a quantidade de elementos.
    return [int(line.strip()) for line in lines[1:] if line.strip()]


def measure_time(sort_function, arr: list[int], *args) -> float:
    start_time = perf_counter()
    sort_function(arr, *args)
    end_time = perf_counter()
    return end_time - start_time


def save_instance(path: Path, values: list[int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        file.write(f"{len(values)}\n")
        for value in values:
            file.write(f"{value}\n")


def main() -> int:
    if len(sys.argv) != 2:
        program_name = Path(sys.argv[0]).name or "merge_quick.py"
        print(f"Uso: python {program_name} <arquivo_de_entrada>")
        return 1

    file_path = Path(sys.argv[1])

    try:
        values = read_file(file_path)
    except FileNotFoundError:
        print(f"Arquivo nao encontrado: {file_path}")
        return 1
    except ValueError as error:
        print(f"Erro ao ler arquivo: {error}")
        return 1

    merge_values = list(values)
    quick_values = list(values)

    merge_time = measure_time(merge_sort, merge_values, 0, len(merge_values) - 1)

    # O Quick Sort recursivo pode exigir mais profundidade em particoes ruins.
    sys.setrecursionlimit(max(1000, len(quick_values) * 2 + 10))
    quick_time = measure_time(quick_sort, quick_values, 0, len(quick_values) - 1)

    output_path = RESULTS_DIR / file_path.name
    save_instance(output_path, merge_values)

    print(f"Arquivo analisado: {file_path.name}")
    print(f"Quantidade de elementos: {len(values)}")
    print(f"Tempo do Merge Sort: {merge_time:.6f} segundos")
    print(f"Tempo do Quick Sort: {quick_time:.6f} segundos")
    print(f"Arquivo ordenado salvo em: {output_path}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
