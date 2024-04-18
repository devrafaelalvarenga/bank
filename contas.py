class Conta(Banco):
    def __init__(self, clientes: str, numero: str, saldo: int = 0):
        self.clientes = clientes  # nome do cliente
        self.numero = numero  # numero da conta
        self.saldo = 0  # saldo da conta
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"Conta corrente: {self.numero}  Saldo: {
              self.saldo:.2f}")

    def saque(self, valor: int):
        if self.saldo > valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            self.operacoes.append(['SAQUE INDISPONIVEL', valor])

    def deposito(self, valor: int):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])

    def extrato(self):
        print(f"Extrato Conta corrente: {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\nSALDO:     {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes: str, numero: str, saldo: int = 0, limite: int = 0):
        Conta.__init__(self, clientes=clientes, numero=numero, saldo=saldo)
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def saque(self, valor: int):

        if self.saldo > valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        elif (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            self.operacoes.append(['SAQUE INDISPONIVEL', valor])

    def extrato(self):
        print(f"Extrato Conta corrente: {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:.2f}")
        print(f"LIMITE     {self.limite:.2f}\nSALDO      {
              self.saldo + self.limite:.2f}\n")

    def resumo(self):
        print(f"Conta corrente: {self.numero}  Saldo: {
              self.saldo + self.limite:.2f}")
