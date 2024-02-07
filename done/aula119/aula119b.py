import os
import platform
import json


def limpar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def listar(tarefas):
    print()

    if not tarefas:
        print("Nenhuma tarefa para listar")
        return

    print("Tarefas:")
    for tarefa in tarefas:
        print(f"\t{tarefa}")

    print()


def desfazer(tarefas, tarefas_refazer):
    print()

    if not tarefas:
        print("Nenhuma tarefa para desfazer")
        return

    tarefa = tarefas.pop()
    print(f"{tarefa=} removida da lista de tarefas.")
    tarefas_refazer.append(tarefa)

    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()

    if not tarefas_refazer:
        print("Nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    print(f"{tarefa=} adicionada na lista de tarefas.")
    tarefas.append(tarefa)

    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()

    tarefa = tarefa.strip()
    if not tarefa:
        print("Você não digitou uma tarefa.")
        return

    print(f"{tarefa=} adicionada na lista de tarefas.")
    tarefas.append(tarefa)

    print()
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="UTF-8") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)

    return tarefas


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, "w", encoding="UTF-8") as arquivo:
        tarefas = json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

    return tarefas


CAMINHO_ARQUIVO = "aula119/aula119.json"
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

comandos = {
    "listar": lambda: listar(tarefas),
    "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
    "refazer": lambda: refazer(tarefas, tarefas_refazer),
    "clear": lambda: limpar(),
    "adicionar": lambda: adicionar(tarefa, tarefas),
}

while True:
    print("Comandos: listar, desfazer e refazer")

    tarefa = input("Digite uma tarefa ou comando: ")
    comando = comandos.get(tarefa, lambda: adicionar(tarefa, tarefas))

    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue
