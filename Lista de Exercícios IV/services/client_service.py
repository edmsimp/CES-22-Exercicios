from services.service import Service
from agents.client import Client

class ClientService (Service):

    def insert (self, client_data, name, email) :
        # add new client and stores it
        new_client = Client(name, email)
        new_client.past_orders = {}
        client_data.append(new_client)
        return new_client

    def modify(self, client_data, name):
        # search through the database with the author and title
        found = False
        for c in client_data:
            if name == c.name:
                found = True
                print("Client modified")  
                # TODO: add modify logic
                return c  
        if found == False:
            print("Client not found, exiting service")    

    def get(self, client_data, name):
        found = False
        for c in client_data:
            if name == c.name:
                found = True
                print("Client returned")  
                # TODO: add modify logic
                return c  
        if found == False:
            print("Client not found, exiting service")    

    def remove(self, client_data, name):
        found = False
        for c in client_data:
            if name == c.name:
                found = True
                print("Client removed")
                client_data.remove(c)
                return c
        if found == False:
            print("Client not, exiting service")
