class Banco:
    def __init__(self, nome: str):
        self.nome = nome  # nome do banco
        self.clientes = []  # nome do cliente
        self.contas = []  # numero da conta

    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()
