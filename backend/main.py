from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
import uvicorn

app = FastAPI(title="API Innovatech Chile")



# CONFIGURACIÓN CORS: es Vital para que React se conecte al Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# CREDENCIALES SUPABASE 
SUPABASE_URL = "https://idvouuvgjgsccgirbsso.supabase.co"
SUPABASE_KEY = "sb_publishable_socGEhroN0waoEe8SOPJ5w_GI6Om0vh"




# Creamos el cliente de Supabase para interactuar con la base de datos
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)    

@app.get("/") 
def read_root():
    return {"mensaje": "Backend operando correctamente para Innovatech"}


@app.get("/items")  # Endpoint para obtener items desde Supabase
def get_items():    
    try:
        response = supabase.table("items").select("*").execute()  
        return response.data
    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":  # Punto de entrada para ejecutar el servidor
    uvicorn.run(app, host="0.0.0.0", port=8000) 


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "innovatech-backend"}

from pydantic import BaseModel

# Definimos el modelo de datos para recibir la información (Pydantic)
class Item(BaseModel):
    nombre: str
    precio: float

# ENDPOINT POST: Crea un producto nuevo en Supabase
@app.post("/items")
def crear_producto(item: Item):
    try:
        data = {"nombre": item.nombre, "precio": item.precio}
        response = supabase.table("items").insert(data).execute()
        return {"mensaje": "Producto creado con éxito", "datos": response.data}
    except Exception as e:
        return {"error": str(e)}

# ENDPOINT GET (Health): Para el botón de tu diapositiva
@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}
