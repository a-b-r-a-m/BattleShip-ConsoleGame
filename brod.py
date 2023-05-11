class Brod:
    def __init__(self, _klasa: str, _velicina: int):
        self._klasa = _klasa
        self._velicina = _velicina
        self._koordinate = []

    @property
    def klasa(self):
        return self._klasa

    @property
    def velicina(self):
        return self._velicina

    @property
    def koordinate(self):
        return self._koordinate

    @koordinate.setter
    def koordinate(self, koord: tuple):
        self._koordinate.append(koord)
