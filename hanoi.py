def mover_discos(discos, torre_origem, torre_destino, torre_auxiliar):
    if discos == 1:
        print(f'Mover {discos} da {torre_origem} para {torre_destino}')
    else:
        mover_discos(discos - 1, torre_origem, torre_auxiliar, torre_destino)
        print(f'Mover {discos} da {torre_origem} para {torre_destino}')
        mover_discos(discos - 1, torre_auxiliar, torre_destino, torre_origem)

mover_discos(3, 'Torre 1', 'Torre 3', 'Torre 2')