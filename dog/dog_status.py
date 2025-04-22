def dog_status(dog):
    awake_status = "Sim" if dog.get_awake() else "Não"
    print(f"""  [STATUS DO CACHORRO]
        FOME: {dog.get_hunger()}
        SONO: {dog.get_sleep()}
        ESTÁ ACORDADO?: {awake_status}
    """)