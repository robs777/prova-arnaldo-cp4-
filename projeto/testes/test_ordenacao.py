from algoritmos.ordenacao import Ordenacao
import random

def test_ordenacao():

    #Ordenado crescente
    lista_crescente = sorted(random.sample(range(1, 100), 10))
    

    # Não ordenado
    lista_nao_ordenado = [random.randint(1, 100) for _ in range(10)]
    

    # Ordenado descrescente
    lista_descrescente = sorted(random.sample(range(1, 100), 10), reverse=True)
    

    # Vazio
    lista_vazia = []
    

    # Um elemento
    lista_um_elemento = [random.randint(1, 100)]
   

    # Repetidos
    lista_repetidos = [random.randint(1, 100) for _ in range(10)]
    

    # Negativos
    lista_negativos = [random.randint(-100, 100) for _ in range(10)]
    


    # BUBBLE SORT
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_crescente))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_nao_ordenado))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_descrescente))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_vazia))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_um_elemento))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_repetidos))
    print("Bubble Sort: ", Ordenacao.bubble_sort(lista_negativos))

    # SELECTION SORT
    print("Selection Sort: ", Ordenacao.selection_sort(lista_crescente))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_nao_ordenado))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_descrescente))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_vazia))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_um_elemento))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_repetidos))
    print("Selection Sort: ", Ordenacao.selection_sort(lista_negativos))

    # INSERTION SORT
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_crescente))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_nao_ordenado))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_descrescente))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_vazia))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_um_elemento))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_repetidos))
    print("Insertion Sort: ", Ordenacao.insertion_sort(lista_negativos))



    # MERGE SORT
    print("Merge Sort: ", Ordenacao.mergeSort(lista_crescente))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_nao_ordenado))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_descrescente))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_vazia))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_um_elemento))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_repetidos))
    print("Merge Sort: ", Ordenacao.mergeSort(lista_negativos))

    # QUICK SORT
    print("Quick Sort: ", Ordenacao.quickSort(lista_crescente))
    print("Quick Sort: ", Ordenacao.quickSort(lista_nao_ordenado))
    print("Quick Sort: ", Ordenacao.quickSort(lista_descrescente))
    print("Quick Sort: ", Ordenacao.quickSort(lista_vazia))
    print("Quick Sort: ", Ordenacao.quickSort(lista_um_elemento))
    print("Quick Sort: ", Ordenacao.quickSort(lista_repetidos))
    print("Quick Sort: ", Ordenacao.quickSort(lista_negativos))
