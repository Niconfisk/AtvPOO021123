from professor import Professor
from disciplina import Disciplina
from atividade import Atividade

def exibir_menu():
    print("\n1. Adicionar disciplina")
    print("2. Adicionar atividade")
    print("3. Marcar atividade como concluída")
    print("4. Listar atividades em aberto")
    print("5. Listar atividades concluídas")
    print("6. Listar disciplinas do professor")
    print("0. Sair")

n = input('Insira o nome do professor: ')
professor = Professor(n)

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome_disciplina = input("Digite o nome da disciplina: ")
        disciplina = Disciplina(nome_disciplina)
        professor.adicionar_disciplina(disciplina)

    elif opcao == "2":
        nome_disciplina = input("Digite o nome da disciplina: ")
        for disc in professor.disciplinas:
            if disc.nome == nome_disciplina:
                nome_atividade = input("Digite o nome da atividade: ")
                data_atividade = input("Digite a data da atividade (DD/MM/AAAA): ")
                atividade = Atividade(nome_atividade, data_atividade)
                disc.adicionar_atividade(atividade)
                break
        else:
            print("\nDisciplina não encontrada ou data duplicada.")

    elif opcao == "3":
        nome_disciplina = input("Digite o nome da disciplina: ")
        for disc in professor.disciplinas:
            if disc.nome == nome_disciplina:
                nome_atividade = input("Digite o nome da atividade: ")
                for atividade in disc.atividades:
                    if atividade.nome == nome_atividade:
                        atividade.marcar_concluida()
                        print("\nAtividade marcada como concluída.")
                        break
                else:
                    print("\nAtividade não encontrada.")
                break
        else:
            print("\nDisciplina não encontrada.")

    elif opcao == "4":
        nome_disciplina = input("Digite o nome da disciplina: ")
        for disc in professor.disciplinas:
            if disc.nome == nome_disciplina:
                disc.listar_atividades_em_aberto()
                break
        else:
            print("\nDisciplina não encontrada.")

    elif opcao == "5":
        nome_disciplina = input("Digite o nome da disciplina: ")
        for disc in professor.disciplinas:
            if disc.nome == nome_disciplina:
                disc.listar_atividades_concluidas()
                break
        else:
            print("\nDisciplina não encontrada.")

    elif opcao == "6":
        professor.listar_disciplinas()

    elif opcao == "0":
        print("\nSaindo do programa.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")