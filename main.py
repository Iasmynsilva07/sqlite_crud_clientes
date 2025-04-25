from database import create_table
from operations import insert_customer, list_customers, get_customer_by_id, delete_customer

def menu():
    print("\n==== Sistema de Clientes ====")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente por ID")
    print("4 - Deletar cliente")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    create_table()

    while True:
        opcao = menu()

        if opcao == '1':
            name = input("Nome: ")
            weight = input("Peso: ")
            insert_customer(name, float(weight))
            print("Cliente adicionado com sucesso!")

        elif opcao == '2':
            clientes = list_customers()
            for c in clientes:
                print(f"ID: {c[0]} | Nome: {c[1]} | Peso: {c[2]}")

        elif opcao == '3':
            cid = input("ID do cliente: ")
            cliente = get_customer_by_id(int(cid))
            if cliente:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Peso: {cliente[2]}")
            else:
                print("Cliente não encontrado.")

        elif opcao == '4':
            cid = input("ID do cliente para deletar: ")
            delete_customer(int(cid))
            print("Cliente deletado com sucesso!")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == '__main__':
    main()
