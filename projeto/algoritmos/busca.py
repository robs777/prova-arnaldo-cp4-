class Busca:
    @staticmethod

    # Busca por um elemento presente no vetor  e Não presente
    def busca_sequencial1(lista, valor_procurado):
        indice = 0
        for numero in lista:
            if numero == valor_procurado:
                return indice
            indice += 1
        return -1
    
    # Busca em um vetor vazio
    def busca_sequencial2(lista, valor_procurado):
        if not lista:
            return -1
        indice = 0
        for numero in lista:
            if numero == valor_procurado:
                return indice
            indice += 1
        return -1
    
    # Busca em um vetor com um único elemento
    def busca_sequencial3(lista, valor_procurado):
        indice = 0
        for numero in lista:
            if numero == valor_procurado:
                return indice
            indice += 1
        return -1



    @staticmethod
    # Busca por um elemento presente no vetor , Não presente , Busca em um vetor vazio e Busca em um vetor com um único elemento
    def busca_binaria(lista, valor):
        min = 0
        max = len(lista) - 1
        while max >= min:
            chute = (min + max) // 2
            if lista[chute] == valor:
                return chute
            elif lista[chute] < valor:
                min = chute + 1
            else:
                max = chute - 1
        return -1
    
    
