class Atividade:
  def __init__(self, nome, data):
      self.nome = nome
      self.data = data
      self.concluida = False

  def marcar_concluida(self):
      self.concluida = True

  def __str__(self):
      status = "Concluída" if self.concluida else "Em aberto"
      return f"{self.nome} - {self.data} - {status}"
