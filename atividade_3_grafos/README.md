# Atividade 3 - Grafos

Esta atividade implementa, em Python, os algoritmos pedidos pelo professor para trabalhar com grafos:

- `Kruskal` e `Prim` para arvore de espalhamento minimo;
- `Dijkstra` para caminho minimo de `0` ate `n - 1`.

## Arquivos

- `main.py`: executa uma instancia ou todas de uma vez.
- `graph_reader.py`: le o arquivo e monta o grafo.
- `kruskal.py`: implementacao do Kruskal.
- `prim.py`: implementacao do Prim.
- `dijkstra.py`: implementacao do Dijkstra.
- `validator.py`: guarda os resultados de referencia.
- `instancias/`: pasta das instancias `dij10.txt`, `dij20.txt`, `dij40.txt` e `dij50.txt`.

## Formato da entrada

Cada arquivo comeca com `n`, o numero de vertices. Depois disso, vem os pesos do triangulo superior da matriz de adjacencia.

Exemplo:

```text
4
23 17 19
22 20
25
```

Esse arquivo representa as arestas:

- `0,1 = 23`
- `0,2 = 17`
- `0,3 = 19`
- `1,2 = 22`
- `1,3 = 20`
- `2,3 = 25`

## Como executar

Para rodar uma instancia:

```bash
python atividade_3_grafos/main.py atividade_3_grafos/instancias/dij10.txt
```

Para rodar todas:

```bash
python atividade_3_grafos/main.py --all
```

No modo `--all`, o programa procura automaticamente por:

- `atividade_3_grafos/instancias/dij10.txt`
- `atividade_3_grafos/instancias/dij20.txt`
- `atividade_3_grafos/instancias/dij40.txt`
- `atividade_3_grafos/instancias/dij50.txt`

## Saida

A saida mostra apenas os resultados calculados pelos algoritmos.

Exemplo:

```text
Instancia: dij10

Arvore de Espalhamento Minimo
Kruskal: 7072
Prim: 7072

Caminho Minimo
Dijkstra: 5183
```

## Resumo rapido dos algoritmos

`Kruskal` ordena as arestas por peso e vai escolhendo as menores sem formar ciclo.

`Prim` comeca em um vertice e vai expandindo a arvore sempre pela menor aresta disponivel.

`Dijkstra` calcula a menor distancia da origem `0` ate o destino `n - 1`. O caminho continua sendo reconstruido internamente, mas a saida padrao mostra apenas o valor da distancia minima.
