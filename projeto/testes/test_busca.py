from algoritmos.busca import Busca
import random

def test_busca():
    tamanho_lista = random.choice([10, 100, 1000])
    print(f"Tamanho da Lista: {tamanho_lista}")

    lista_aleatoria = [random.randint(0, 100) for _ in range(tamanho_lista)]
    print("Lista Aleatória:", lista_aleatoria)

    print("Bubble Sort:", Busca.busca_sequencial(lista_aleatoria))
    print("Selection Sort:", Busca.busca_binaria(lista_aleatoria))

