from clientes import Clientes
from contas import Conta, ContaEspecial
from bancos import Banco

# cria cliente
joao = Clientes(nome='Joao da Silva', telefone='999999999')
maria = Clientes(nome='Maria da Silva', telefone='888888888')

# print(joao.nome)

# cria conta
conta_joao = Conta(clientes=[joao.nome], numero='001', saldo=0)

# cria conta especial
conta_maria = ContaEspecial(
    clientes=[maria.nome], numero='002', saldo=0, limite=100)


# print(conta_joao.resumo())
conta_joao.deposito(150)
conta_joao.saque(500)
print(conta_joao.extrato())

# print(conta_maria.resumo())
conta_maria.deposito(200)
conta_maria.saque(300)
print(conta_maria.extrato())

# cria banco
meu_banco = Banco('Meu Banco')

# abre conta no banco
# meu_banco.abre_conta(conta=conta_joao)
meu_banco.abre_conta(conta=conta_joao)
meu_banco.abre_conta(conta=conta_maria)

print(meu_banco.lista_contas())
