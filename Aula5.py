class Conta:
    def __init__(self):
        self.saldo = 1000
    def saldo(self):
        return self.saldo
conta = Conta()
print(conta.saldo)

conta.saldo = 2000

print(conta.saldo)
#------------------------------
class Conta:
    def __init__(self):
      self.saldo = 1000
    @property
    def saldo(self):
        return self.saldo
conta = Conta()
print(conta.saldo)

conta.saldo = 2000

print(conta.saldo)
#-------------------------------
class Conta:
    def __init__(self):
      self.__saldo = 42
t = Conta()
print(t._Conta__saldo)
t._Conta__saldo = 100
print(t._Conta__saldo)
#-------------------------------
from dataclasses import dataclass
@dataclass(frozen=True)
class Conta:
    saldo: float = 1000
    nome: str = 'Maria'

conta = Conta()
print(conta.saldo)
