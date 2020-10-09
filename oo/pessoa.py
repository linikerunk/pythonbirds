class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico(): # função atrelada a classe pessoa
        return 42

    @classmethod # ter acesso a classe que ta executando esse método
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    luciano.olhos = 1
    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(liniker.__dict__)
    print(luciano.olhos)
    print(liniker.olhos)
    print(id(Pessoa.olhos)), print(id(luciano.olhos)), print(id(liniker.olhos))
    print(Pessoa.metodo_estatico()), print(luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe()), 
    print(luciano.nome_e_atributos_de_classe())