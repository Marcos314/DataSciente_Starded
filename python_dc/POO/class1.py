#criando a classe Livro

class Livro():

    #método responsável por inicializar cada obj criado a partir dessa classe
    def __init__(self):

        #atributos de cada obj criado a partir desta classe, o self é uma referencia a cada atributo criado na classe
        self.titulo = 'O monge executivo'
        self.isbn = 99888888
        print('Construtor chamado para criar um obj desta classe')

        #Pelo que entendi, toda vez q um obj for instanciado, ele vai ser criado já com titulo e isbn

    def imprimi(self):
        print('Foi criado o livro %s e ISBN %d '%(self.titulo, self.isbn))
        print('{} E {}'.format(self.titulo, self.isbn))

Livro1 = Livro()

Livro1.imprimi()






