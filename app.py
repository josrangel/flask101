from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/") #Raiz del sitio
def index(): #La funcion index indica que sera la funcion principal
    return render_template("index.html")

@app.route("/saludo") #Raiz del sitio
def saludo(): 
    return "Hola ;V"

@app.route("/saludo/<nombre>") #parametros por url
def saludoNombre(nombre): 
    return render_template("saludo.html", nombre=nombre) #Se el pasa al template el parametro

@app.route("/funcion",methods=['POST']) #peticion tipo POST
def funcionApi():
    funcion=request.form["funcion"]#Se accede al valor del form-data
    return render_template("funcion.html", funcion=funcion) #Se el pasa al template el parametro

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port =5000)#port =5000, #El modo debug sirve para que se actualizen los cambios sin tener que detener el server manualmente
    print("ESTOY VIVO!!!")
