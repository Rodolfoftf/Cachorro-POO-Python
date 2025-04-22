class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.hunger = 0
        self.sleep = 0
        self.is_awake = False  # Cão começa dormindo
        print(f'O cachorro {self.name} da raça {self.breed} foi criado e está dormindo.')

    def to_wake_up(self):
        if not self.is_awake:
            self.is_awake = True
            print(f'O cachorro {self.name} da raça {self.breed} acordou!')
        else:
            print(f'O cachorro {self.name} já está acordado.')

    def to_sleep(self):
        if self.is_awake:
            self.is_awake = False
            self.sleep = 0  # Ao dormir, o contador de cansaço zera
            print(f'O cachorro {self.name} da raça {self.breed} foi dormir! [Cansaço zerado]')
        else:
            print(f'O cachorro {self.name} já está dormindo.')

    def to_feed(self):
        self.hunger = 0  # Fome volta a zero ao alimentar o cão
        print(f'Você alimentou o {self.name} da raça {self.breed}. [Fome zerada]')

    def to_play(self):
        if not self.is_awake:
            print(f'O cachorro {self.name} está dormindo e não pode brincar agora!')
            return

        self.hunger += 1
        self.sleep += 1
        print(f'O cachorro {self.name} da raça {self.breed} brincou! [Fome: {self.hunger}, Cansaço: {self.sleep}]')

        # Verificar condição de morte por fome
        if self.hunger >= 6:
            print(f'O cachorro {self.name} da raça {self.breed} morreu de fome. ☠️')
            exit()  # Encerra o programa
        elif self.hunger == 5:
            print("⚠️ Atenção! O cão está prestes a morrer de fome! ⚠️")

        # Verificar condição de cansaço para dormir automaticamente
        if self.sleep >= 5:
            print(f'O cachorro {self.name} está muito cansado e vai dormir automaticamente. 💤')
            self.to_sleep()

    def get_sleep(self):
        return self.sleep

    def get_awake(self):
        return self.is_awake

    def get_hunger(self):
        return self.hunger
