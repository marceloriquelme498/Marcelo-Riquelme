from flask import Flask, render_template 
app = Flask(__name__) 
 
@app.route("/") 
def dashboard(): 
    datos = {"usuarios": 120, "ventas": 4520, "visitas": 3080} 
    return render_template("dashboard.html", datos=datos) 
 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True) 
