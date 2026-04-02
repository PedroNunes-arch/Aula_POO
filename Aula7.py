from typing_extensions import Generic
from typing import TypeVar
T = TypeVar("T")

class Caixa(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    def pegar_item(self) -> T :
        return self.item

if __name__ == "__main__":
    caixa_int = Caixa[int](42)
    caixa_str = Caixa[str]('Python')
    caixa_lista = Caixa[list]([1,2,3])

    print(caixa_int.pegar_item())
    print(caixa_str.pegar_item())
    print(caixa_lista.pegar_item())
#------------------------------------
print(5 + 3.14)
print(int(5+3.14))
print("Idade: " + str(25))
#-------------------------------------
def repetir(texto, vezes):
  return texto * vezes

print(repetir("Python", 3))
#-----------------------------------
class Animal:
  def fazer_som(self):
    print('O animal faz um som')

class Cachorro(Animal):
  def fazer_som(self):
    print('O cachorro faz AU AU AU!')

class Gato(Animal):
  def fazer_som(self):
    print('O gato MIAU!')

class Vaca(Animal):
  def fazer_som(self):
    print('A vaca MOO!')

def fazer_barulho(animal: Animal):
  animal.fazer_som()

animais = [Cachorro(), Gato(), Vaca(), Animal()]

for animal in animais:
  fazer_barulho(animal)
#-------------------------------------------
class Calcuadora:
  def somar(self, a, b=None):
    if b is None:
        return a + a
    return a + b
  
  if __name__ == '__main__'
  calc = Calcuadora()
  print(calc.somar(5))
  print(calc.somar(5, 3))
