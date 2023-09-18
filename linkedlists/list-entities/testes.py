from No import No
from LS import LS
from LSE import LSE
from LDE import LDE

# Testes lista simples
print('-----------TESTE LISTA SIMPLES-------------')
testels = LS(5)
print('Lista Simples vazia criada.')
print('Vazia:', testels.empty())
print('Cheia:', testels.full())
print('Tamanho:', testels.size()) 
print('Adicionando os elementos 1, 2 e 4...')
testels.appendList(1)
testels.appendList(2,2)
testels.appendList(4,3)
print('Vazia:', testels.empty())
print('Cheia:', testels.full())
print('Tamanho:', testels.size())
print('A lista eh:')
testels.printList()
print('Adicionar 3 na posicao 3...')
testels.appendList(3,3)
print('Tamanho:', testels.size())
print('A lista eh:')
testels.printList()
testels.remove(5)
print('Removendo elemento 5...')
print('A lista eh:')
testels.printList()
print('Tamanho:', testels.size())
testels.remove(2)
print('Removendo elemento 2...')
print('A lista eh:')
testels.printList()
print('Tamanho:', testels.size())


# Testes LSE
'''print('-----------TESTE LSE-------------')
testelse = LSE()
print('LSE vazia criada.')
print('Vazia:', testelse.empty())
print('Tamanho:', testelse.size())
print('Adicionando elemento 3')
testelse.append(3)
print('Tamanho:', testelse.size())
print('Vazia:', testelse.empty())
print('Elemento da posicao 1:', testelse.element(1))
print('Elemento da posicao 3:', testelse.element(3))
print('A lista é:')
testelse.printList(), 

# Testes LDE
print('-----------teste lde-------------')
testelde = LDE()
print('Vazia:', testelde.empty())
print('Tamanho:', testelde.size())'''

print('===FIM===')
