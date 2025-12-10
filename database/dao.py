from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_all_rifugi():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Rifugio"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            rif = Rifugio(row["id"],
                          row["nome"],
                          row["localita"],
                          row["altitudine"],
                          row["capienza"])
            result.append(rif)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_all_connessioni():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM Connessione"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            con = Connessione(row["id"],
                              row["id_rifugio1"],
                              row["id_rifugio2"],
                              row["distanza"],
                              row["difficolta"],
                              row["durata"],
                              row["anno"])
            result.append(con)
        cursor.close()
        cnx.close()
        return result