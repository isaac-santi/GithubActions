from data.models.Telefono import Telefono

class TelefonosDao():
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT * FROM telefono')
        data=cursor.fetchall()
        telefonos_lista = []

        for telefonos in data:
            telefonos_lista.append(Telefono(telefonos[0],telefonos[1],telefonos[2],telefonos[3]))
        
        return telefonos_lista

    def AñadirTelefonos(self,telefono):
            cursor=self.db.cursor()
            cursor.execute('INSERT INTO telefono (id_telefonos,modelos,precio,marca) VALUES (%s,%s,%s,%s)',(telefono.id_telefonos,telefono.modelos,telefono.precio,telefono.marca))
            self.db.commit()

    def BorrarTelefonos(self,id_telefonos):
            cursor=self.db.cursor()
            cursor.execute('DELETE FROM telefono WHERE id_telefonos=%s',(id_telefonos,))
            self.db.commit()
