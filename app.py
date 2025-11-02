from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("principal.html")

@app.route("/servicios")
def servicios():
    usuarios = [
        [1, "Juan Perez", "Perez", 1999, 2000],
        [2, "Maria Gomez", "Gomez", 2001, 2002],
        [3, "Carlos Ruiz", "Ruiz", 1998, 1999]]
    return render_template("servicios.html", usuarios=usuarios)

@app.route("/lista_citas")
def lista_citas():
    usuarios = [
        [1, "Juan Perez", 1999, "Samuel", "revision", "aceptad"],
        [2, "Maria Gomez", 2001, "Samuel", "pan", "terminada"],
        [3, "Carlos Ruiz", 1998, "Samuel", "lingo", "en proceso"]]
    return render_template("lista_citas.html", usuarios=usuarios)


@app.route("/editar_servicios/<int:id>")
def editar_servicios(id):
    usuario = [1, "Juan Perez", "Perez", 1999, 2000, "12894248", "Xela"]
    return render_template("editar_servicios.html", usuario=usuario)

@app.route("/editar_citas/<int:id>")
def editar_cita(id):
    usuario = [1, "Juan Perez", "Perez", 1999, 2000, "12894248"]
    return render_template("editar_citas.html", usuario=usuario)

@app.route("/registro_serv")
def registro_serv():
    return render_template("registro_serv.html")

@app.route('/registrocita')
def registrocita():
    return render_template("registro_cita.html")

@app.route("/eliminar_usuario")
def eliminar_usuario():
    return "Usuario eliminado"



if __name__ == "__main__":
    app.run(debug=True)
