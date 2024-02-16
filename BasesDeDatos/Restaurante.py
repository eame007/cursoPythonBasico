import sqlite3

def cread_db():
    conexion = sqlite3.connect("Restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute('''CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabal de categorias ya existe") 
    else:
        print("La tabla de categorias ha sido creada exitosamente")
    
    try:    
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabal de categorias ya existe") 
    else:
        print("La tabla de categorias ha sido creada exitosamente")
        
    conexion.close()

cread_db()