# Variáveis globais auxiliares
is_admin = False # User ou Admin, determina permissões
ans = 0 # Controla o temmpo de expiração do documento

# Interface para a máquina de estados que representa um estado. Classe abstrata
class State:    
    def __init__(self):
        self.name = ""

    def render(self): # Renderizar documento
        print("Checando permissões...\n")
    
    def publish(self): # Publicar documento
        print("Checando permissões...\n")

# Classe Context
class Document:
    def render(self):
        self.state.render()
    
    def publish(self):
        self.state.publish()
    
    def changeState(self, state : State):
        self.state = state

# Estados são descritos nas classes abaixo!
class Draft (State):
    def __init__(self, document : Document()):
        super().__init__()
        self.document = document
        self.name = "em Rascunho"

    def render(self):
        global is_admin
        super().render()
        if is_admin == True:
            print("Documento renderizado!\n")
        else:
            print("Perdão, essa opção só está disponível para administradores.\n")
    
    def publish(self):
        global is_admin
        super().publish()
        if is_admin == True:
            self.document.changeState(Published(document))
        else:
            self.document.changeState(Moderation(document)) 

class Moderation (State):
    def __init__(self, document : Document):
        super().__init__()
        self.document = document
        self.name = "sob Revisão"

    def render(self):
        global is_admin
        super().render()
        if is_admin == True:
            print("Documento renderizado!\n")
        else:
            print("Perdão, essa opção só está disponível para administradores.\n")
    
    def publish(self):
        global is_admin
        super().publish()
        if is_admin == True:
            accept = input("Aceitar documento? S/N ")
            if accept == "S":
                self.document.changeState(Published(document))
            elif accept == "N":
                self.document.changeState(Draft(document))
            else:
                print("Entrada inválida, saindo do serviço.\n")
                
        else:
            print("Perdão, essa opção só está disponível para administradores.\n")

class Published (State):
    def __init__(self, document : Document):
        super().__init__()
        self.document = document
        self.name = "Publicado"

    def render(self):
        global is_admin
        super().render()
        if is_admin == True:
            print("Documento renderizado!\n")
        else:
            print("Perdão, essa opção só está disponível para administradores.\n")
    
    def publish(self):
        global is_admin
        global ans
        super().publish()
        if ans > 1: # Se tiver passado 1 loop, reseta.
            print("Tempo de expiração alcançado.\n")
            self.document.changeState(Draft(document))
        else:
            if is_admin == True:
                print("Documento já publicado, tempo de expiração próximo de acabar.\n")
            else:
                print("Documento já publicado.\n")

# Definição do documento que será manipulado
document = Document()
document.changeState(Draft(document))

# Main Loop
while (True):
    ans += 1
    # Apenas para testes, deveria existir um sistema de segurança mais seguro aqui!
    user_type = input("Digite \"user\" caso seja um cliente ou \"admin\" caso seja um administrador: ")
    run = False
    if user_type == "user":
        is_admin = False
        run = True
    elif user_type == "admin":
        is_admin = True
        run = True
    else:
        print("Entrada inválida")
    # Loop de execução bem simplificado por conta da implementação com State.
    # Basta chamar a função que se deseja.
    if run == True:
        print("Digite a ação que deseja tomar:\n")
        option = input("1 - Exibir documento, 2 - Publicar Documento: ")
        if option == "1":
            document.render()
        elif option == "2":
            document.publish()
            print("Documento " + document.state.name)