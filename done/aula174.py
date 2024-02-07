"""
Copiar -> shutil.copy
Copiar Árvore recursivamente -> shutil.copytree
Apagar Árvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear/Mover -> shutil.move ou os.rename
"""

import os
import shutil

HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "EXEMPLO")
NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")

shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + "_EITA")
