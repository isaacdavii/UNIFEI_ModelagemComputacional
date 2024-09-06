from sympy import symbols, Eq, solve

idadeDiofanto = symbols('idadeDiofanto')
print('SOBRE DIOFANTO')
print('\n')

print('Consideramos que todas as variáveis escritas "quantas partes" estarão fracionados, i.e,  1 / "x" sendo x um número inteiro que representa a parte inteira')
print('\n')

infancia = int(input('Quantas partes viveu como infante? '))

juventude = int(input('Quantas partes viveu como jovem? '))

barbaCrescida = int(input('Quantas partes viveu até se casar? '))

filhoNasce = int(input('Quantos anos após casamento nasceu seu filho? '))

aposMorteFilho = int(input('Quantos anos viveu após a morte do filho? '))

equation = Eq(idadeDiofanto, (idadeDiofanto / infancia) + (idadeDiofanto / juventude) + (idadeDiofanto / barbaCrescida) + filhoNasce + (idadeDiofanto / 2) + aposMorteFilho)

solution = solve(equation, idadeDiofanto)

print(f'Diofanto viveu {solution[0]} anos!')