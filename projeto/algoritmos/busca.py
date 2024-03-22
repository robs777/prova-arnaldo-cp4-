class Busca():

    # sequencial
    def busca_sequencial(lista, valor_procurado):
    indice = 0
    for numero in lista:
        if numero == valor_procurado:
            return indice
        indice = indice + 1
        return -1

    def BuscaBinaria(lista, valor):
        min=0
        max=len(lista)-1
        while max>=min:
            chute = (min+mx)//2
            if lista[chute]==valor:
                return chute
            elif lista[chute]<valor:
                min = chute+1
            else:
                max=chute-1
        return -1