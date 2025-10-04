class Calculadora:
    def __init__(self, batteryMax: int= 100):
        self.display = 0
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def recarregar(self, increment: int):
        self.battery += increment
        if self.battery >= self.batteryMax:
         print("fail: limite de carga atingido")
        else:
             self.battery += 1

    def soma(self, a: int, b: int):
        if self.battery > 0:
            self.display = a + b
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")
    
    def divisão(self, num: int, den: int):
        if den == 0:
            print("fail: divisao por zero")
        elif self.battery > 0:
            self.display = num/den
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")
    
    
        