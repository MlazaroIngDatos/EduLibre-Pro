import os
import json
import redis
import boto3
from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # Esto carga tus llaves del archivo .env
app = Flask(__name__)

# Conexión a MongoDB (Almacenamiento permanente)
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client['edulibre_pro']
recursos = db.materiales

# Conexión a Redis (Velocidad/Caché)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASS"),
    decode_responses=True
)
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
)
BUCKET_NOMBRE = os.getenv("AWS_BUCKET")

@app.route('/materiales', methods=['GET'])
def listar():
    # 1. ¿Está en la memoria rápida (Redis)?
    en_cache = cache.get("lista_pro")
    if en_cache:
        print(">>> Respuesta instantánea desde Redis")
        return jsonify(json.loads(en_cache)), 200

    # 2. Si no, buscar en MongoDB (más lento)
    print(">>> Buscando en MongoDB Atlas...")
    lista = list(recursos.find({}, {'_id': 0})) # Traer datos sin el ID raro de Mongo
    
    # 3. Guardar en Redis por 60 segundos para la próxima consulta
    cache.setex("lista_pro", 60, json.dumps(lista))
    return jsonify(lista), 200
@app.route('/materiales', methods=['POST'])
def guardar():
    datos = request.json
    # 1. Guardar en MongoDB Atlas
    recursos.insert_one(datos)
    
    # 2. IMPORTANTE: Borramos la caché de Redis 
    # para que la próxima lectura traiga los datos nuevos
    cache.delete("lista_pro")
    
    return jsonify({"mensaje": "Material guardado y caché sincronizada"}), 201

@app.route('/subir', methods=['POST'])
def subir_archivo():
    # Recibimos el archivo físico y el título
    archivo = request.files['archivo']
    titulo = request.form.get('titulo')

    # 1. Subir a la nube de Amazon
    s3.upload_fileobj(archivo, BUCKET_NOMBRE, archivo.filename)
    
    # 2. Generar link público
    url_aws = f"https://{BUCKET_NOMBRE}://{archivo.filename}"

    # 3. Guardar metadata en Mongo y limpiar Redis
    recursos.insert_one({"titulo": titulo, "url": url_aws})
    cache.delete("lista_pro")

    return jsonify({"mensaje": "Archivo guardado en AWS S3", "url": url_aws}), 201    
if __name__ == '__main__':
    app.run(debug=True)