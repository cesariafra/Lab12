import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self.G = nx.Graph()

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        self.G.clear()
        fattori_difficolta = {'facile' : 1, 'media' : 1.5, 'difficile' : 2}
        for el in DAO.get_all_connessioni():
            if el.anno <= year:
                result = []
                for r in DAO.get_all_rifugi():
                    if r.id == el.id_rifugio1 or r.id == el.id_rifugio2:
                        result.append(r)
                self.G.add_nodes_from(result)
                self.G.add_edge(result[0], result[1], peso = float(el.distanza)*(fattori_difficolta[el.difficolta]))

    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        lista_pesi = [weight for u, v, weight in self.G.edges(data='peso')]

        return min(lista_pesi), max(lista_pesi)

    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        minori = 0
        maggiori = 0

        for el in self.G.edges(data='peso'):
            if el[2] < soglia:
                minori += 1
            elif el[2] > soglia:
                maggiori += 1

        return minori, maggiori

    def cammino_minimo(self, soglia):
        peso_minimo = float('inf')
        percorso = None

        for node in self.G.nodes():
            vicini_validi = []
            for neighbor in self.G.neighbors(node):
                peso_arco = self.G[node][neighbor]['peso']
                if peso_arco > soglia:
                    vicini_validi.append((neighbor, peso_arco))

            if len(vicini_validi) < 2:
                continue

            vicini_validi.sort(key=lambda x: x[1])
            v1, peso1 = vicini_validi[0]
            v2, peso2 = vicini_validi[1]
            somma = peso1 + peso2

            if somma < peso_minimo:
                peso_minimo = somma
                arco1 = (v1, node, peso1)
                arco2 = (node, v2, peso2)
                percorso = (arco1, arco2)

        return percorso