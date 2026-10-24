def ler_numero(mensagem):
    """Lê um número válido informado pelo usuário."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número, como 10 ou 2,5.")


def calcular(num1, num2, operacao):
    """Executa a operação escolhida e retorna o resultado."""
    if operacao == "+":
        return num1 + num2
    if operacao == "-":
        return num1 - num2
    if operacao == "*":
        return num1 * num2
    if operacao == "/":
        if num2 == 0:
            return None
        return num1 / num2
    return "operacao_invalida"


def main():
    print("=" * 30)
    print("       CALCULADORA")
    print("=" * 30)

    while True:
        num1 = ler_numero("Primeiro número: ")
        operacao = input("Operação (+, -, *, /) ou 'sair': ").strip().lower()

        if operacao == "sair":
            print("Calculadora encerrada.")
            break

        if operacao not in ("+", "-", "*", "/"):
            print("Operação inválida. Escolha +, -, * ou /.")
            continue

        num2 = ler_numero("Segundo número: ")
        resultado = calcular(num1, num2, operacao)

        if resultado is None:
            print("Erro: não é possível dividir por zero.")
        else:
            print(f"Resultado: {resultado:g}" if isinstance(resultado, float) else f"Resultado: {resultado}")

        print("-" * 30)


if __name__ == "__main__":
    main()
