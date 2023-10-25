# Data Structures Project

**Interface visual de aplicação das estruturas de dados:**
- Listas Sequenciais
- Listas Simplesmente Encadeadas
- Listas Duplamente Encadeadas
- Pilhas
- Filas
- Árvores Binárias de Busca

**Disciplina:** Estrutura de Dados I

**Professor:** Prof. Dr. Tiago Maritan

**Equipe de desenvolvedores:**
- Ana Cabral
- Bárbara Alves
- Felipe Silva Lima
- João Pedro Gomes

## Implementação
Foram criadas classes para cada tipo de estrutura de dados com métodos para sua manipulação e utilizadas as bibliotecas de interface visual Tkinter e CustomTkinter para criação de um programa que demonstra o funcionamento dessas estruturas.

**Para utilizar o programa, além de claro, Python, o usuário deverá ter o [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter#installation) instalado, a pasta ds-project e executar o arquivo AppScreen.py.**

Para mais informações sobre a biblioteca CustomTkinter: [Documentação CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)


### Lista Sequencial
Está definida no arquivo LS.py. 
<details>
<summary>Métodos e Atributos da Lista Sequencial</summary>

A classe LS se inicializa inserindo como entrada o tamanho da lista sequencial. Seus atributos definidos com a inicialização são:
- dados: a lista de elementos com tamanho size(entrada)
- len: tamanho da lista dados
- node_radius: tamanho da caixa do elemento

Os métodos da Lista Sequencial São:
- empty(): retorna se a lista está vazia
- full(): retorna se a lista está cheia
- size(): retorna 'len', o tamanho de dados[]
- printList(): mostra todos os elementos da lista
- element(pos): checa elemento em determinada posição
- position(elem): checa posições de determinado elemento
- appendList(elem,pos): adiciona elemento em determinada posição
- removeList(pos): remove elemento de determinada posição
- removeData(elem): remove determinado elemento de todas as posições
- sortList(): coloca todos os elementos vazios no fim da lista
- draw_sequential_list(canvas,size): função para representação gráfica da lista na interface visual

</details>


### Lista Simplesmente Encadeada e Lista Duplamente Encadeada
Antes de definir as Listas Simplesmente Encadeada e Duplamente Encadeada, a utilização de uma classe Nó é necessária. 

<details>
<summary>Métodos e Atributos da LSE e LDE</summary>
A classe Nó é definida pelos seguintes atributos e métodos:
- content: conteúdo do nó
- next: 'aponta' para próximo nó
- prev: 'aponta' para o nó anterior (utilizado apenas na LDE)
- getContent(): retorna o conteúdo do nó atual
- setContent(content): entra com o conteúdo do nó atual
- getNext(): retorna o conteúdo do próximo nó
- setNext(next): entra com o conteúdo do próximo nó
- getPrev(): retorna o conteúdo do nó anterior (utilizado apenas na LDE)
- setPrev(prev): entra com o conteúdo do nó anterior (utilizado apenas na LDE)

Então, as Listas Simplesmente Encadeada e Duplamente Encadeada estão definidas como Classes nos arquivos LSE.py e LDE.py. As classes LSE e LDE se inicializam com a criação de uma 'cabeça' e utilizam a biblioteca Customtkinter. Seus atributos definidos com a inicialização são:
- head: cabeça da lista, o primeiro que gera o nó
- content: conteúdo do nó
- len: tamanho da lista
- node_radius: tamanho da caixa do elemento
- node_spacing: espaço entre cada caixa de elemento

Os métodos da Lista Sequencial São:
- empty(): retorna se a lista está vazia
- full(): retorna se a lista está cheia
- size(): retorna 'len', o tamanho de dados[]
- printList(): mostra todos os elementos da lista
- element(pos): checa elemento em determinada posição
- position(elem): checa posições de determinado elemento
- appendList(elem,pos): adiciona elemento em determinada posição
- removeAtStart(): remove a cabeça se a lista tiver tamanho um
- removeAtPosition(pos): remove o elemento de determinada posição
- removeList(pos): aplica as duas funções anteriores em um método só
- draw_singly_linked_list(canvas): função para representação gráfica da lista na interface visual (apenas na LSE)
- draw_doubly_linked_list(canvas): função para representação gráfica da lista na interface visual (apenas na LDE)
</details>

### Pilha
Está definida no arquivo PL.py.
<details>
<summary>Métodos e Atributos da Pilha</summary>
A classe PL se inicializa inserindo como entrada o tamanho da pilha. O funcionamento utiliza a lógica das Listas Sequenciais e por isso utiliza os mesmos métodos. Seus atributos definidos com a inicialização são:
- dados: a lista de elementos com tamanho size(entrada)
- len: tamanho da lista de dados
- node_radius: tamanho da caixa do elemento

Os métodos da Pilha são:
- empty(): retorna se a lista está vazia
- full(): retorna se a lista está cheia
- size(): retorna 'len', o tamanho de dados[]
- top_stack(): retorna o elemento que está no topo da lista (último que foi inserido)
- appendList(elem,pos): adiciona elemento no topo da pilha
- removeList(pos): remove elemento que se encontra no topo da pilha
- draw_stack(canvas,size): função para representação gráfica da pilha na interface visual
</details>

### Fila
Está definida no arquivo FL.py.
<details>
<summary>Métodos e Atributos da Fila</summary>
A classe FL se inicializa inserindo como entrada o tamanho da fila. O funcionamento utiliza a lógica das Listas Sequenciais e por isso utiliza os mesmos métodos. Seus atributos definidos com a inicialização são:
- dados: a lista de elementos com tamanho size(entrada)
- len: tamanho da lista de dados
- node_radius: tamanho da caixa do elemento

Os métodos da Pilha são:
- empty(): retorna se a lista está vazia
- full(): retorna se a lista está cheia
- size(): retorna 'len', o tamanho de dados[]
- element(): retorna o elemento que está no inicio da fila (primeiro)
- appendList(elem,pos): adiciona elemento no topo da pilha
- removeList(pos): remove elemento que se encontra no topo da pilha
- draw_queue(canvas,size): função para representação gráfica da fila na interface visual
</details>

## Interface Visual
A interface visual está implementada através dos arquivos AppScreen.py, listscr.py (implementação das listas) e treescr.py (implementação das filas, pilhas e abp). Em que a AppScreen é a tela inicial para selecionar o tipo de lista e as outras telas são as interfaces específica da estruturas de dados selecionadas. São importadas nas telas o Tkinter, CustomTkinter, Os, Subprocess, Webbrowser além de No.py, LS.py, LSE.py e LDE.py, FL.py, PL.py, ABP.py.

A primeira janela gera uma tela inicial com o visual implementado com o CustomTkinter, com o título do projeto na parte superior, botões para escolha de estruturas de dados, os créditos do projeto na parte inferior junto a um botão que leva para o diretório do projeto no Github.
