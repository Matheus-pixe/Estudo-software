#calculadora
def Ler(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Deve ser colocado um numeral!')

def Op(mensagem):
    while True:
        texto = input(mensagem).lower().strip()
        if texto:
            return texto
        print('Deve ser utilzado uma operação') #MELHORAR

def opera():
    match operacao:
        case '+':
            print(f'{num1}+{num2}={num1+num2}')
        case '-':
            print(f'{num1}-{num2}={num1-num2}')
        case 'x'|'*':
            print(f'{num1}x{num2}={num1*num2:.2f}')
        case '/':
            if num2 == 0:
                print('Não é possivel a divisão por zero')
            else:
                print(f'{num1}/{num2}={num1/num2:.2f}')
        case '**':
            print(f'{num1}^{num2}={num1**num2}') #MELHORAR

        case _:
            print('Infelizmente deve ser digitado alguma operação.(+, -, x , /,**)')
            return operacao

        
while True:
    print('='*21)
    print('     CALCULADORA')
    print('='*21)
    num1 = Ler('Escreva um numero: \n')
    num2 = Ler('Outro numero: \n')
    operacao = Op('Qual será a operação usada? + , - , x|* ,/ ou **?\n').lower().strip()
    
    print("Ok. calculando...")
    opera()
    if input('Calcular novamente? (s/n)\n').lower().strip() != 's':
        break
    print('Calculo Finalizado')
    
