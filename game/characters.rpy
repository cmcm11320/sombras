init python:

    class Personas:
        def __init__(self, name = "Bloqueado", sobrenome = "???", relation = "???" , bloodType = "???", major = "???", history= "???", affection = 0, imageName = "normal"):
            self.name = name
            self.sobrenome = sobrenome
            self.relation = relation
            self.bloodType = bloodType
            self.major = major
            self.history = history
            ## Todos iniciam com 0 e tem max 10
            self.affection = affection
            #Localização das pastas de imagem
            self.imageName = "images/Characters/" + name +"/" + imageName + ".png"

## We're setting the name, bloodType, major, affection, and imageName.
default main_1 = Personas(name="You",affection=10,imageName = "main")

default alice_1 = Personas()

default pedro_1 = Personas()
default anna_1 = Personas()
default miguel_1 = Personas()
default isabella_1 = Personas()
default mauricio_1 = Personas()
default lucas_1 = Personas()
default luiz_1 = Personas()


## Primeiro a mostrar no status
default selectedCharacter = main_1