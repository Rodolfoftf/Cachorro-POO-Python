from dog_status import dog_status

def chosen_menu(dog):
    while True:
        print("""
            MENU DE ESCOLHAS:
            1- Acordar o cão.
            2- Mandar o cão ir dormir.
            3- Alimentar o cão.
            4- Brincar com o cão.
            5- Sair.
        """)

        chosen_option = int(input('Digite a opção desejada: '))
        match chosen_option:
            case 1:
                dog.to_wake_up()
                dog_status(dog)
            case 2:
                dog.to_sleep()
                dog_status(dog)
            case 3:
                dog.to_feed()
                dog_status(dog)
            case 4:
                dog.to_play()
                dog_status(dog)
            case 5:
                print('Obrigado por lembrar de mim, lambeijos, até a próxima.')
                break
            case _:
                print('Digite uma opção válida.')
