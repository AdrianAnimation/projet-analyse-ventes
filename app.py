import sqlite3

conn = sqlite3.connect('ventes.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS produits (
        id_produit INTEGER PRIMARY KEY,
        nom TEXT NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS magasins (
        id_magasin INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        ville TEXT,
        region TEXT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS ventes (
        id_vente INTEGER PRIMARY KEY,
        id_produit INTEGER,
        id_magasin INTEGER,
        date TEXT,
        quantite INTEGER,
        prix REAL,
        FOREIGN KEY(id_produit) REFERENCES produits(id_produit),
        FOREIGN KEY(id_magasin) REFERENCES magasins(id_magasin)
    )
''')

conn.commit()
conn.close()


print("Base de datos y tablas creadas con éxito.")
