from flask import Flask, render_template, request, redirect, url_for

from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb://localhost:27017/")  
db = client["mi_clinica"] 
servicios_col = db["servicios"]
citas_col = db["citas"]
doctores_col = db["doctores"]



app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("principal.html")

@app.route("/servicios")
def servicios():
    usuarios = list(servicios_col.find())
    return render_template("servicios.html", usuarios=usuarios)



@app.route("/lista_citas")
def lista_citas():
    usuarios = list(citas_col.find())
    return render_template("lista_citas.html", usuarios=usuarios)





@app.route("/editar_servicios/<id>")
def editar_servicios(id):
    usuario = servicios_col.find_one({"_id": ObjectId(id)})
    return render_template("editar_servicios.html", usuario=usuario)

@app.route("/actualizar_servicio", methods=["POST"])
def actualizar_servicio():
    try:
        id = request.form["id"]
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        costo = request.form["costo"]
        duracion = request.form["duracion"]

        servicios_col.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "costo": int(costo),
                    "duracion": int(duracion)
                }
            }
        )

        return redirect(url_for("servicios"))

    except Exception as e:
        return f"Error al actualizar: {e}"


@app.route("/editar_cita/<id>")
def editar_cita(id):
    usuario = citas_col.find_one({"_id": ObjectId(id)})
    lista_doctores = doctores_col.distinct("nombre")
    lista_servicios = servicios_col.distinct("nombre")
    return render_template("editar_citas.html", usuario=usuario, ld = lista_doctores , ls =lista_servicios )



@app.route("/actualizar_cita", methods=["POST"])
def actualizar_cita():
    try:
        id = request.form["id"]
        nombre_servicio = request.form["servicio"]
        nombre_doctor = request.form["doctor"]
        servicio_doc = servicios_col.find_one({"nombre": nombre_servicio})
        doctor_doc = doctores_col.find_one({"nombre": nombre_doctor})
        citas_col.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "paciente": request.form["paciente"],
                    "fecha": request.form["fecha"],
                    "servicio_id": servicio_doc["_id"],
                    "servicio": {
                        "nombre": servicio_doc["nombre"],
                        "descripcion": servicio_doc.get("descripcion", ""),
                        "costo": servicio_doc.get("costo", 0),
                        "duracion": servicio_doc.get("duracion", "")
                    },
                    "comentario": request.form["comentario"],
                    "costo": request.form["costo"],
                    "doctor_id": doctor_doc["_id"],
                    "doctor": {
                        "_id": doctor_doc["_id"],
                        "nombre": doctor_doc["nombre"],
                        "especialidad": doctor_doc.get("especialidad", ""),
                        "fecha_ingreso": doctor_doc.get("fecha_ingreso", ""),
                        "telefono": doctor_doc.get("telefono", "")
                        }
                    }})
        return redirect("/lista_citas")

    except Exception as e:
        return f"Error al actualizar cita: {e}"



@app.route("/registro_serv")
def registro_serv():
    return render_template("registro_serv.html")

@app.route("/guardar_servicio", methods=["POST"])
def guardar_servicio():
    try:
        servicios_col.insert_one({
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "costo": request.form["costo"],
            "duracion": request.form["duracion"]
        })
        return redirect("/servicios")

    except Exception as e:
        return f"Error al guardar servicio: {e}"

@app.route('/registrocita')
def registrocita():
    lista_doctores = doctores_col.distinct("nombre")
    lista_servicios = servicios_col.distinct("nombre")
    return render_template("registro_cita.html", ld = lista_doctores , ls =lista_servicios )

@app.route("/guardar_cita", methods=["POST"])
def guardar_cita():
    try:
        
        nombre_servicio = request.form["servicio"]
        nombre_doctor = request.form["doctor"]
        servicio_doc = servicios_col.find_one({"nombre": nombre_servicio})
        doctor_doc = doctores_col.find_one({"nombre": nombre_doctor})

        citas_col.insert_one({
            "paciente": request.form["paciente"],
            "fecha": request.form["fecha"],
            "servicio_id": servicio_doc["_id"],
            "servicio": {
                "nombre": servicio_doc["nombre"],
                "descripcion": servicio_doc.get("descripcion", ""),
                "costo": servicio_doc.get("costo", 0),
                "duracion": servicio_doc.get("duracion", "")
            },
            "comentario": request.form["comentario"],
            "costo": request.form["costo"],
            "doctor_id": doctor_doc["_id"],
            "doctor": {
                "nombre": doctor_doc["nombre"],
                "especialidad": doctor_doc.get("especialidad", ""),
                "fecha_ingreso": doctor_doc.get("fecha_ingreso", ""),
                "telefono": doctor_doc.get("telefono", "")
            }
        })
        return redirect("/lista_citas")

    except Exception as e:
        return f"Error al guardar cita: {e}"



@app.route("/doctores")
def doctores():
    usuarios = list(doctores_col.find())
    return render_template("doctores.html", usuarios=usuarios)

@app.route("/registro_doctor")
def registro_doctor():
    return render_template("registro_doctor.html")

@app.route("/guardar_doctor", methods=["POST"])
def guardar_doctor():
    try:
        doctores_col.insert_one({
            "nombre": request.form["nombre"],
            "especialidad": request.form["especialidad"],
            "fecha_ingreso": request.form["fecha_ingreso"],
            "telefono": request.form["telefono"]
        })
        return redirect("/doctores")

    except Exception as e:
        return f"Error al guardar doctor: {e}"


@app.route("/editar_doctor/<id>")
def editar_doctor(id):
    usuario = doctores_col.find_one({"_id": ObjectId(id)})
    return render_template("editar_doctor.html", usuario=usuario)

@app.route("/actualizar_doctor", methods=["POST"])
def actualizar_doctor():
    try:
        id = request.form["id"]

        doctores_col.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "nombre": request.form["nombre"],
                    "especialidad": request.form["especialidad"],
                    "fecha_ingreso": request.form["fecha_ingreso"],
                    "telefono": request.form["telefono"],
                }
            }
        )
        return redirect("/doctores")

    except Exception as e:
        return f"Error al actualizar doctor: {e}"



@app.route("/eliminar_servicio/<id>")
def eliminar_servicio(id):
    servicios_col.delete_one({"_id": ObjectId(id)})
    return redirect("/servicios")

@app.route("/eliminar_cita/<id>")
def eliminar_cita(id):
    citas_col.delete_one({"_id": ObjectId(id)})
    return redirect("/lista_citas")

@app.route("/eliminar_doctor/<id>")
def eliminar_doctor(id):
    doctores_col.delete_one({"_id": ObjectId(id)})
    return redirect("/doctores")





if __name__ == "__main__":
    app.run(debug=True)
