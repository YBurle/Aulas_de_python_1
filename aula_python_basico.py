    # Declarando uma variável e uso da função print
x=10
print(x, type(x))
print("valor")
print("x=10")
print('valor={}' .format(x))
print(f'valor={x}\n') #o "f" não pode ficar separado do '. O \n serve para que na execuçao ele crie um espaço

    # Atribuição múltipla
a, b = 1, 2 #atribuimos as variáveis a e b os valores 1 e 2, respectivamente
print('Antes da troca')
print(f'Valor das variáveis: a={a}, b={b}')

    # Primeira troca (uso de uma terceira variável)
c = a
a = b
b = c
print('Primeira troca')
print(f'Valor das variáveis: a={a}, b={b}')

# Segunda troca (troca declarada)
a, b = b, a
print('Segunda troca')
print(f'Valor das variáveis: a={a}, b={b}\n')

    # Uso de operadores compostos:
print(f'x={x}')
x+=2 #somando 2 ao valor de x
print(f'x={x}')
x-=2 #subtraindo 2 ao valor de x
print(f'x={x}')
x*=2 #multiplicando por 2 o valor de x
print(f'x={x}')
x/=2 #dividindo por 2 o valor de x
print(f'x={x}')
x%=2 #calculando o resto da divisão inteira por 2
print(f'x={x}\n')

    # Tipos de escopo
def multiplicador(numero):
    a = 2  # esta variável tem escopo local, pois encontra-se dentro de uma função
    print(f"Dentro da função, a variável vale: {a}")
    return a * numero

a = 3  # esta variável tem escopo global, pois encontra-se fora de uma função, sendo válida para tdo o código
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")
print(b)


def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # como foi alterado anteriormente, essa variável passa a ter caráter global
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global que será desconsiderada
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}\n")

    #Exemplo de lista sequencial
lista = [101,202,303,404,505] #construção de uma lista utilizando os colchetes
print(type(lista))
print(f'Posição 0 = {lista[0]}')
print(f'Posição 1 = {lista[1]}')
print(f'Posição 2 = {lista[2]}')
print(f'Posição 3 = {lista[3]}')
print(f'Posição 4 = {lista[4]}')
print(f'Lista completa = {lista}')

l = list('abc') #construção de uma lista utilizando o tipo list
print(l)
print('')

    #Exemplo de tupla:
lista_tupla = (1,2,3) #construção de uma lista tupla usando os parenteses (que são opcionais, o que irá caracterizar a tupla são as vírgulas
print(type(lista_tupla))
print(lista_tupla)
print(f"Posição 0 = {lista_tupla[0]}") #imprimindo apenas um item da lista

t = tuple('123') #construção de uma lista tupla usando o tipo tuple
print(t)
print('')

    #Exemplo de range:

print(list(range(5))) #escreve uma lista com 5 números, iniciando do 0
print(list(range(5, 10))) #escreve uma lista com início 5 e fim antes do 10
print(list(range(0, 10, 2))) #escreve uma lista com início 0, fim antes do 10 e sendo incrmenetado de 2 em 2
print('')

    #Exemplo de dicionário
pessoas = {1111:['nome 01'], 2222:['nome 02'], 3333:['nome 03'], 4444:['nome 04']}
print(pessoas)
print(f'Primeira pessoa = {pessoas[1111]}')

cpf = {'09552165407': 'Yasmin Burle', '11278096442': 'Giovanni', '65262069487': 'Analice'}
print(cpf['09552165407'])
print('')

    #Exemplo de tipo booleano
print(2<3) #fará um teste lógico e retornará o valor "true"
print(not(2<3)) #O operador not irá inverter o valor booleano
print('')

    #Manipulação de string
curso='ensino a distancia'
print(curso)
print(curso.upper()) #tudo em letra maiuscula
print(curso.lower()) #tudo em letra minuscula
print(curso.split()) #particiona a string em suas palavras
print('')

    #exercicios da aula
a = ['10']
b = ['20']
c = ['30']
r = a+b+c #ira apenas concatenar os valores pois estamos passando uma lista de strings
print(f'r={r}')

a = [int(a[0])*2]
b = [int(b[0])*3]
c = [int(c[0])*4]
x = a+b+c #iremos transformar a lista de string em uma lista de inteiros e multiplicar pelo valor desejado
print(x)

a = int(a[0])*2 #estamos transformando o valor presente na posicao 0 da lista em um inteiro e por conseguinte multiplicando pelo valor desejado
b = int(b[0])*3
c = int(c[0])*4
y = a+b+c
print(y)
print('')
    #Uso da função input:
nome = input('Entrada: ') #essa função irá exibir no console a mensagem escrita dentro do parenteses, receber o valor e guardar dentro da variável a qual se encontra
print(f'a entrada foi: {nome}')

cpf = input('Digite seu cpf: ')
print(f'Seu cpf é: {cpf}')
print(type(cpf)) #tudo que for escrito dentro da função input será vista como uma string

    #Uso da funçào eval
num = eval(input('Digite um valor o valor a ser dobrado: ')) #A função eval será responsável por transformar o que for recebido no input de str para int
num *= 2
print(f'O resultado é igual a: {num}')
