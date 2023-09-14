"""
Módulo de Processamento de Dados para Verificação de Cartões de Crédito

Este módulo fornece funcionalidades para processar e verificar números de cartões de crédito ou similares, determinando se eles são VÁLIDOS ou INVÁLIDOS com base em algoritmos de validação específicos. Ele inclui etapas para converter strings em listas de inteiros, dobrar valores numéricos, somar números em formatos específicos e verificar a validade do cartão de acordo com as regras de validação.
\n\n
Este módulo fornece uma função principal, `start()`, para processar e verificar números de cartões de crédito ou similares, determinando se eles são VÁLIDOS ou INVÁLIDOS com base em algoritmos de validação específicos. E retornando `True`, caso VÁLIDO, ou `False`, caso INVÁLIDO.

Autor: João Victor Lagos de Aguiar
Data de Criação: 13 de setembro de 2023

Uso:
-----
Para usar este módulo, importe-o em seu projeto e utilize as funções disponíveis. As principais funções incluem:

- `start(codigo_cartao)`: Função de entrada que processa um código de cartão fornecido pelo usuário e determina se ele é válido ou inválido com base nas etapas anteriores.

Exemplos de Uso:
---------------
Aqui estão alguns exemplos de como utilizar as funções deste módulo:

```python
# Importe o módulo em seu projeto
from cartao_verificador import *

# Verifique se um cartão é válido ou inválido
codigo_cartao = "123456"
start(codigo_cartao)
# Saída: O resultado final da etapa de verificação (por exemplo, 21) e uma mensagem indicando se o cartão é VÁLIDO ou INVÁLIDO. E retornando True, caso VÁLIDO, ou False, caso INVÁLIDO.
```python
"""

def string_list_to_int_list(lista):
    """
    Esta função recebe uma lista de strings e converte em uma lista de inteiros.\n

    Args:
        lista (list): Uma lista de strings contendo valores numéricos.

    Returns:
        None: A função modifica a lista original, não retorna uma nova lista.

    Exemplos:
        >>> minha_lista = ["12", "3", "99"]
        >>> string_list_to_int_list(minha_lista)
        >>> minha_lista
        [12, 3, 99]

        >>> outra_lista = ["45", "67", "8"]
        >>> string_list_to_int_list(outra_lista)
        >>> outra_lista
        [45, 67, 8]

        >>> lista_mista = ["abc", "xyz", "123"]
        >>> string_list_to_int_list(lista_mista)
        >>> lista_mista
        ['abc', 'xyz', 123]
    """

    for i in range(len(lista)):
        try:
            lista[i] = int(lista[i])
        except Exception:
            print("----------------------------------------------------------------")
            print("Lista contem valores não convertíveis para inteiro.\nVerifique se sua lista contem SOMENTE valores passíveis de ser tornados inteiros!")
            print("----------------------------------------------------------------")
            raise

def int_list_to_string_list(lista):
    """
    Esta função recebe uma lista e a converte em uma lista de strings.

    Args:
        lista (list): Uma lista.

    Returns:
        None: A função modifica a lista original, não retorna uma nova lista.

    Exemplos:
        >>> minha_lista = [12, 3, 99]
        >>> int_list_to_string_list(minha_lista)
        >>> minha_lista
        ['12', '3', '99']

        >>> outra_lista = [45, 67, 8]
        >>> int_list_to_string_list(outra_lista)
        >>> outra_lista
        ['45', '67', '8']

        >>> lista_mista = ["abc", "xyz", 123]
        >>> int_list_to_string_list(lista_mista)
        >>> lista_mista
        ['abc', 'xyz', '123']
    """

    for i in range(len(lista)):
        try:
            lista[i] = str(lista[i])
        except Exception:
            raise

def _double_num_values_in_list(lista):
    """
    Esta função recebe uma lista de valores (strings ou números) e duplica os valores numéricos encontrados.

    Args:
        lista (list): Uma lista de valores que podem incluir strings e números.

    Returns:
        None: A função modifica a lista original, não retorna uma nova lista.

    Exemplos:
        >>> minha_lista = ["12", "3", "99"]
        >>> double_num_values_in_list(minha_lista)
        >>> minha_lista
        ['24', '6', '198']

        >>> outra_lista = ["abc", "xyz", "123"]
        >>> double_num_values_in_list(outra_lista)
        >>> outra_lista
        ['abc', 'xyz', '246']

        >>> lista_mista = ["abc123", "!@#", "456"]
        >>> double_num_values_in_list(lista_mista)
        >>> lista_mista
        ['abc123', '!@#', '912']
    """
    
    for i in range(len(lista)):
        if str(lista[i]).isdigit():
            lista[i] = int(lista[i])*2
            lista[i] = str(lista[i]) 

def _split_and_flatten(lista):
    """
    Esta função recebe uma lista de strings e realiza duas etapas:
    
    1. Transforma a lista em uma única string, unindo todos os elementos.
    2. Transforma a string resultante em uma lista de caracteres individuais.
    
    Args:
        lista (list): Uma lista de strings.

    Returns:
        list: Uma lista de caracteres individuais obtida a partir da lista de entrada.

    Example:
        >>> split_and_flatten(["12", "3", "99"])
        ['1', '2', '3', '9', '9']

        >>> split_and_flatten(["abc", "xyz", "123"])
        ['a', 'b', 'c', 'x', 'y', 'z', '1', '2', '3']

        >>> split_and_flatten(["abc123", "!@#", "456"])
        ['a', 'b', 'c', '1', '2', '3', '!', '@', '#', '4', '5', '6']
    """

    # Transforma Lista em String
    lista = "".join(lista)

    # Transforma String em Lista
    lista = list(lista)

    return lista

def _first_step(codigo):
    """
    Esta função realiza uma série de etapas em uma sequência de caracteres 'codigo':

    1. Pega números de 2 em 2 (começando pelo antepenúltimo) e armazena em uma Lista.
    2. Dobra os valores da Lista.
    3. Dentro da lista, quebra números em dígitos.
    4. Soma os valores da lista.

    Args:
        codigo (str): Uma sequência de caracteres contendo números.

    Returns:
        int: A soma dos valores resultantes das etapas anteriores.

    Exemplos:
        >>> codigo = "123456"
        >>> first_step(codigo)
        16
        # Explicação:
        # - Pegando números de 2 em 2: ["5", "3", "1"]
        # - Dobrando os valores: ["10", "6", "2"]
        # - Quebrando números em dígitos: ["1", "0", "6", "2"]
        # - Somando os valores: 1 + 0 + 6 + 2 = 9
    """

    # Pega números de 2 em 2 (começando pelo antepenúltimo) e armazena em uma Lista
    codigo_fisrt_step =  codigo[-2::-2]
    codigo_fisrt_step = list(codigo_fisrt_step) # String vira Lista

    # Dobra os valores da Lista
    _double_num_values_in_list(codigo_fisrt_step)

    # Dentro da lista, quebra números em digitos. Exemplo: ["12","3","99"] -> ["1","2","3","9","9"]
    codigo_fisrt_step = _split_and_flatten(codigo_fisrt_step)

    # Soma os valores da lista
    string_list_to_int_list(codigo_fisrt_step) # Transforma a lista em inteiros para que seja possível fazer a soma
    result = sum(codigo_fisrt_step)

    return result

def _second_step(codigo, added_value):
    """
    Esta função realiza uma série de etapas em uma sequência de caracteres 'codigo' e adiciona um valor específico:

    1. Pega números de 2 em 2 (começando pelo último) e armazena em uma Lista.
    2. Converte os valores da Lista em inteiros.
    3. Soma os valores inteiros da Lista ao 'added_value'.

    Args:
        codigo (str): Uma sequência de caracteres contendo números.
        added_value (int): Um valor inteiro a ser adicionado ao resultado.

    Returns:
        int: A soma dos valores resultantes das etapas anteriores com o 'added_value'.

    Exemplos:
        >>> codigo = "123456"
        >>> added_value = 10
        >>> second_step(codigo, added_value)
        46
        # Explicação:
        # - Pegando números de 2 em 2: ["6", "4", "2"]
        # - Convertendo os valores em inteiros: [6, 4, 2]
        # - Somando os valores com 'added_value' (10): 6 + 4 + 2 + (10) = 22
    """

    # Pega números de 2 em 2 (começando pelo último) e armazena em uma Lista
    codigo_second_step = codigo[::-2]
    codigo_second_step = list(codigo_second_step)

    string_list_to_int_list(codigo_second_step) # Transforma a lista em inteiros para que seja possível fazer a soma
    result = sum(codigo_second_step) + added_value

    return result

def start(codigo_cartao):
    """
    Verifica a validade de um código de cartão de crédito ou similar.

    Esta função realiza as seguintes etapas para verificar a validade de um código de cartão:
    1. Executa a primeira etapa de processamento (_first_step) no código de entrada.
    2. Executa a segunda etapa de processamento (_second_step) no código de entrada com base no resultado da primeira etapa.
    3. Exibe o resultado final da verificação.
    4. Retorna True se o cartão for VÁLIDO (final_result == 20), caso contrário, retorna False.

    Args:
        codigo_cartao (str): Uma sequência de caracteres representando o código do cartão a ser verificado.

    Returns:
        bool: True se o cartão for VÁLIDO, False se o cartão for INVÁLIDO.

    Nota:
        Certifique-se de que o código do cartão fornecido seja uma sequência de caracteres válida de acordo com as especificações da sua aplicação.
    """

    result_first_step = _first_step(codigo_cartao)
    final_result = _second_step(codigo_cartao, result_first_step)
    print(final_result)


    if final_result==20:
        print("Cartão VÁLIDO!")
        return True
    else:
        print("Cartão INVÁLIDO!")
        return False

    

if __name__ == "__main__":
    codigo_cartao = str(input("Digite o código do cartão: "))
    start(codigo_cartao)