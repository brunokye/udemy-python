"""
PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
extrair texto e imagens, manipular metadados, e mais.

A documentação contém todas as informações necessárias para usar PyPDF2.
Link: https://pypdf2.readthedocs.io/en/3.0.0/

Ative seu ambiente virtual
pip install pypdf2
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAL = PASTA_RAIZ / "pdfs_originais"
PASTA_NOVA = PASTA_RAIZ / "arquivos_novos"
RELATORIO_BACEN = PASTA_ORIGINAL / "R20230210.pdf"

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page00 = reader.pages[0]
imagem00 = page00.images[0]

# print(page00.extract_text())

# with open(PASTA_NOVA / imagem1.name, "wb") as fp:
#     fp.write(imagem00.data)

# writer = PdfWriter()
# writer.add_page(page00)

# with open(PASTA_NOVA / "page00.pdf", "wb") as arquivo:
#     writer.write(arquivo)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f"page0{i}.pdf", "wb") as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

merger = PdfMerger()
files = [
    PASTA_NOVA / "page00.pdf",
    PASTA_NOVA / "page01.pdf",
]

for file in files:
    merger.append(file)

with open(PASTA_NOVA / "merged.pdf", "wb") as arquivo:
    merger.write(arquivo)
