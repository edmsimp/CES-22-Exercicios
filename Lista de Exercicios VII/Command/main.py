from tkinter import *
from tkinter.font import Font

# Para o exercício, simplificou-se o exemplo do banco para basicamente
# 3 usos: verificar o saldo, verificar a dívida e fazer uma transferência.
#   - Verificar saldo apenas exibe quanto dinheiro você tem
#   - Verificar divida apenas exibe quanto você deve
#   - Para fazer uma transferência, insira um valor válido na barra de texto
#      e aperte no botão, o valor será descontado do saldo.
# Por fim, o histórico armazena cada ação dessas!

# Pseudo Data Base => Apenas para testes!
saldo = 1000
divida = 200
historico_aux = ""

# Definições básicas da tela
tela = Tk()
tela.title("Banco")
tela.geometry("800x500+10+20")

# Blocos interativos da GUI
valor_transf = Entry()
valor_transf.insert(END, "Insira um valor")
descricao = Entry()
saida = Entry()
historico_nome  = Entry()
historico = Text()
label1 = Label(tela, text="Bem vindo ao banco, selecione uma das ações abaixo.", font=(12))

# Classe receiver, que realiza as operações em si
class Receiver:
    def __init__(self):
        self.descricao = descricao      

    def descrever_acao(self, texto):
        global historico_aux
        descricao.delete(0, END)
        descricao.insert(END, texto)
        historico_aux = texto + " "

    def inserir_valor(self, valor):
        global historico_aux
        saida.delete(0, END)
        saida.insert(END, "R$ " + str(valor) + ",00")
        historico_aux = historico_aux + "R$ " + str(valor) + ",00\n"
        historico.insert('1.0', historico_aux)

    def reduzir_saldo(self, valor):
        global historico_aux
        global saldo
        saida.delete(0, END)
        saida.insert(END, "R$ " + valor + ",00")
        try: 
            saldo = saldo - int(valor)
            historico_aux = historico_aux + "R$ -" + valor + ",00\n"
        except ValueError:
            historico_aux = historico_aux + "Error\n"
        historico.insert('1.0', historico_aux)

receiver = Receiver()

# Classe interface Command, como nos slides
class Command:
    def execute(self):
        # TODO: aicionar uma lógica extra se necessário
        # Foi considerado que essa classe é puramente abstrata
        pass

# Classes filhas de Command. Note que elas reutilizam operações comunns do Receiver!
class VerficarSaldo (Command):
    def __init__(self, acao):
        super().__init__()
        self.receiver = receiver
        self.acao = acao

    def execute(self):
        super().execute()
        receiver.descrever_acao(self.acao)
        receiver.inserir_valor(saldo)

class Verficardivida (Command):
    def __init__(self, acao):
        super().__init__()
        self.receiver = receiver
        self.acao = acao

    def execute(self):
        super().execute()
        receiver.descrever_acao(self.acao)
        receiver.inserir_valor(divida)

class Tranferencia (Command):
    def __init__(self, acao):
        super().__init__()
        self.receiver = receiver
        self.acao = acao

    def execute(self):
        super().execute()
        self.valor = valor_transf.get()
        receiver.descrever_acao(self.acao)
        receiver.reduzir_saldo(self.valor)

# O cliente define os commandos de acordo com a GUI.
# Nesse caso, a classe Button funciona como Invoker!!!
but_saldo = Button(tela, text="Verificar Saldo", command=VerficarSaldo("Verificar Saldo:").execute)
but_divida = Button(tela, text="Verificar Dívida", command=Verficardivida("Verificar Dívida:").execute)
but_transf = Button(tela, text="Transferir para Fultano", command=Tranferencia("Transferir para Fultano:").execute)

# Criação da GUI
descricao.place(x=150,y=250)
saida.place(x=150,y=300)
historico_nome.place(x=520, y=240, width=55)
historico_nome.insert(END, "Histórico")
historico.place(x=400, y = 265, width=300, height=200)
valor_transf.place(x=555, y=190)
label1.place(x=210, y=25)
but_saldo.place(x=100, y=150)
but_saldo["font"] = Font(size=10)       
but_divida.place(x=350, y=150)
but_divida["font"] = Font(size=10)        
but_transf.place(x=550, y=150)
but_transf["font"] = Font(size=10)

# Loop da GUI
tela.mainloop()