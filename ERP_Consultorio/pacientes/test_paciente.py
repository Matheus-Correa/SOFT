import unittest
from datetime import datetime
from pacientes.paciente import Paciente
from pacientes.consulta import Consulta

class TestPaciente(unittest.TestCase):
    def setUp(self):
        """Configura os objetos para os testes."""
        self.paciente = Paciente(1, "João Silva", "12345678901", "987654321", "joao@email.com")
        self.consulta1 = Consulta(1, datetime(2024, 12, 5, 9, 0), "Limpeza")
        self.consulta2 = Consulta(2, datetime(2024, 12, 10, 14, 0), "Exame")

    def test_agendar_consulta(self):
        """Testa se uma consulta é agendada corretamente."""
        self.paciente.agendar_consulta(self.consulta1)
        historico = self.paciente.consultar_historico()
        self.assertEqual(len(historico), 1)
        self.assertEqual(historico[0], self.consulta1)

    def test_consultar_historico(self):
        """Testa se o histórico de consultas é retornado corretamente."""
        self.paciente.agendar_consulta(self.consulta1)
        self.paciente.agendar_consulta(self.consulta2)
        historico = self.paciente.consultar_historico()
        self.assertEqual(len(historico), 2)
        self.assertEqual(historico[0], self.consulta1)
        self.assertEqual(historico[1], self.consulta2)

    def test_consultar_historico_vazio(self):
        """Testa se o histórico de consultas vazio é retornado corretamente."""
        self.assertEqual(len(self.paciente.consultar_historico()), 0)

    def test_enviar_lembrete_sucesso(self):
        self.paciente.agendar_consulta(self.consulta1)
        lembrete = self.paciente.enviarLembrete(1)
        self.assertEqual(
            lembrete,
            "Lembrete: Consulta de João Silva agendada para 2024-12-05 09:00:00."
        )

    def test_enviar_lembrete_falha(self):
        lembrete = self.paciente.enviarLembrete(99)  # Consulta inexistente
        self.assertEqual(lembrete, "Consulta não encontrada.")


if __name__ == '__main__':
    unittest.main()
