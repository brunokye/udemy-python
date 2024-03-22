from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo o arquivo.")
        arquivo = open(caminho_arquivo, modo, encoding="UTF-8")
        yield arquivo
    except Exception as error:
        print(f"Ocorreu um erro: {error}")
    finally:
        print("Fechando o arquivo.")
        arquivo.close()


with my_open("aula150/aula150.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n", 123)
    arquivo.write("Linha 3\n")
    print("WITH", arquivo)
