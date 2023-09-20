class LS:
    def __init__(self, size=0):
        self.dados = [None]*size
        self.len = len(self.dados)

    # Verifica se a lista esta vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Verifica se a lista esta cheia
    def full(self):
        if self.empty() == True:
            return False
        elif self.empty() == False:
            if None in self.dados:
                return False
            else:
                return True
    
    # Retorna o tamanho da lista
    def size(self):
        self.len = len(self.dados)
        return self.len
    
    # Printa os elementos da lista
    def printList(self):
        print(self.dados)

    # Checa o elemento de determinada posicao
    def element(self, pos):
        if pos > self.len or pos <= 0:
            raise ValueError("Posicao invalida.")
        return self.dados[pos-1]
    
    # Checa as posicoes de um determinado elemento
    def position(self, elem):
        auxPos = []
        aux = 0
        for i in range(0, self.len - 1):
            if self.dados[i] == elem:
                auxPos.append(i+1)
                aux = 1
        if aux == 1:
            return auxPos
        else:
            raise ValueError("Nenhum elemento foi encontrado.")
    
    # Insercao de elemento em uma determinada posicao
    def appendList(self, elem, pos=1):
        if self.len == 0 and pos == 1:
            self.dados.append(elem)
            return True
        if (self.full() == True) or (pos!=1 and pos > self.len) or pos <= 0:
            return ("Posicao invalida.")
        last = self.dados[self.len-1]
        if last is not None:
            self.dados.append(last)
        for i in range (self.len - 1, pos-1, -1):
            if self.dados[i-1] is not None:
                self.dados[i] = self.dados[i - 1]            
        self.dados[pos - 1] = elem
        self.len
        return True
    
    # Remocao de uma determinada posicao
    def remove(self, pos):
        auxReorder = []
        if pos > self.len or pos <=0:
            raise ValueError("Posicao invalida.")
        else:
            self.dados[pos-1] = None
            return True
    
    # Remoção de determinado elemento em todas as aparicoes
    def removeData(self,elem):
        auxPos = self.position
        for i in range(auxPos[i-1]):
            self.remove(auxPos[i-1])
            return True
        
    # Ordena a lista para que todos os elementos nulos fiquem no final
    def sortList(self):
        auxReorder = []
        for i in range(self.len-1):
            if self.dados[i] is not None:
                auxReorder.append(self.dados[i])
        while len(auxReorder)<self.len:
            auxReorder.append(None)
        self.dados = auxReorder
        return True
