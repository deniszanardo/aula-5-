# 1. Verificação de maioridade e permissão
Enunciado:
Crie um programa que leia a idade do usuário e se ele possui autorização dos pais (responda True ou False).
O usuário pode participar da atividade se tiver 18 anos ou mais ou tiver autorização dos pais.
Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

idade = int(input('Idade: '))
autorizacao = input('Possui autorização: ')
pode = (idade >= 18) and (autorizacao)


print('Pode participar? - ', pode)