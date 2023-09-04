class LS:
    def __init__(self):
        self.dados = []
        self.len = len(self.dados)

    # Verifica se a lista está vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Verifica se a lista está cheia
    def full(self):
        return self.len == self.dados.size()
    
    # Retorna o tamanho da lista
    def size(self):
        return self.len
    
    # Printa os elementos da lista
    def print(self):
        current = self.head
        while current:
            print(current.content)
            current = current.next

    # Checa o elemento de determinada posição
    def element(self, pos):
        if pos > self.len or pos <= 0:
            raise ValueError("Posição inválida.")
        return self.dados[pos-1]
    
    # Checa as posições de um determinado elemento
    def position(self, elem):
        for i in range(0, self.len - 1):
            if self.dados[i] == elem:
                return i + 1
        
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Checa as posições de um determinado elemento após a primeira ocorrência
    def position(self, elem, desloc):
        for  i in range(desloc, self.len - 1):
            if self.dados[i] == elem:
                return i+1
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Inserção de Nó em uma determinada posição
    def append(self, pos, elem):
        if self.full() or pos > self.len or pos <= 0:
            return False
        
        for i in range (self.len, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]
            
        self.dados[pos - 1] = elem
        
        self.len += 1
        
        return True
    
    # Remoção de Nó de uma determinada posição
    def remove(self, pos):
        if pos > self.len or pos <=0:
            raise ValueError("Posição inválida.")
        
        aux = self.dados[pos - 1]
        
        for i in range(pos - 1, self.len):
            self.dados[i] = self.dados[i + 1]
        
        self.len -= 1
        return aux