from data.models.Marca import Marca

class MarcasDao():
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT * FROM marca')
        data=cursor.fetchall()
        marcas_lista = []

        for marcas in data:
            marcas_lista.append(Marca(marcas[0],marcas[1],marcas[2]))
        
        return marcas_lista

    def AñadirMarcas(self,marca):
            cursor=self.db.cursor()
            cursor.execute('INSERT INTO marca (id_marca,nombre_marca,fecha_lanzamiento) VALUES (%s,%s,%s)',(marca.id_marca,marca.nombre_marca,marca.fecha_lanzamiento))
            self.db.commit()

    def BorrarMarcas(self,id_marca):
            cursor=self.db.cursor()
            cursor.execute('DELETE FROM marca WHERE id_marca=%s',(id_marca,))
            self.db.commit()
