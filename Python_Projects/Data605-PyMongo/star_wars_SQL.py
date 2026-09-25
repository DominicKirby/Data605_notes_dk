import pymongo
import requests
import mysql.connector


def import_starships():
    try:
        """Importing starships from API"""
        starships = requests.get("https://swapi.dev/api/starships")
        return starships.json()
    except:
        return None

def import_db():
    try:
        """Importing database from MongoDB client"""
        uri = "mongodb://localhost:27017"
        client = pymongo.MongoClient(uri)
        db = client['star_wars']
        return db
    except:
        return None

  # 1. Establish the connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Reebok17.",  # Replace with your MySQL password
    database="star_wars",  # Optional: if the database already exists
)

if connection.is_connected():
    db_info = connection.get_server_info()
    print(f"Successfully connected to MySQL Server version {db_info}")

# 2. Create a cursor object to run queries
cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
record = cursor.fetchone()


db = import_db()
characters = db.characters.find({}, {})
characters_names = []
character_query = "INSERT IGNORE INTO characters (name) Values (%s)"

for character in characters:
    values = character['name'],
    cursor.execute(character_query, values)
    connection.commit()
    print(f'{character["name"]} has been added to the database')

starships = import_starships()

name_query = "INSERT IGNORE INTO starships (name, model) Values (%s, %s)"

tuple_list = []

for starship in starships['results']:
    name_values = starship['name']
    model_values = starship['model']
    tuple_list.append((name_values, model_values))
cursor.executemany(name_query, tuple_list)
connection.commit()


#print(import_starships()['results'])