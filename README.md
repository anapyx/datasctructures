# Data Structures Project

**Interface visual de aplicação das estruturas de dados:**
- Listas Sequenciais
- Listas Simplesmente Encadeadas
- Listas Duplamente Encadeadas
- Pilhas
- Filas
- Árvores Binárias de Busca

**Disciplina:** Estrutura de Dados

**Professor:** Prof. Dr. Tiago Maritan

**Equipe de desenvolvedores:**
- Ana Cabral
- Bárbara Alves
- Felipe Silva Lima
- João Pedro Gomes

## Implementação
Foram criados Classes para cada tipo de Lista que contem métodos de funções para sua manipulação, além de uma Classe Nó que é utilizada nas Classes das Listas Simplesmente Encadeadas e Duplamente Encadeadas. Além disso foram utilizadas as bibliotecas de interface visual Tkinter e CustomTkinter para demonstração do funcionamento das listas e funções.

**Para utilizar o programa, além de claro, Python, o usuário deverá ter o [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter#installation) instalado, a pasta linkedlists e executar o arquivo tela1.py.**

Para mais informações sobre a biblioteca CustomTkinter: [Documentação CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

### Lista Sequencial
Está definida no arquivo LS.py. A classe LS se inicializa inserindo como entrada o tamanho da lista sequencial. Seus atributos definidos com a inicialização são:
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

### Lista Simplesmente Encadeada e Lista Duplamente Encadeada
Antes de definir as Listas Simplesmente Encadeada e Duplamente Encadeada, a utilização de uma classe Nó é necessária. A classe Nó é definida pelos seguintes atributos e métodos:
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

### Pilha
Está definida no arquivo PL.py. A classe PL se inicializa inserindo como entrada o tamanho da pilha. Seus atributos definidos com a inicialização são:
- dados: a lista de elementos com tamanho size(entrada)
- len: tamanho da lista de dados
- node_radius: tamanho da caixa do elemento

Os métodos da Pilha são:
- empty(): retorna se a lista está vazia
- full(): retorna se a lista está cheia
- size(): retorna 'len', o tamanho de dados[]
- top_stack(): retorna o elemento que está no topo da lista (último que foi inserido)
- appendList(elem,pos): adiciona elemento em determinada posição
- removeList(pos): remove elemento que se encontra no topo da pilha
- sortList(): coloca todos os elementos vazios no fim da lista
- draw_stack(canvas,size): função para representação gráfica da pilha na interface visual

## Interface Visual
A interface visual está implementada através dos arquivos tela1.py e tela2.py. Em que a tela 1 é a tela inicial para selecionar o tipo de lista e a tela 2 é a interface da lista escolhida. São importadas CustomTkinter, Os, Subprocess, Webbrowser além de No.py, LS.py, LSE.py e LDE.py.

### Tela Inicial
A primeira janela gera uma tela inicial com o visual implementado com o CustomTkinter, com o título do projeto na parte superior, botões para escolha de lista no centro, os créditos do projeto na parte inferior junto a um botão que leva para o projeto no github. Segue a lista de botões e as funções que implementam:
- button_ls: implementa a função open_ls() que irá abrir a tela2 com o menu da Lista Sequencial
- button_lse: implementa a função open_lse() que irá abrir a tela2 com o menu da Lista Simplesmente Encadeada
- button_lde: implementa a função open_lde() que irá abrir a tela2 com o menu da Lista Duplamente Encadeada
- button_doc: implementa a função open_doc() que irá abrir no navegador com o projeto no github.

### Tela das Listas
A segunda janela das listas abrirá conforme a lista escolhida na tela inicial. A janela tem o título da lista escolhida no topo, o menu de funções de implementação na parte esquerda e um quadro em branco do lado direito, neste acontecerá a implementação visual das funções nas listas. Os seguintes botões e funções são implementadas:
- buttonSize: implementa a função define_size() que inicializará a lista sequencial (apenas na lista sequencial)
- buttonHead: implementa a função create_head() que inicializará a cabeça das LSE/LDE (apenas nas listas LSE ou LDE)
- buttonAdd: implementa a função de adicionar elemento em determinada posiçao add_element()
- buttonRem: implementa a função de remover elemento em determinada posiçao remnove_element()
- buttonElem: implementa a função de buscar elemento search_element()
- buttonPos: implementa a função de buscar elemento pela posição search_position()
- buttonGoBack: implementa a função de retornar open_tela1() que abre novamente a tela inicial

As funções da tela utilizam internamente as funções de cada Classe de lista para gerar a representação visual dos elementos e mostrar resultados aos usuários.

Com isso, foi possível implementar as listas com uma boa representação visual de seu funcionamento.
