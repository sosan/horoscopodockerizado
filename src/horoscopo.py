"""
    HOROSCOPOS
    ----------
"""


class HoroscopoChino():
    ANIMALES_HOROSCOPO_CHINO = [
        'mono', 'gallo', 'perro', 'cerdo', 'rata',
        'buey', 'tigre', 'conejo', 'dragon',
        'serpiente', 'caballo', 'cabra'
    ]

    def __init__(self, anyo_usuario):
        self.anyo_usuario = anyo_usuario

    def signo(self):
        try:
            for i in range(0, 12):
                if self.anyo_usuario % 12 == i:
                    return self.ANIMALES_HOROSCOPO_CHINO[i]

        except ValueError:
            return 'Error al introducir el año'
            signo()
