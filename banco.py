class ContaBancaria:
    titular=""
    saldo=0.0
    limite=0.0
    def __init__(self,titular,saldo,limite):
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
    def exibir_info(self):
        print("Titular: ",self.titular)
        print("Saldo: ",self.saldo)
        print("Limite: ",self.limite)
    def depositar(self,valor):
        if valor>0:
            self.saldo+=valor
            self.exibir_saldo()
            print(1)
        else:
            print(0)
    def levantar(self,valor):
        if valor<0 or valor>self.limite:
            print(0)
        else:
            self.saldo-=valor
            self.exibir_saldo()
            print(1)
    def exibir_saldo(self):
        print("Saldo: ",float(self.saldo))
titular=input("Como se chama? ")
cb=ContaBancaria(titular,10,10)
cb.exibir_info()
escolha=""
while True:
    escolha=input("Que operação deseja fazer? (depositar,levantar,versaldo,verinfo) [q para sair] ")
    if escolha=="depositar":
        valor=float(input("Quanto quer depositar? "))
        cb.depositar(valor)
    elif escolha=="levantar":
        valor=float(input("Quanto quer levantar? "))
        cb.levantar(valor)
    elif escolha=="versaldo":
        cb.exibir_saldo()
    elif escolha=="verinfo":
        cb.exibir_info()
    elif escolha=="q":
        print("Adeus!")
        break
    else:
        print("O quê?")
