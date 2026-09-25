import pymongo
import requests

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

def replace_pilots(db, starships):
    """Replacing starship pilot hyperlinks with Object ID's from characters database"""
    for starship in starships:

        # Checking if the list is empty or to be replaced
        if starship['pilots'] != []:

            # Setting up a pilot list to append to later
            pilot_list = []

            # Finding the pilot ID to append to the pilot list
            for pilot_uri in starship['pilots']:
                pilot = requests.get(pilot_uri).json()
                pilot_id = list(db.characters.find({"name": pilot['name']}, {"_id" : 1}))[0]['_id']
                pilot_list.append(pilot_id)

            # Changing the local json instance
            starship['pilots'] = pilot_list
    return starships

def update_pilots(db, starships):
    """Upserting starship pilot object ID's"""
    print("-------------------")
    # Inserting or updating the new starship dataset with pilots included
    for starship in starships:
        db.starships.update_one({"starship.name" : starship['name']}, {"$set" : starship}, upsert=True)
        print("Inserted or Updated: ", starship['name'])
    print("-------------------")




