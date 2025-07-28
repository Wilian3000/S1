from flask import Flask, render_template

app = Flask(__name__)

# Datos del menú (pueden provenir de base de datos)
menu_items = [
    {"nombre": "Inicio",      "ruta": "/"},
    {"nombre": "Productos",   "ruta": "/productos"},
    {"nombre": "Servicios",   "ruta": "/servicios"},
    {"nombre": "Contacto",    "ruta": "/contacto"},
]

@app.route('/')
def index():
    return render_template('menu.html', items=menu_items, titulo="Mi Sitio Web")

@app.route('/productos')
def productos():
    return render_template('menu.html', items=menu_items, titulo="Productos")

@app.route('/servicios')
def servicios():
    return render_template('menu.html', items=menu_items, titulo="Servicios")

@app.route('/contacto')
def contacto():
    return render_template('menu.html', items=menu_items, titulo="Contacto")

if __name__ == '__main__':
    app.run(debug=True)
