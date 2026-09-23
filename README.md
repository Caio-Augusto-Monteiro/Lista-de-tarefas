# Lista de Tarefas

Um gerenciador de tarefas (to-do list) simples e funcional em Python.

## Funcionalidades

- ✓ Adicionar novas tarefas
- ✓ Listar todas as tarefas
- ✓ Marcar tarefas como concluídas
- ✓ Desmarcar tarefas
- ✓ Editar descrição de tarefas
- ✓ Deletar tarefas específicas
- ✓ Limpar todas as tarefas concluídas
- ✓ Salvar e carregar tarefas automaticamente em JSON

## Como usar

### Executar a aplicação

```bash
python lista.py
```

### Menu de opções

1. **Adicionar tarefa** - Cria uma nova tarefa
2. **Listar tarefas** - Exibe todas as tarefas com status
3. **Marcar como concluída** - Marca uma tarefa como feita
4. **Desmarcar** - Remove a marca de concluído
5. **Deletar tarefa** - Remove uma tarefa
6. **Editar tarefa** - Altera a descrição
7. **Limpar concluídas** - Remove todas as tarefas concluídas
8. **Sair** - Encerra a aplicação

## Arquivo de dados

As tarefas são salvas automaticamente em `tarefas.json` no mesmo diretório.

## Requisitos

- Python 3.6+

## Exemplo de uso

```
GERENCIADOR DE TAREFAS
============================================================
1. Adicionar tarefa
2. Listar tarefas
...

Escolha uma opção: 1
Digite a tarefa: Comprar leite
✓ Tarefa adicionada: Comprar leite

Escolha uma opção: 2

============================================================
LISTA DE TAREFAS
============================================================
○ [1] Comprar leite
   Criada em: 12/06/2026 14:30:45
============================================================
```

## Autor

Desenvolvido com Python 🐍
