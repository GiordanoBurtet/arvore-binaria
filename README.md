# arvore-binaria
Operações de dados abstratos Set em uma árvore binária em python
Estrutura de Dados de Conjunto (Set) baseada em Árvore Binária de Pesquisa (BST)

Justificativa da Escolha da Estrutura de Dados
A escolha de uma Árvore Binária de Pesquisa (BST) como estrutura subjacente para implementar um Conjunto (Set) tem várias vantagens:

Ordenação: Os elementos em uma BST são armazenados de forma ordenada, o que facilita a realização de operações como busca, inserção e remoção com complexidade eficiente.

Eficiência: As operações em BSTs têm complexidade média eficiente. A busca, inserção e remoção são realizadas em O(log n), onde 'n' é o número de elementos no conjunto, na média de casos. No pior caso, a complexidade é O(n), mas isso é raro com árvores bem balanceadas.

Armazenamento de Elementos Únicos: BSTs garantem que não haja elementos duplicados, o que é uma característica fundamental de um conjunto.

Flexibilidade: A BST pode ser facilmente estendida para suportar operações de conjunto comuns, como união, interseção e diferença.

Complexidade de Tempo e Espaço
Aqui estão as complexidades de tempo e espaço esperadas para cada operação na estrutura de dados de Conjunto baseada em BST:

Inserção (inserir):

Complexidade de Tempo: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
Complexidade de Espaço: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
Remoção (remover):

Complexidade de Tempo: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
Complexidade de Espaço: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
Verificação de Pertencimento (contem):

Complexidade de Tempo: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
Complexidade de Espaço: O(log n) em média, O(n) no pior caso (árvore desequilibrada).
União (uniao):

Complexidade de Tempo: O(m log n), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser unido.
Complexidade de Espaço: O(m + n), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser unido.
Interseção (intersecao):

Complexidade de Tempo: O(min(m log n, n log m)), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser interseccionado.
Complexidade de Espaço: O(min(m, n)), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser interseccionado.
Diferença (diferenca):

Complexidade de Tempo: O(m log n), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser subtraído.
Complexidade de Espaço: O(m + n), onde 'n' é o número de elementos no conjunto atual e 'm' é o número de elementos no conjunto a ser subtraído.
