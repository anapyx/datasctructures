class LS:
    def __init__(self):
        self.dados = []
        self.len = len(self.dados)

    # Verifica se a lista est� vazia
    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    # Verifica se a lista est� cheia
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

    # Checa o elemento de determinada posi��o
    def element(self, pos):
        if pos > self.len or pos <= 0:
            raise ValueError("Posi��o inv�lida.")
        return self.dados[pos-1]
    
    # Checa as posi��es de um determinado elemento
    def position(self, elem):
        for i in range(0, self.len - 1):
            if self.dados[i] == elem:
                return i + 1
        
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Checa as posi��es de um determinado elemento ap�s a primeira ocorr�ncia
    def position(self, elem, desloc):
        for  i in range(desloc, self.len - 1):
            if self.dados[i] == elem:
                return i+1
        raise ValueError("Nenhum elemento foi encontrado.")
    
    # Inser��o de N� em uma determinada posi��o
    def append(self, pos, elem):
        if self.full() or pos > self.len or pos <= 0:
            return False
        
        for i in range (self.len, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]
            
        self.dados[pos - 1] = elem
        
        self.len += 1
        
        return True
    
    # Remo��o de N� de uma determinada posi��o
    def remove(self, pos):
        if pos > self.len or pos <=0:
            raise ValueError("Posi��o inv�lida.")
        
        aux = self.dados[pos - 1]
        
        for i in range(pos - 1, self.len):
            self.dados[i] = self.dados[i + 1]
        
        self.len -= 1
        return aux