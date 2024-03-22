"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python NÃO TEM modificadores de acesso

Mas podemos seguir as seguintes convenções:
  (sem underline) = public
      pode ser usado em qualquer lugar
_ (um underline) = protected
      não DEVE ser usado fora da classe
      ou suas subclasses.
__ (dois underlines) = private
      "name mangling" (desfiguração de nomes) em Python
      _NomeClasse__nome_attr_ou_method
      só DEVE ser usado na classe em que foi
      declarado.
"""


class Foo:
    def __init__(self):
        self.public = "isso é público"
        self._protected = "isso é protegido"
        self.__private = "isso é privado"

    def metodo_public(self):
        return "metodo_public"

    def _metodo_protected(self):
        return "_metodo_protected"

    def _metodo_private(self):
        return "__metodo_private"


f = Foo()

print(f.public, f._protected, f.__private)
print(f.metodo_public())
