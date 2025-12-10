from dataclasses import dataclass
from datetime import time

@dataclass
class Connessione:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int
    distanza : float
    difficolta : str
    durata : time
    anno : int

    def __eq__(self, other):
        return isinstance(other, Connessione) and self.id == other.id

    def __str__(self):
        return f"{self.id} ({self.id_rifugio1}) --> ({self.id_rifugio2})"

    def __repr__(self):
        return f"{self.id} ({self.id_rifugio1}) --> ({self.id_rifugio2})"

    def __hash__(self):
        return hash(self.id)