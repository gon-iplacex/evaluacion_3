from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index.html")

#ejercicio 1
@app.route("/ejercicio1",methods =["GET","POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nota1 = float(request.form.get("nota1"))
        nota2 = float(request.form.get("nota2"))
        nota3 = float(request.form.get("nota3"))
        asistencia = int(request.form.get("asistencia"))
        promedio_notas = round((nota1+nota2+nota3)/3)
        estado = (
            "aprobado" 
            if (promedio_notas>=40 and asistencia >=75)
            else "reprobado"
    )
        resultado = {
            "promedio":promedio_notas,
            "asistencia":asistencia,
            "estado":estado

    }
    return render_template("ejercicio1.html",resultado=resultado)
#ejercicio 2
@app.route("/ejercicio2",methods = ["GET","POST"])
def ejercicio2():
    resultado = None
    if request.method =="POST":
        nombre1=request.form.get("nombre1")
        nombre2=request.form.get("nombre2")
        nombre3=request.form.get("nombre3")
        nombres = [nombre1,nombre2,nombre3]
        nombre_largo = max (nombres, key = len)
        cantidad = len(nombre_largo)
        resultado = {
            "nombre": nombre_largo,
            "cantidad": cantidad
    }
    return render_template("ejercicio2.html",resultado=resultado)
if __name__ == "__main__":
    app.run(debug=True)