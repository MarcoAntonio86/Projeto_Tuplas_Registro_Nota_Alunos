alunos = []  # Lista de alunos (tuplas)
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar aluno e notas \n'
    '2. Calcular médias \n'
    '3. Exibir alunos com médias mais altas e mais baixas \n'
    '4. Sair \n')

print(menu)

while escolha != 4:
    escolha = int(input('Informe a opção: '))
    
    if escolha == 1:
        nome_aluno = input('Informe o nome do aluno: ')
        notas = []
        disciplina = input('Informe a disciplina: ')
        while True:
            nota = float(input('Informe a nota (ou digite -1 para parar): '))
            if nota == -1:
                break
            notas.append(nota)
        alunos.append((nome_aluno, disciplina, notas))  # Adiciona uma tupla à lista

    elif escolha == 2:
        if len(alunos) == 0:
            print('Não há alunos para calcular médias!')
        else:
            for aluno in alunos:
                nome_aluno, disciplina, notas = aluno
                media = sum(notas) / len(notas)
                print(f'A média do aluno {nome_aluno} na disciplina {disciplina} é {media:.2f}')

    elif escolha == 3:
        if len(alunos) == 0:
            print('Não há alunos para exibir médias!')
        else:
            medias = [(aluno[0], sum(aluno[2]) / len(aluno[2])) for aluno in alunos]
            medias.sort(key=lambda x: x[1])
            menor_media = medias[0]
            maior_media = medias[-1]

            print(f'Aluno com a média mais baixa: {menor_media[0]}, Média: {menor_media[1]:.2f}')
            print(f'Aluno com a média mais alta: {maior_media[0]}, Média: {maior_media[1]:.2f}')

    elif escolha == 4:
        print("Aplicativo encerrado.")
        break

    else:
        print('Opção inválida')
