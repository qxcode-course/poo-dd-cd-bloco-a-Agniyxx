class Carro:
    def __init__ (self, gasMax: int = 100, passMax: int = 2):
        self.passageiros: int = 0
        self.quilometros: int = 0
        self.gas: int = 0
        self.passMax: int = passMax
        self.gasMax: int = gasMax

    def __str__(self) -> str:
        return f"pass:{self.passageiros}, gas:{self.gas} km:{self.quilometros}"
    
    def show(self):
        print (self)

    def enter(self):
        if self.passageiros >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
             self.passageiros += 1
    
    def leave(self):
        if self.passageiros <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passageiros -= 1

    def abastecer(self, qtd: int):
        self.gas += qtd
        if self.gas >= self.gasMax:
            self.gas = self.gasMax
        
    def drive(self, distancia: int):
        if self.passageiros == 0:
            print("fail: não ha ninguem no carro")
        if self.gas == 0:
            print("fail: tanque vazio")
        if self.gas < distancia:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.quilometros += self.gas
            self.gas = 0
        else:
            self.gas -= distancia
            self.quilometros += distancia
            print("fail: tanque vazio  apos andar {quilometros} km")

def main():
    carro = Carro() 
