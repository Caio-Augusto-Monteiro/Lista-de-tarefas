import json
import os
from datetime import datetime


class ToDoList:
    def __init__(self, filename="tarefas.json"):
        self.filename = filename
        self.tarefas = []
        self.carregar()

    def carregar(self):
        """Carrega as tarefas do arquivo."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    self.tarefas = json.load(f)
            except json.JSONDecodeError:
                self.tarefas = []
        else:
            self.tarefas = []

    def salvar(self):
        """Salva as tarefas no arquivo."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tarefas, f, ensure_ascii=False, indent=2)

    def adicionar(self, descricao):
        """Adiciona uma nova tarefa."""
        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "concluida": False,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }
        self.tarefas.append(tarefa)
        self.salvar()
        print(f"✓ Tarefa adicionada: {descricao}")

    def listar(self):
        """Lista todas as tarefas."""
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\n" + "=" * 60)
        print("LISTA DE TAREFAS")
        print("=" * 60)
        for tarefa in self.tarefas:
            status = "✓" if tarefa["concluida"] else "○"
            descricao = (
                f"~{tarefa['descricao']}~"
                if tarefa["concluida"]
                else tarefa["descricao"]
            )
            print(f"{status} [{tarefa['id']}] {descricao}")
            print(f"   Criada em: {tarefa['data_criacao']}")
        print("=" * 60 + "\n")

    def marcar_concluida(self, id_tarefa):
        """Marca uma tarefa como concluída."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                self.salvar()
                print(f"✓ Tarefa {id_tarefa} marcada como concluída!")
                return
        print(f"✗ Tarefa {id_tarefa} não encontrada.")

    def desmarcar_concluida(self, id_tarefa):
        """Desmarca uma tarefa concluída."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = False
                self.salvar()
                print(f"✓ Tarefa {id_tarefa} marcada como não concluída!")
                return
        print(f"✗ Tarefa {id_tarefa} não encontrada.")

    def deletar(self, id_tarefa):
        """Deleta uma tarefa."""
        self.tarefas = [t for t in self.tarefas if t["id"] != id_tarefa]
        self.salvar()
        print(f"✓ Tarefa {id_tarefa} deletada!")

    def limpar_concluidas(self):
        """Remove todas as tarefas concluídas."""
        tamanho_anterior = len(self.tarefas)
        self.tarefas = [t for t in self.tarefas if not t["concluida"]]
        removidas = tamanho_anterior - len(self.tarefas)
        self.salvar()
        print(f"✓ {removidas} tarefa(s) concluída(s) removida(s)!")

    def editar(self, id_tarefa, nova_descricao):
        """Edita a descrição de uma tarefa."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["descricao"] = nova_descricao
                self.salvar()
                print(f"✓ Tarefa {id_tarefa} editada!")
                return
        print(f"✗ Tarefa {id_tarefa} não encontrada.")


def menu():
    """Menu principal da aplicação."""
    lista = ToDoList()

    while True:
        print("\n" + "=" * 60)
        print("GERENCIADOR DE TAREFAS")
        print("=" * 60)
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Desmarcar tarefa")
        print("5. Deletar tarefa")
        print("6. Editar tarefa")
        print("7. Limpar tarefas concluídas")
        print("0. Sair")
        print("=" * 60)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Digite a tarefa: ").strip()
            if descricao:
                lista.adicionar(descricao)
            else:
                print("✗ Tarefa não pode estar vazia!")

        elif opcao == "2":
            lista.listar()

        elif opcao == "3":
            lista.listar()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a marcar como concluída: "))
                lista.marcar_concluida(id_tarefa)
            except ValueError:
                print("✗ ID inválido!")

        elif opcao == "4":
            lista.listar()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a desmarcar: "))
                lista.desmarcar_concluida(id_tarefa)
            except ValueError:
                print("✗ ID inválido!")

        elif opcao == "5":
            lista.listar()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a deletar: "))
                lista.deletar(id_tarefa)
            except ValueError:
                print("✗ ID inválido!")

        elif opcao == "6":
            lista.listar()
            try:
                id_tarefa = int(input("Digite o ID da tarefa a editar: "))
                nova_descricao = input("Digite a nova descrição: ").strip()
                if nova_descricao:
                    lista.editar(id_tarefa, nova_descricao)
                else:
                    print("✗ Descrição não pode estar vazia!")
            except ValueError:
                print("✗ ID inválido!")

        elif opcao == "7":
            lista.limpar_concluidas()

        elif opcao == "0":
            print("✓ Até logo!")
            break

        else:
            print("✗ Opção inválida!")


if __name__ == "__main__":
    menu()
