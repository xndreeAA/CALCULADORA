from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    nombre = request.form["nombre"]
    numeros_str = request.form["numeros"]

    try:
        # Convertir a lista de números
        numeros = [float(x) for x in numeros_str.replace(",", " ").split()]
        
        media = statistics.mean(numeros)
        desviacion = statistics.pstdev(numeros)  # desviación estándar poblacional
    except Exception:
        return "Error: asegúrate de ingresar solo números separados por espacio o coma."

    return render_template("resultado.html", nombre=nombre, media=media, desviacion=desviacion)

if __name__ == "__main__":
    app.run(debug=True)
