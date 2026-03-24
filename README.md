# Ordenacao por Comparacao

Implementacao em Python dos algoritmos `Insertion Sort` e `Selection Sort`.

## Arquivos

- `main.py`: executa uma instancia individualmente ou gera a tabela de tempos.
- `insertion_sort.py`: implementacao do Insertion Sort.
- `selection_sort.py`: implementacao do Selection Sort.
- `instancias-num/`: instancias de entrada fornecidas pelo professor.
- `results/`: instancias ordenadas geradas pela execucao.

## Como usar

Executar uma instancia individual e mostrar o tempo dos dois algoritmos:

```bash
python main.py instancia instancias-num/num.1000.1.in
```

Gerar a tabela CSV com todas as instancias:

```bash
python main.py tabela --saida minha-tabela.csv
```

