class Paciente:
    def __init__(self, id, nome, cpf, telefone, email):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.historico_consultas = []

    def agendar_consulta(self, consulta):
        """Adiciona uma consulta ao histórico do paciente."""
        self.historico_consultas.append(consulta)

    def consultar_historico(self):
        """Retorna o histórico de consultas do paciente."""
        return self.historico_consultas

    def enviarLembrete(self, consulta_id):
        """Envia um lembrete sobre a consulta com base no ID."""
        consulta = next((c for c in self.historico_consultas if c.id == consulta_id), None)
        if consulta:
            return f"Lembrete: Consulta de {self.nome} agendada para {consulta.dataHora}."
        return "Consulta não encontrada."