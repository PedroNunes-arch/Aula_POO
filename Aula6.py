class Veiculo:
    def __init__(self,marca):
        self.marca  = marca

    def mover(self):
        return "Esta se movendo"
class Carro(Veiculo):
    def mover(self):
        return "O carro está dirigindo na estrada"

class Bicicleta(Veiculo):
    def over(self):
        return "Bicicleta está na estrada"

c = Carro("Honda")
b = Bicicleta("Caloi")

print(c.marca, "→", c.mover())
print(b.marca, "→", b.mover())

#----------------------------------------

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
class Estudante(Pessoa):
  def __init__(self, nome, idade, matricula):
    super().__init__(nome, idade)
    self.matricula = matricula
  
e = Estudante("Helena", 20, "12345")
print(e.nome, "→", e.matricula, "→" )

#----------------------------------------

class Animal:
  def __init__(self, nome. idade):
    self.nome = nome
    self.idade = idade

  def fazer_som(self):
    return "Fazer som de animal"

  def descrever(self):
    return f"Eu sou {self.nome}, tenho {self.idade} anos"
  class Cachorro(Animal):
    def __init__(self,nome,idade,raca):
      super()._init__(nome,idade)
      self.raca = raca

    def fazer_som(self):
      return "Au au au!"
  class Gato(Animal):
    pass

  rex = Cachorro('Maui', 4,'Bulldog Frances')
  print(rex.descrever())
  print(rex.fazer_som())
  print("Raca:", rex.raca)
  print()

  Print('Rex é instancia de Cachorro?', isinstance(rex,Gato))
  Print('Rex é instancia de Animal?', isinstance(rex,Gato))
  Print('Rex é instancia de Gato?', isinstance(rex,Gato))

#----------------------------------------
class A: pass
class B: pass
class C(A,B): pass
print(C.__mro__)
help(C)
