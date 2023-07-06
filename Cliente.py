class Cliente:
    Rut = 0
    Nombre = ''
    Apellido = ''
    Num_asiento = 0
    Valor = 0

    def __init__(self):
        self.Rut = 11111111
        self.Nombre = 'S/N'
        self.Apellido = 'S/A'
        self.Num_asiento = 1
        self.Valor = 120000

    def setRut(self, r):
        if len(r) == 8 or len(r) == 7:
            self.Rut = r
            return True
        else:
            print("EL rut no es valido (7 - 8 Caracteres)")
            return False