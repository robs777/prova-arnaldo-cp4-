class Ordenacao:
    @staticmethod
    # todos
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]: 
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                elif lista[j] < lista[j+1]: 
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    @staticmethod
    #todos
    def selection_sort(lista):
        n = len(lista)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if lista[minimo] > lista[j]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i] 
        return lista

    @staticmethod
    # Todos exceto ordenado decre
    def insertion_sort(lista):
        n = len(lista)
        for j in range(1, n):
            chave = lista[j]
            i = j - 1
            while i >= 0 and lista[i] > chave:
                lista[i + 1] = lista[i]
                i = i - 1
            lista[i + 1] = chave

    # decrescente 
    def insertion_sort_dec(lista):
        n = len(lista)
        for j in range(1, n):
            chave = lista[j]
            i = j - 1
            while i >= 0 and lista[i] < chave: # Alteração aqui: lista[i] < chave
                lista[i + 1] = lista[i]
                i = i - 1
            lista[i + 1] = chave


    @staticmethod
    def mergeSort(alist):
        aux = [0] * len(alist)
        Ordenacao.mergesort(alist, aux, 0, len(alist) - 1)

    @staticmethod
    def merge(A, aux, esquerda, meio, direita):
        for k in range(esquerda, direita + 1):
            aux[k] = A[k]
        i = esquerda
        j = meio + 1
        for k in range(esquerda, direita + 1):
            if i > meio:
                A[k] = aux[j]
                j += 1
            elif j > direita:
                A[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                A[k] = aux[j]
                j += 1
            else:
                A[k] = aux[i]
                i += 1

    @staticmethod
    def mergesort(A, aux, esquerda, direita):
        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2
        Ordenacao.mergesort(A, aux, esquerda, meio)
        Ordenacao.mergesort(A, aux, meio + 1, direita)
        Ordenacao.merge(A, aux, esquerda, meio, direita)

    @staticmethod
    def quickSort(alist):
        Ordenacao.quicksort(alist, 0, len(alist) - 1)

    @staticmethod
    def quicksort(lista, inicio, fim):
        if inicio < fim:
            pivo = Ordenacao.dividir(lista, inicio, fim)
            Ordenacao.quicksort(lista, inicio, pivo - 1)
            Ordenacao.quicksort(lista, pivo + 1, fim)

    @staticmethod
    def dividir(lista, inicio, fim):
        pivo = lista[fim]
        posicao_pivo = inicio
        for i in range(inicio, fim):
            if lista[i] < pivo:
                lista[i], lista[posicao_pivo] = lista[posicao_pivo], lista[i]
                posicao_pivo += 1
        lista[posicao_pivo], lista[fim] = lista[fim], lista[posicao_pivo]
        return posicao_pivo
