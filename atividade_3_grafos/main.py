from __future__ import annotations

import argparse
from pathlib import Path

from dijkstra import dijkstra
from graph_reader import read_graph_file
from kruskal import kruskal
from prim import prim


PROJECT_DIR = Path(__file__).resolve().parent
INSTANCES_DIR = PROJECT_DIR / "instancias"
DEFAULT_INSTANCES = ("dij10.txt", "dij20.txt", "dij40.txt", "dij50.txt")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Executa Kruskal, Prim e Dijkstra para as instancias da atividade 3."
    )
    parser.add_argument("arquivo", nargs="?", type=Path)
    parser.add_argument("--all", action="store_true")
    return parser


def run_instance(path: Path) -> None:
    n, _, adj_list, edges = read_graph_file(path)
    instance_name = path.stem

    kruskal_weight, _ = kruskal(n, edges)
    prim_weight, _ = prim(adj_list, start=0)
    shortest_distance, _ = dijkstra(adj_list, source=0, target=n - 1)
    shortest_distance_text = display_distance(shortest_distance)

    print(f"Instancia: {instance_name}")
    print()
    print("Arvore de Espalhamento Minimo")
    print(f"Kruskal: {kruskal_weight}")
    print(f"Prim: {prim_weight}")
    print()
    print("Caminho Minimo")
    print(f"Dijkstra: {shortest_distance_text}")


def display_distance(distance: float) -> int | str:
    if distance == float("inf"):
        return "inf"
    return int(distance)


def run_all_instances() -> int:
    missing_files = []

    for index, filename in enumerate(DEFAULT_INSTANCES):
        path = INSTANCES_DIR / filename
        if not path.exists():
            missing_files.append(path)
            continue

        if index > 0:
            print()
        run_instance(path)

    if missing_files:
        if len(missing_files) > 0 and len(missing_files) < len(DEFAULT_INSTANCES):
            print()
        print("Arquivos ausentes:")
        for path in missing_files:
            print(path)
        return 1

    return 0


def main() -> int:
    args = build_parser().parse_args()
    if args.all == bool(args.arquivo):
        raise SystemExit("Informe um arquivo de instancia ou use --all.")

    if args.all:
        return run_all_instances()

    run_instance(args.arquivo)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
