import pymongo
import requests
import mysql.connector


def import_starships():
    """Importing starships from API"""
    results = []

    starships0 = requests.get("https://swapi.dev/api/starships").json()
    for starship in starships0['results']:
        results.append(starship)

    starships = starships0
    while starships['next'] is not None:
        starships = requests.get(starships['next']).json()
        for starship in starships['results']:
            results.append(starship)

    return results

def import_db():
    try:
        """Importing database from MongoDB client"""
        uri = "mongodb://localhost:27017"
        client = pymongo.MongoClient(uri)
        db = client['star_wars']
        return db
    except:
        return None


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="star_wars",
)

if connection.is_connected():
    db_info = connection.get_server_info()
    print(f"Successfully connected to MySQL Server version {db_info}")

cursor = connection.cursor(buffered=True)
cursor.execute("SELECT DATABASE();")
record = cursor.fetchone()


def character_input():
    db = import_db()
    character_query = "INSERT IGNORE INTO characters (name) Values (%s)"
    characters = db.characters.find({}, {})
    for character in characters:
        values = character['name'],
        cursor.execute(character_query, values)
        connection.commit()

    print("Added all characters to the MySQL database")



def starships_input():
    starships = import_starships()

    name_query = "INSERT IGNORE INTO starships (name, model) Values (%s, %s)"

    tuple_list = []

    for starship in starships:
        name_values = starship['name']
        model_values = starship['model']
        tuple_list.append((name_values, model_values))

    cursor.executemany(name_query, tuple_list)
    connection.commit()
    print("Added all starships to the MySQL database")


def starships_characters_input():
    db = import_db()
    starships = import_starships()
    characters = db.characters.find({}, {})

    for starship in starships:
        if starship['pilots'] != []:
            starship_name = starship['name']

            cursor.execute(
                "SELECT ID FROM starships WHERE name = %s", (starship_name, )
            )
            starship_row = cursor.fetchone()

            if not starship_row:
                continue

            starship_id = starship_row[0]

            for pilot in starship['pilots']:
                pilot_data = requests.get(pilot).json()
                pilot_name = pilot_data['name']

                cursor.execute(
                    "SELECT ID FROM characters WHERE name = %s", (pilot_name, )
                )
                pilot_row = cursor.fetchone()

                if not pilot_row:
                    continue

                pilot_id = pilot_row[0]

                # FIXED: Removed trailing comma (string) and corrected parameter order (character_id first, starship_id second)
                junction_query = "INSERT IGNORE INTO character_starships (character_id, starship_id) VALUES (%s, %s)"

                cursor.execute(junction_query, (pilot_id, starship_id))
                connection.commit()
                print("Added", starship_name, starship_id, pilot_id, pilot_name)


# character_input()
# starships_input()
# starships_characters_input()