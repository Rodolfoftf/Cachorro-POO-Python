from dog_class import Dog
def start_dog():
    dog_name = input('Digite o nome do cachorro: ')
    dog_breed = input('Diga a raça do seu cachorro: ')

    return Dog(dog_name, dog_breed)
