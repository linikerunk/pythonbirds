class Pessoa:

    def __init__(self, nome = None, idade=35):
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa("Luciano")
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome = "Liniker"
    print(p.nome)
    print(p.idade)