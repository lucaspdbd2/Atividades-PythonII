## Questão 1: Faça um procedimento recursivo que receba dois valores inteiros a e b e imprime o intervalo fechado entre eles. Se a > b imprima uma mensagem de erro.

def imprimir_intervalo(a, b):
    if a > b:
        print("Erro: o valor de 'a' deve ser menor ou igual a 'b'.")
    else:
        print(a)
        if a < b:
            imprimir_intervalo(a + 1, b)    

## Questão 2: Mudando apenas uma linha, altere o código anterior para imprimir o intervalo invertido.

def imprimir_intervalo_invertido(a, b):
    if a > b:
        print("Erro: o valor de 'a' deve ser menor ou igual a 'b'.")
    else:
        print(b)
        if b > a:
            imprimir_intervalo_invertido(a, b - 1)      

## Questão 3: Escreva uma função recursiva que recebe um inteiro n > 1 e calcula a soma dos valores entre n e 1.


def soma_recursiva(n):
    if n <= 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)        

## Questão 4: Escreva uma função recursiva que recebe um inteiro n e verifica se n é um valor primo, ou seja, se é divisível apenas por si mesmo e por 1.


def eh_primo(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return eh_primo(n, divisor - 1) 

## Questão 5: Implemente uma função recursiva que recebe um número inteiro decimal e retorna sua representação binária como uma string. Para realizar essa conversão, utilize o método de divisão sucessiva, onde você divide o número decimal por 2 e coleta os restos até que o quociente seja zero. A ordem dos restos coletados, de baixo para cima, forma o número binário correspondente.
    #Exemplo de Conversão:
    #Para converter o número decimal 13 para binário:
        #3 ÷ 2 = 6, resto 1
        #6 ÷ 2 = 3, resto 0
        #3 ÷ 2 = 1, resto 1
        #1 ÷ 2 = 0, resto 1
    #Lendo os restos de baixo para cima, obtemos o número binário 1101.


def decimal_para_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_para_binario(n // 2) + str(n % 2)    

## Implemente uma função recursiva em Python que realiza a travessia em pré-ordem de uma árvore binária representada por listas aninhadas. Na travessia em pré-ordem (ou pré-fixada), o nó raiz é visitado primeiro, seguido pela subárvore esquerda e, por fim, pela subárvore direita. A questão fixa as constantes RAIZ_IDX, ESQ_IDX, DIR_IDX representando os índices da lista onde se encontra o valor raíz, o nó a esquerda e o nó a direita. 
# # Representação visual da árvore:

 #      4
 #     / \
 #    2   5
 #   / \
 #  1   3

RAIZ_IDX = 0
ESQ_IDX = 1
DIR_IDX = 2 
def pre_ordem(arvore):
    if arvore is None:
        return
    print(arvore[RAIZ_IDX])  # Visita o nó raiz
    pre_ordem(arvore[ESQ_IDX])  # Visita a subárvore esquerda
    pre_ordem(arvore[DIR_IDX])  # Visita a subárvore direita  








    