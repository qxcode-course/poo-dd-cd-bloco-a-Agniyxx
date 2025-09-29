class Carro:
    def __init__ (self, passageiros: int, km: int, gas: int):
        self.passageiros: int = passageiros
        self.km: int = km
        self.gas: int = gas
    




    def __str__(self) -> str:
        return f"pass:{self.passageiros}, gas:{gas} km:{self.km}"