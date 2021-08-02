from datetime import datetime
import time
# ---------------------- Funções úteis ----------------------
def timer(segundosAntes, frase, segundosDepois):
    time.sleep(segundosAntes)
    print(frase)
    time.sleep(segundosDepois)

# ============================= OBSERVAÇÕES ==============================
# ---- Todos os programas propostos estão nesse mesmo arquivo.
# ---- Os scripts estão organizados nas seções abaixo, e serão executados de
#      acordo com a vontade do usuário

# ============================= MENU DE SCRIPTS ==============================
mensagemMenu =  ('''
 ----------------- Escolha o programa que você deseja -----------------
 _______________________________________________________________________
CASO DESEJE SAIR DO PROGRAMA, DIGITE: 0
_______________________________________________________________________
1) Mensagem de boas-vindas.
_______________________________________________________________________
2) Frase do dia
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


--> Digite o NUMERO do programa que deseja executar: ''')



# ============================= EXERCÍCIOS ==============================

# _____________________________________________________________________
def exe_1():
    frase = "'Uma pessoa que nunca cometeu um erro, nunca tentou nada novo.'"
    print('\n - A frase do dia é:\n' + frase)
    timer(1, 'Fim do exercício', 1)
# _____________________________________________________________________



# _____________________________________________________________________
def exe_2():
    horario = datetime.now() # Determinar o horário
    horario = int(horario.strftime('%H%M%S')) # Converter para int
    
    matina= 60000
    meio_dia = 120000
    noite = 180000
    
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
    
    timer(0, 'Prazer {}! Quando você nasceu?'.format(nome), 2)
    anoNasc = input('- Digite aqui o ano em que você nasceu --> ')
    mesNasc = input('- Digite aqui o mês em que você nasceu --> ')
    diaNasc = input('- Digite aqui o dia em que você nasceu --> ')
    
    print('Legal! Então:')
    print('NOME: {} - DATA DE NASCIMENTO: {}/{}/{}'.format(nome, diaNasc, mesNasc, anoNasc))
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_4():
    somando = True
    while somando:
        timer(1, 'Vamos somar alguns números? Pode ser inteiro ou decimal!', 1)
        x = float(input('- Digite um número: '))
        y = float(input('- Digite um número: '))
        
        total = x + y
        print('Total: {}'.format(total))
        timer(1, 
        '''
        Para continuar somando, digite "1"
        Quer sair? Digite "2"
        ''' ,1)
        resposta = int(input('--> '))
        
        if resposta == 2:
            break
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_5():
    x = input('Digite algo para verificá-lo:')
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
    timer(1, 'Vamos somar e determinar o sucessor e antecessor de um valor INTEIRO!',1)
    x = int(input('- Digite um número: '))
    y = int(input('- Digite um número: '))

    soma = x + y
    antecessor = int(soma) - 1
    sucessor = int(soma) + 1
    
    print('O resultado da soma é: {}. \nSeu antecessor é: {} \nSeu sucessor é: {}'.format(soma, antecessor, sucessor))
    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_7():
    timer(1, 'Vamos descobrir o dobro, triplo, e raíz quadrada de um número! Seja inteiro ou decimal.',1)

    x = float(input(' - Digite um número: '))
    
    dobro   = x*2
    triplo  = x*3
    raiz    = round(x**.5, 2)
    
    print('Seu número: {}\nO dobro do seu número: {}\nO triplo do seu número: {}\nA raíz quadrada do seu número: {}'.format(x, dobro, triplo, raiz))
    timer(5, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_8():
    timer(1, 'Vamos calcular a sua media!',1)
    
    x = float(input('- Digite sua primeira nota: '))
    y = float(input('- Digite sua segunda nota: '))

    media = round((x+y)/2, 2)
    
    print('Sua média é: {}'.format(media))
    timer(1, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_9():
    timer(1, 'Vamos calcular algumas medidas!', 1)

    m = float(input(' - Digite um valor em METROS: '))
    
    cm = m * 100
    mm = m * 1000

    print('Metros: {}m. \nCentímetros: {}cm \nMilimetros: {}mm'.format(m, cm, mm))
    timer(2, 'Fim do exercício', 1)

# _____________________________________________________________________



# _____________________________________________________________________
def exe_10():
    timer(1, 'Vamos ver a tabuada de 1 a 10 de um valor INTEIRO', 1)
    
    def tabuada(x):
        for cont in range(1,11):
            print('{0} x {1} = {2}'.format(x,cont,x*cont))


    x = int(input('Digite um número INTEIRO: '))
    tabuada(x)
    timer(3, 'Fim do exercício', 1)

# _____________________________________________________________________
# ======================= FIM DOS EXERCÍCIOS ==========================

# ------------------------------ // ------------------------------------

# ======================= EXECUÇÃO DO CÓDICO ==========================
# _____________________________________________________________________

def menu(chave): # Determina qual exercício(função) será executado
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
    10: lambda a: exe_10() 
    }
    return menu[chave](a)

loop = True
while loop:
    resposta = int(input("\nDeseja ir para o menu?\n - Digite 1 para 'SIM'\n - Digite 2 para 'NÃO'\n --> "))
                   
    if resposta == 1:
        chave = int(input(mensagemMenu))
        if not 0 <= chave <= 10:
            raise ValueError
        elif chave == 0:
            print('Saindo...')
            break
        else:  
            menu(chave)
    elif (resposta == 2):
        print('Saindo...')
        break
    else:
        print('Valor incorreto, tente novamente')
