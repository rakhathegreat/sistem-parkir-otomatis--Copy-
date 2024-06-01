import db
import uuid
import datetime

cursor = db.cursor
cursor.execute("USE sistem_parkir;")

def tanggal():
    return str(datetime.date.today())

def jam():
    return str(datetime.datetime.now().strftime("%H:%M:%S"))

def id():
    # Generate a shorter UUID
    random_id = str(uuid.uuid4())[:8]
    return random_id

def masuk(npm):
        id_gambar = id()
        insert_image(id_gambar, "image4.jpg")
        sql_query = "INSERT INTO masuk (id_masuk, tanggal_masuk, jam_masuk, id_gambar) VALUES (%s, %s, %s, %s);"
        id_masuk = id()
        cursor.execute(sql_query, (id_masuk, tanggal(), jam(), id_gambar))
        db.mydb.commit()
        parkir(npm, id_masuk)
        
def parkir(npm, id_masuk):
        sql_query = "INSERT INTO `parkir` (`id_parkir`, `id_tarif`, `npm`, `id_masuk`, `id_keluar`, `plat_nomor`, `status`) VALUES (%s, %s, %s, %s, NULL, %s, %s);"
        cursor.execute(sql_query, (id(), 1, npm, id_masuk, "Z123FE", "IN"))
        db.mydb.commit()

def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_image(id, image_path):
    try:
        binary_image = convert_to_binary_data(image_path)
        sql_query = "INSERT INTO gambar (id_gambar, gambar) VALUES (%s, %s);"
        cursor.execute(sql_query, (id, binary_image))
        db.mydb.commit()
    except:
        print("Error executing")
    


