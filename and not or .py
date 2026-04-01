# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

# idade = int(input('Idade'))
# autorizacao = input('Possui autorização: ')
# pode = (idade >=18) and (autorizacao)

# print('Pode participar? - ', pode)

# -------------------------------------------->
# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba "Peso normal" ou "Fora da faixa".

# peso = float(input('Digite seu peso:  '))

# altura = float(input('Digite sua altura: '))

# imc = peso/altura**2
# print(imc)

# peso_normal = imc >= 18.5 and imc<= 24.9

# v = peso_normal and 'Peso Normal' or 'Fora '
# print(v)

#------------------------------------------------


# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" ou "Acesso negado".

# nome = str(input("Digite seu nome: "))
# senha = int(input("Digite sua senha: "))

# admin = nome == "admin" and senha ==1234

# v = admin and 'Acesso Liberado' or 'Acesso Negado'
# print(v)

#-------------------------------------------------

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

# valor = float(input("Digite o valor da compra: "))
# vip = str(input('Você é vip? '))

# descontovip = valor >=100 or vip == "sim"

# desconto = valor * 0.10

# valortotal = valor - d 

# valorfinal = valortotal == "valor final com desconto" or valor == "valor original"

# print(valortotal)


# v = valortotal and print(valortotal) or valor print(valor)

# print(v)

# admin = nome == "admin" and senha ==1234

# v = admin and 'Acesso Liberado' or 'Acesso Negado'
# print(v)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.


idade = int(input("Digite seu idade: "))

peso = float(input('Digite seu peso: '))

pode = idade >=16 or idade <=69 and peso >=50 
npode = idade <16 or idade >69 and peso <50

print('Você pode doar', pode or 'Você não pode doar', npode)

print(pode == 'Vc pode doar' or  npode == 'Não pode'  )


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.



# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".



# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".


# ano = int(input('Digite um ano: '))


# Ano_bissexto = ano // (4 and 400)

# Ano_nao_bissexto = ano 

# print(Ano_bissexto and Ano_nao_bissexto)




# print(ano)  == True, 'Ano Bissexto' or ==False, 'Ano não bissexto')





# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.



# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.





# instrucoes


# # AND -  E xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# x  =  10

# y  =  10

# carteira_motorista = 'sim'

# idade  = 25

# print(carteira_motorista == 'sim' and idade < 17)



# # OR - OU  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# tempo  =  input('Digite o tempo: ')

# print(tempo == 'calor' or  tempo == 'frio'  )

# # ambas verdadeiras ou ao menos uma expressão true



# # not não  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# # é veridadeiro quando ao contrário,

# salario =  input('O salario caiu? ')

# print(not tempo  == 'calor' and  not  salario == 'não') 


# # in -  dentro xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# lista  =  [1,2,3]

# print(1 in lista or not 2 in lista)


