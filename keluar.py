import db
import uuid
import datetime

def id():
    # Generate a shorter UUID
    random_id = str(uuid.uuid4())[:8]
    return random_id

def keluar(npm):
    cursor = db.cursor
    cursor.execute("USE sistem_parkir;")

    sql_query = "INSET INTO keluar (id_keluar, tanggal_keluar, jam_keluar, id_gambar)"
    cursor.execute(sql_query, (npm))
    id_parkir = cursor.fetchone()[0]
    print(id_parkir)
    
keluar(["237006062"])