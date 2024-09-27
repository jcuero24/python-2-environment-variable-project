import os
from dotenv import load_dotenv
 
environment = input("Elige el entorno (dev/pro): ").strip().lower()
print(f"Entorno seleccionado: {environment}")

if environment == "dev":
    load_dotenv(".env.dev")
elif environment == "pro":
    load_dotenv(".env.pro")
else:
    print("Entorno no válido. Usa 'dev' o 'pro'.")
    exit()
    
# Acceder a las variables de entorno
user_name = os.getenv("USER_NAME")
api_key = os.getenv("API_KEY")
email = os.getenv("EMAIL")
database_url = os.getenv("DATABASE_URL")

# Imprimir las variables de entorno
print(f"USER_NAME: {user_name}")
print(f"API_KEY: {api_key}")
print(f"EMAIL: {email}")
print(f"DATABASE_URL: {database_url}")
