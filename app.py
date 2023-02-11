from flask import Flask, render_template, request, redirect, url_for
from data.telefonos_dao import TelefonosDao
from data.marcas_dao import MarcasDao
from data.models.Telefono import Telefono
from data.models.Marca import Marca
from database import db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/telefonos')
def telefono_route():
    telefonos_dao : TelefonosDao = TelefonosDao(db)
    return render_template('telefonos.html', telefono_grupo=telefonos_dao.get_all())


@app.route('/marcas')
def marca_route():
    marcas_dao : MarcasDao = MarcasDao(db)
    return render_template('marcas.html', marca_grupo=marcas_dao.get_all())


@app.route('/añadirtelefonos', methods=['POST'])
def añadir_telefono():   
    if request.method == 'POST':
        id_telefonos = request.form['id_telefonos']
        modelos = request.form['modelos']
        precio = request.form['precio']
        marca = request.form['marca']
        
        telefono_tabla = Telefono(id_telefonos,modelos,precio,marca)
        telefonos_dao : TelefonosDao = TelefonosDao(db)
        telefonos_dao.AñadirTelefonos(telefono_tabla)
        return redirect(url_for('telefono_route'))


@app.route('/añadirmarcas', methods=['POST'])
def añadir_marca():
    if request.method == 'POST':
        id_marca = request.form['id_marca']
        nombre_marca = request.form['nombre_marca']
        fecha_lanzamiento = request.form['fecha_lanzamiento']
        

        marca_tabla = Marca(id_marca,nombre_marca,fecha_lanzamiento)
        marcas_dao : MarcasDao = MarcasDao(db)
        marcas_dao.AñadirMarcas(marca_tabla)
        return redirect(url_for('marca_route'))


@app.route('/borrartelefonos/<string:id_telefonos>')
def borrar_telefonos(id_telefonos):
    telefonos_dao : TelefonosDao = TelefonosDao(db)
    telefonos_dao.BorrarTelefonos(id_telefonos)
    return redirect(url_for('telefono_route'))


@app.route('/borrarmarcas/<string:id_marca>')
def borrar_marcas(id_marca):
    marcas_dao : MarcasDao = MarcasDao(db)
    marcas_dao.BorrarMarcas(id_marca)
    return redirect(url_for('marca_route'))


if __name__ == '__main__':
    app.run(debug=True,port=5000)