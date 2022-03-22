from datetime import datetime # Exercício 2
import time                   # Funcão timer() usada em todos os exercícios
import random                 # Exercício 17

# ---------------------- Funções úteis ----------------------
def timer(segundosAntes, frase, segundosDepois):
    time.sleep(segundosAntes)
    print('\n{}'.format(frase))
    time.sleep(segundosDepois)


# ============================= OBSERVAÇÕES ==============================
# ---- Todos os programas propostos estão nesse mesmo arquivo.
# ---- Os scripts estão organizados nas seções abaixo, e serão executados de
#      acordo com a vontade do usuário
# ---- Há exercícios que variam da proposta, estes são marcados com comentários
#      explicativos

# ============================= MENU DE SCRIPTS ==============================
mensagemMenu = ('''
 ----------------- Escolha o programa que você deseja -----------------
 _______________________________________________________________________
CASO DESEJE SAIR DO PROGRAMA, DIGITE: 0
_______________________________________________________________________
1) Frase do dia
_______________________________________________________________________
2) Mensagem de boas-vindas.
_______________________________________________________________________
3) Nome e data de nascimento.
_______________________________________________________________________
4) Soma de dois números.
_______________________________________________________________________
5) Classificação de valores.
_______________________________________________________________________
6) Número antecessor e sucessor do resultado de uma soma.
_______________________________________________________________________
7) Dobro, triplo e raiz quadrada de um número.
_______________________________________________________________________
8) Calculadora de média
_______________________________________________________________________
9) Convertor de entre metros, centímetros e milímetros.
_______________________________________________________________________
10) Calcular a tabuada, de 1 a 10, de um número.
_______________________________________________________________________
11) Conversão de real para dólar (Valor para ser usado no dólar: 5.30)
_______________________________________________________________________
12) Programa que lê a largura e a altura de uma parede em metros, calcula
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que 
cada litro de tinta pinta uma área de 2 metros quadrados.
_______________________________________________________________________
13) Algoritmo que lê o preço de um produto e mostra seu novo 
preço, com 5% de desconto.
_______________________________________________________________________
14) Algoritmo que lê o salário de um funcionário e mostra seu
novo salário, com 15% de aumento.
_______________________________________________________________________
15) Programa que converte uma temperatura em graus Celsius
para graus Fahrenheit.
_______________________________________________________________________
16) Programa que recebe a quantidade de km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcular o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 
por Km rodado.
_______________________________________________________________________
17) Sorteio de alunos.
_______________________________________________________________________


--> Digite o NÚMERO do programa que deseja executar: ''')

# ============================= EXERCÍCIOS ==============================

# _____________________________________________________________________
def exe_1():
    frase = "'Uma pessoa que nunca cometeu um erro, nunca tentou nada novo.' - Albert Einstein"
    print('\n - A frase do dia é:\n' + frase)
    
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________

# OBSERVAÇÃO: O exercício propõe um output baseado no input do usuário
# porém decidi fazer o output baseado no horário em que o código é executado

def exe_2():
    horario = datetime.now()  
    horario = int(horario.strftime('%H%M%S'))  

    matina      = 60000
    meio_dia    = 120000
    noite       = 180000

    if (matina < horario < meio_dia):
        print('Bom dia! Bem vindo(a)!')

    elif (meio_dia < horario < noite):
        print('Boa tarde! Bem vindo(a)!')

    elif (noite < horario < matina):
        print('Boa noite! Bem vindo(a)!')

    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_3():
    timer(0, 'Me conte sobre você!', 2)
    nome = str(input('- Qual seu nome? Digite aqui! --> '))

    timer(0, 'Prazer {}! Quando você nasceu?'.format(nome), 0)
    anoNasc = input('- Digite aqui o ano em que você nasceu --> ')
    mesNasc = input('- Digite aqui o mês em que você nasceu --> ')
    diaNasc = input('- Digite aqui o dia em que você nasceu --> ')

    print('Legal! Então:')
    print('NOME: {} - DATA DE NASCIMENTO: {} / {} / {}'.format(
        nome, diaNasc, mesNasc, anoNasc))
    
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_4():
   
    timer(1, 'Vamos somar alguns números? Pode ser inteiro ou decimal!', 1)
    x = float(input('- Digite um número: '))
    y = float(input('- Digite um número: '))

    total = x + y
    print('Total: {}'.format(total))
        
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_5():
    x = input('Digite algo para verificá-lo:  ')
    print('O tipo primitivo desse dado é:', type(x))
    print('Só tem espaços?', x.isspace())
    print('É um número?', x.isnumeric())
    print('É uma letra?', x.isalpha())
    print('É alfanumérico?', x.isalnum())
    print('É uma letra maiúscula?', x.isupper())
    print('É uma letra minúscula?', x.islower())
    print('É um título?', x.istitle())

    timer(5, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_6():
    timer(1, 'Vamos somar e determinar o sucessor e antecessor de um valor INTEIRO!', 1)
    x = int(input('- Digite um número: '))
    y = int(input('- Digite um número: '))

    soma        = x + y
    antecessor  = int(soma) - 1
    sucessor    = int(soma) + 1

    print('O resultado da soma é: {}. \nSeu antecessor é: {} \nSeu sucessor é: {}'.format(soma, antecessor, sucessor))
    
    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_7():
    timer(1 ,'Vamos descobrir o dobro, triplo, e raíz quadrada de um número! Seja inteiro ou decimal.', 1)

    x = float(input(' - Digite um número: '))

    dobro   = x * 2
    triplo  = x * 3
    raiz    = round(x**.5, 2)

    print(
        'Seu número: {}\nO dobro do seu número: {}\nO triplo do seu número: {}\nA raíz quadrada do seu número: {}'
        .format(x, dobro, triplo, raiz))
    timer(5, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_8():
    timer(1, 'Vamos calcular a sua média!', 1)

    x = float(input('- Digite sua primeira nota: '))
    y = float(input('- Digite sua segunda nota: '))

    media = round((x + y) / 2, 2)

    print('Sua média é: {}'.format(media))
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_9():
    timer(1, 'Vamos calcular algumas medidas!', 1)

    m = float(input(' - Digite um valor em METROS: '))

    cm = m * 100
    mm = m * 1000

    print('Metros: {}m. \nCentímetros: {}cm \nMilímetros: {}mm'.format(m, cm, mm))
    timer(2, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_10():
    timer(1, 'Vamos ver a tabuada de 1 a 10 de um número? Pode ser inteiro ou decimal!', 1)

    def tabuada(x):
        for cont in range(1, 11):
            print('{} x {} = {}'.format(x, cont, x * cont))

    x = float(input('Digite um número qualquer: '))
    tabuada(x)
    
    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_11():
    timer(1, 'Conversão de REAL para DÓLAR', 1)
    timer(0, 'Para fins didáticos, o dólar será considerado $5.50', 1)

    reais     = float(input('-Digite aqui o valor em reais: R$ '))

    conversao = round(reais / 5.50, 2)  #dolares

    print('Cotação:\n - Reais: R$ {}\n - Dólares: US$ {}'.format(reais, conversao))

    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________


# _____________________________________________________________________
def exe_12():
    timer(
        1,
        'Problema: Calcular a área de uma parede e a quantidade de tinta necessária para pinta-lá.\n * Dado: 1L de tinta pinta uma área de 2m quadrados.',
        1)

    altura  = float(input(' - Digite aqui a altura da parede em METROS: '))
    largura = float(input(' - Digite aqui a largura da parede em METROS: '))

    area    = round(altura * largura, 2)
    tinta   = float(area / 2)

    print(
        'A quantidade de tinta, em litros, necessária para pintar uma parede de {}m de altura e {}m de largura é: {}L de tinta'
        .format(altura, largura, tinta))

    timer(3, 'Fim do exercício', 1)


# _____________________________________________________________________


# _____________________________________________________________________
def exe_13():
    timer(1, 'Aplicar desconto de 5% em produtos!', 1)

    produto = str(input(' - Digite qual o produto --> '))
    preço   = float(input(' - Digite o preço, em REAIS, deste produto: R$ '))

    desconto = 0.95

    descontoProd = round(preço * desconto, 2)

    print('{} --> Preço com desconto: R$ {}'.format(produto, descontoProd))

    timer(3, 'Fim do exercício', 1)


# _____________________________________________________________________


# _____________________________________________________________________
def exe_14():
    timer(1, 'Calcular aumento de salário em 15%', 1)

    funcionario     = str(input(' - Digite o nome do funcionário --> '))
    salario         = float(input(' - Digite o salário atual do funcionário: R$ '))
    
    aumento         = .15
    novo_salario    = round(salario + (salario*aumento), 2)

    print('NOME DO FUNCIONÁRIO: {}\nSALÁRIO ANTES DO DESCONTO: R$ {}\nSALÁRIO ATUALIZADO: R$ {}'.format(funcionario, salario, novo_salario))

    timer(3, 'Fim do exercício', 1)
    
# _____________________________________________________________________

# _____________________________________________________________________

# OBSERVAÇÃO: O exercício propõe uma conversão única de °C para °F, 
# porém aprimorei o códido permitindo a escolha da conversão 

def exe_15():
    timer(1, 
'''
Conversor de graus Celsius (°C) para graus Fahrenheit (°F)
- Digite 1 se deseja converter graus Celsius (°C) para graus Fahrenheit (°F) 
- Digite 2 se deseja converter graus Fahrenheit (°F) para graus Celsius (°C)''', 1)
      
    opcao = int(input('--> '))    
    if opcao == 1:
        c = float(input(' - Digite a temperatura em graus Celsius: '))
        f =  round(((9*c)/5)+32, 2)
        print(' - {}°C em Fahrenheit é {}°F'.format(c, f))
    elif opcao == 2:
        f = float(input(' - Digite a temperatura em graus Fahrenheit: '))
        c =  round(((f - 32) * 5)/9, 2)
        print(' - {}°F em Celsius é {}°C'.format(f, c))
    else:
        print('Opção inválida')
       
    timer(3, 'Fim do exercício', 1)
# _____________________________________________________________________

# _____________________________________________________________________
def exe_16():
    timer(1, 'Problema: Calcular o custo do aluguel de um carro considerando que:\n * Custa R$60.00 por dia de uso\n * Cada quilometro rodado custa R$0.15 ', 1)

    dias = float(input(' - Digite aqui por quantos dias o carro foi alugado --> '))
    km = float(input(' - Digite aqui quantos quilometros o carro andou enquanto alugado --> '))
    
    custo_dia = dias * 60
    custo_km  = km * .15
    
    total = custo_dia + custo_km
    
    print('RESULTADO:\n Um carro alugado por {} dias e com {}km rodados resulta em um custo de R$ {}'.format(dias, km, total))

    timer(3, 'Fim do exercício', 1)
   
# _____________________________________________________________________

# _____________________________________________________________________

# OBSERVAÇÃO: O exercício propõe um número fixo de alunos, porém aprimorei 
# o código para receber qualquer quantidade de alunos!

def exe_17():
    timer(1, 'Sorteio de alunos', 1)

    x = int(input(' - Digite quantos alunos participarão deste sorteio --> '))
    
    alunos = []
    for i in range(x):
        aluno   = str(input(' * ALUNO N°: {} - Digite o nome do aluno para adicioná-lo: '.format(i + 1)))
        alunos.append(aluno)
        i += 1
    
    print ('O aluno sorteado foi: ' + alunos[random.randrange( len( alunos ))])

    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________

# ======================= FIM DOS EXERCÍCIOS ==========================

# ------------------------------ // ------------------------------------

# ======================= EXECUÇÃO DO CÓDIGO ==========================
# _____________________________________________________________________

def menu(chave):  # Determina qual exercício(função) será executado
    a = chave
    menu = {
        1:  lambda a: exe_1(),
        2:  lambda a: exe_2(),
        3:  lambda a: exe_3(),
        4:  lambda a: exe_4(),
        5:  lambda a: exe_5(),
        6:  lambda a: exe_6(),
        7:  lambda a: exe_7(),
        8:  lambda a: exe_8(),
        9:  lambda a: exe_9(),
        10: lambda a: exe_10(),
        11: lambda a: exe_11(),
        12: lambda a: exe_12(),
        13: lambda a: exe_13(),
        14: lambda a: exe_14(),
        15: lambda a: exe_15(),
        16: lambda a: exe_16(),
        17: lambda a: exe_17(),
    }
    return menu[chave](a)

while True:
    resposta = int(input("\nDeseja ir para o menu?\n - Digite 1 para 'SIM'\n - Digite 2 para 'NÃO'\n --> "))

    if resposta == 1:
        chave = int(input(mensagemMenu))
        if not 0 <= chave <= 17:
            print('\nHm, não é uma opção, tente de novo...')
        elif chave == 0:
            print('Saindo...')
            break
        else:
            menu(chave)
    elif (resposta == 2):
        print('Saindo...')
        break
    else:
        print('\nHm, não é uma opção, tente de novo...')
