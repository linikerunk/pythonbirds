class Pessoa:

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    liniker = Pessoa(nome='Liniker')
    luciano = Pessoa(liniker, nome="Luciano")
    print(id(luciano))
    print(luciano.comprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Silva"
    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(liniker.__dict__)