class Busca:
    @staticmethod
    def busca_sequencial(lista, valor_procurado):
        indice = 0
        for numero in lista:
            if numero == valor_procurado:
                return indice
            indice += 1
        return -1

    @staticmethod
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
