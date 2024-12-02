from estoque.estoque import Estoque
from estoque.fornecedor import Fornecedor
from pacientes.paciente import Paciente
from pacientes.consulta import Consulta

def main():
    print("Bem-vindo ao sistema de gerenciamento de consultório!")

    # Gerenciamento de pacientes
    paciente = Paciente(1, "João Silva", "12345678901", "987654321", "joao@email.com")
    consulta = Consulta(1, "2024-12-05 09:00", "Limpeza")

    paciente.agendar_consulta(consulta)
    print("Consulta agendada com sucesso!")
    historico = paciente.consultar_historico()
    print(f"Histórico de consultas do paciente {paciente.nome}:")
    for c in historico:
        print(f"- {c.tipoProcedimento} em {c.dataHora}")

    # Gerenciamento de estoque
    fornecedor = Fornecedor(1, "Fornecedor A", "123456789", "fornecedor@a.com")
    estoque = Estoque(1, "Cimento", fornecedor, "Cimento odontológico")

    estoque.adicionar_produto(fornecedor, "Cimento", 100)
    print("Produto adicionado ao estoque!")
    produtos = estoque.consultar_produtos()
    print("Produtos no estoque:")
    for produto in produtos:
        print(f"- {produto}")

if __name__ == "__main__":
    main()
