from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("principal.html")

@app.route("/servicios")
def servicios():
    usuarios = [
        [1, "Revisión General", "Evaluación de dolores musculares", 100, 80],
        [2, "Maria Gomez", "Gomez", 2001, 2002],
        [3, "Carlos Ruiz", "Ruiz", 1998, 1999]]
    return render_template("servicios.html", usuarios=usuarios)

@app.route("/lista_citas")
def lista_citas():
    usuarios = [
        [1, "Brandom", "2025-11-02", "Revision General", "Alergico a la penicilina", 50, "Juan Perez"],
        [2, "Maria Gomez", 2001, "Samuel", "pan",  60, "Maria Gomez"],
        [3, "Carlos Ruiz", 1998, "Samuel", "lingo", 40, "Carlos Ruiz"]]
    return render_template("lista_citas.html", usuarios=usuarios)


@app.route("/editar_servicios/<int:id>")
def editar_servicios(id):
    usuario = [1, "Revisión General", "Evaluación de dolores dentales", 100, 80]
    return render_template("editar_servicios.html", usuario=usuario)

@app.route("/editar_citas/<int:id>")
def editar_cita(id):
    usuario = [1, "Juan Perez", "Evaluación de dolores dentales", 1999, 2000, "12894248", "Dr. Carlos Ruiz"]
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

@app.route("/doctores")
def doctores():
    return render_template("doctores.html", usuarios=[
        [1, "Dr. Juan Perez", "Cardiologia", "05/10/2020", "555-1234"],
        [2, "Dra. Maria Gomez", "Neurologia", "2018-03-22", "555-5678"],
        [3, "Dr. Carlos Ruiz", "Pediatria", "2019-11-15", "555-8765"]
    ])

@app.route("/registro_doctor")
def registro_doctor():
    return render_template("registor_doctor.html")

@app.route("/editar_doctor/<int:id>")
def editar_doctor(id):
    usuario = [1, "Dr. Juan Perez", "Cardiologia", "2020-05-10", "555-1234"]
    return render_template("editar_doctor.html", usuario=usuario)



if __name__ == "__main__":
    app.run(debug=True)
