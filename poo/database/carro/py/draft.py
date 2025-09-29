gasMax: int = 100
passMax: int = 2

class Carro:
    def __init__ (self, passageiros: int, km: int, gas: int, gasMax: int, passMax: int):
        self.passageiros: int = 0
        self.km: int = 0
        self.gas: int = 0
        self.gasMax: int = 100
        self.passMax: int = 2
 
     def __str__(self):
        return f"pass:{self.passageiros}, gas:{gas} km:{self.km}"
    
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

    def show(self):
        print (self)

    def main():