class OrganizadorFila:
    def __init__(self):
        self.fila= {}
        self.prox_ticket= 1
        self.ticket_atendido= {}

    def add_cliente(self, cliente):
        ticket = len(self.fila) + 1
        self.fila.update({ticket:cliente})

    def chamar_cliente(self):
        if self.fila:
            prox_ticket = min(self.fila.keys())
            cliente = self.fila[prox_ticket]
            print(f"Próximo atendimento: {prox_ticket}: {cliente}")
            self.ticket_atendido[prox_ticket] = cliente
            del self.fila[prox_ticket]
        else:
            print(f"A fila está vazia!")

    def deletar_cliente(self):
        if self.fila:
            cliente=self.fila[self.prox_ticket]
            del self.fila[self.prox_ticket]
            print(f'Próximo atendimento: {cliente} Ticket: {self.prox_ticket}.')
            self.prox_ticket+=1
        else:
            print(f"A fila está vazia!")


    def ver_fila(self):
        if self.fila:
            fila_str = "Fila atual:\n"
            for ticket, cliente in self.fila.items():
                fila_str += f"Ticket {ticket}: {cliente}\n"
            print(fila_str)
        else:
            print("A fila está vazia.")

    def tempo_espera(self):
        if self.fila:
            tempo_por_cliente = 5
            tempo_total = len(self.fila) * tempo_por_cliente
            print(f"Tempo aproximado de espera: {tempo_total} minutos.")
        else:
            print("A fila está vazia, não há tempo de espera.")


def main():
    organizador = OrganizadorFila()

    while True:
        print("\nOptions:")
        print("1. Add cliente a fila")
        print("2. Ver fila")
        print("3. Chamar ticket")
        print("4. Excluir ticket")
        print("5. Tempo de espera")
        print("6. Sair")
        choice = input("Digite um número dentre as opções: ")

        if choice == "1":
            client_name = input("Qual o nome do cliente: ")
            organizador.add_cliente(client_name)
        elif choice == "2":
            organizador.ver_fila()
        elif choice == "3":
            organizador.chamar_cliente()
        elif choice == "4":
            organizador.deletar_cliente()
        elif choice == "5":
            organizador.tempo_espera()
        elif choice == "6":
            print("Saindo.")
            break
        else:
            print("Número inválido. Por favor selecione novamente.")

if __name__ == "__main__":
    main()