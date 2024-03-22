import os
import platform
import json


def limpar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
        print(tarefa)


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
refazer = []

while True:
    comando = input(
        "Comandos: listar, desfazer, refazer e clear\
        \nDigite uma tarefa ou comando: "
    ).lower()

    if comando == "listar":
        if len(tarefas) == 0:
            print("Nada a listar.")
            continue
        limpar()
        listar_tarefas(tarefas)
    elif comando == "desfazer":
        if len(tarefas) == 0:
            print("Nada a desfazer.")
            continue
        tarefa = tarefas.pop()
        refazer.append(tarefa)
        limpar()
        listar_tarefas(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
    elif comando == "refazer":
        if len(refazer) == 0:
            print("Nada a refazer.")
            continue
        tarefa = refazer.pop()
        tarefas.append(tarefa)
        limpar()
        listar_tarefas(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
    elif comando == "clear":
        limpar()
    else:
        tarefas.append(comando)
        salvar(tarefas, CAMINHO_ARQUIVO)
