import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('api_key')
database_url = os.getenv('database_url')

print(f"API KEY: {api_key}")
print(f"database URL: {database_url}")