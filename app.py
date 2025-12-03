from flask import Flask, render_template, request, flash, redirect 
from db_connection import get_db_connection 
from datetime import datetime 
import os 
 
app = Flask(__name__) 
app.secret_key = os.getenv("FLASK_SECRET", "cambiame_por_una_mas_segura") 
 
lotes = [ 
    {"tipo": "Ternero/a", "desc": "Bovino joven, generalmente al pie de la madre", "cant": 120, "precio": 850000, "img": "product1.jpg"}, 
    {"tipo": "Novillito", "desc": "Macho castrado de destete hasta los 2 años", "cant": 85, "precio": 1350000, "img": "product2.jpg"}, 
    {"tipo": "Novillo", "desc": "Macho castrado de más de 2 años", "cant": 60, "precio": 2100000, "img": "product3.jpg"}, 
    {"tipo": "Vaquillona", "desc": "Hembra desde el destete hasta su primera cría", "cant": 95, "precio": 1950000, "img": "product4.jpg"}, 
    {"tipo": "Vaca", "desc": "Hembra adulta", "cant": 40, "precio": 2800000, "img": "product5.jpg"}, 
    {"tipo": "Toro", "desc": "Macho entero (no castrado)", "cant": 8, "precio": 5200000, "img": "product6.jpg"} 
] 
 
@app.route("/") 
def index(): 
    return render_template("index.html", lotes=lotes) 
 
@app.route("/contacto", methods=["GET","POST"]) 
def contacto(): 
    if request.method == "POST": 
        nombre = request.form.get("nombre","") 
        correo = request.form.get("correo","") 
        celular = request.form.get("celular","") 
        horario = request.form.get("horario","") 
        tipo = request.form.get("tipo_ganado","") 
 
        with get_db_connection() as conn: 
            if conn is None: 
                flash("Error: No se pudo conectar a la base de datos", "danger") 
            else: 
                try: 
                    cursor = conn.cursor() 
                    try: 
                        cursor.execute("INSERT INTO solicitudes (nombre_apellido, correo, celular, horario, tipo_ganado, fecha_solicitud) VALUES (%s,%s,%s,%s,%s,NOW())", (nombre,correo,celular,horario,tipo)) 
                        conn.commit() 
                    except Exception: 
                        cursor.execute("INSERT INTO solicitudes (nombre_apellido, correo, celular, horario, tipo_ganado, fecha_solicitud) VALUES (?,?,?,?,?,?)", (nombre,correo,celular,horario,tipo,datetime.now())) 
                        conn.commit() 
                    finally: 
                        cursor.close() 
                    flash("¡Solicitud enviada con éxito! Te contactaremos pronto.","success") 
                except Exception as e: 
                    flash(f"Error al guardar: {e}","danger") 
        return redirect("/contacto") 
 
    return render_template("contacto.html") 
 
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


