# 2026-05-22

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        lista_de_listas = [[1]]

        for _ in range(1, numRows):
            lista = [1]
            for i in range(1, len(lista_de_listas[-1])):
                soma = lista_de_listas[-1][i] + lista_de_listas[-1][i-1]
                lista.append(soma)
            lista.append(1)
            lista_de_listas.append(lista)

        return lista_de_listas