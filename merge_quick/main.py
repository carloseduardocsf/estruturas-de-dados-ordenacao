from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from time import perf_counter

from merge_sort import merge_sort
from quick_sort import quick_sort


PROJECT_DIR = Path(__file__).resolve().parent
INSTANCES_DIR = PROJECT_DIR / "instancias-num"
RESULTS_DIR = PROJECT_DIR / "results"


def run_merge_sort(values: list[int]) -> list[int]:
    result = list(values)
    merge_sort(result, 0, len(result) - 1)
    return result


def run_quick_sort(values: list[int]) -> list[int]:
    result = list(values)
    # O Quick Sort recursivo pode exigir mais profundidade em particoes ruins.
    sys.setrecursionlimit(max(1000, len(result) * 2 + 10))
    quick_sort(result, 0, len(result) - 1)
    return result


ALGORITHMS = (
    ("Merge Sort", run_merge_sort),
    ("Quick Sort", run_quick_sort),
)


def read_instance(path: Path) -> list[int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    size = int(lines[0].strip())
    return [int(lines[index].strip()) for index in range(1, size + 1)]


def instance_sort_key(path: Path) -> tuple[int, int]:
    parts = path.stem.split(".")
    return int(parts[1]), int(parts[2])


def measure_algorithm(instance_name: str, values: list[int], algorithm_name: str, algorithm) -> tuple[str, str, float]:
    start = perf_counter()
    ordered_values = algorithm(values)
    elapsed_seconds = perf_counter() - start
    return instance_name, algorithm_name, elapsed_seconds, ordered_values


def save_instance(path: Path, values: list[int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        file.write(f"{len(values)}\n")
        for value in values:
            file.write(f"{value}\n")


def run_single_instance(path: Path) -> None:
    values = read_instance(path)
    ordered_values = None
    print(f"Instancia: {path.name}")

    for algorithm_name, algorithm in ALGORITHMS:
        _, algorithm_name, elapsed_seconds, current_values = measure_algorithm(
            path.name,
            values,
            algorithm_name,
            algorithm,
        )
        if ordered_values is None:
            ordered_values = current_values
        print(f"{algorithm_name}: {elapsed_seconds:.6f}s")

    save_instance(RESULTS_DIR / path.name, ordered_values)


def generate_table(instances_dir: Path, table_path: Path) -> None:
    instance_files = sorted(instances_dir.glob("*.in"), key=instance_sort_key)
    table_path.parent.mkdir(parents=True, exist_ok=True)
    total_lines = len(instance_files) * len(ALGORITHMS) + 1
    current_line = 2

    with table_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["instancia", "algoritmo", "tempo_execucao_segundos"])
        csv_file.flush()

        for instance_path in instance_files:
            values = read_instance(instance_path)
            ordered_values = None

            for algorithm_name, algorithm in ALGORITHMS:
                print(f"Linha {current_line}/{total_lines}: {instance_path.name} - {algorithm_name}")
                instance_name, algorithm_name, elapsed_seconds, current_values = measure_algorithm(
                    instance_path.name,
                    values,
                    algorithm_name,
                    algorithm,
                )
                if ordered_values is None:
                    ordered_values = current_values
                writer.writerow([instance_name, algorithm_name, f"{elapsed_seconds:.6f}"])
                csv_file.flush()
                current_line += 1

            save_instance(RESULTS_DIR / instance_path.name, ordered_values)

    print(f"Tabela salva em: {table_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    instance_parser = subparsers.add_parser("instancia")
    instance_parser.add_argument("arquivo", type=Path)

    table_parser = subparsers.add_parser("tabela")
    table_parser.add_argument("--saida", type=Path, required=True)

    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "instancia":
        run_single_instance(args.arquivo)
        return 0
    else:
        generate_table(INSTANCES_DIR, args.saida)
        return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
