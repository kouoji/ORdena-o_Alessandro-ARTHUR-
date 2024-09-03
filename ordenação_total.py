#ordenação total

class alunos:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe

    def __repr__(self):
        return f"{self.nome} ({self.classe})"

def ordenacao_total(alunos):
    return sorted(alunos, key=lambda x: (x.classe, x.nome.casefold()))


alunos = [
    alunos("Josiel", "1º ano"),
    alunos("Massa", "2º ano"),
    alunos("Allan", "1º ano"),
    alunos("Ronaldo", "3º ano"),
    alunos("Kimi", "2º ano")
]

print(ordenacao_total(alunos))