from budget_manager import BudgetManager
from report_generator import ReportGenerator

manager = BudgetManager("data/transactions.json")
report = ReportGenerator("data/transactions.json")

def menu():
    print("\n=== SmartBudget ===")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Ver relatório")
    print("4. Gerar gráfico de gastos")
    print("5. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor da receita: "))
        categoria = input("Categoria: ")
        manager.add_transaction(valor, categoria, tipo="receita")

    elif opcao == "2":
        valor = float(input("Valor da despesa: "))
        categoria = input("Categoria: ")
        manager.add_transaction(valor, categoria, tipo="despesa")

    elif opcao == "3":
        report.show_summary()

    elif opcao == "4":
        report.plot_expenses_by_category()

    elif opcao == "5":
        print("Saindo... até mais!")
        break
