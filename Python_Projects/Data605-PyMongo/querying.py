from star_wars_project import import_db
import requests

# $eq
# $gt
# $gte
# $in
# $lt
# $lte
# $ne
# $nin

db = import_db()
def data_checker():
    """Checks that the primary foreign relationship is working for the newly created database with pilot ObjectID's"""

    # Error handling
    try:
        # Pipeline to compare characters and starships keys
        pipeline = [
            {
                "$lookup" : {
                    "from" : "characters",
                    "localField" : "pilots",
                    "foreignField" : "_id",
                    "pipeline" : [
                        {
                            "$project" : {
                                "_id" : 0,
                                "name" : 1
                            }
                        }
                    ],
                    "as" : "pilot_info"
                }
            },
        ]
        # Calling the pipeline
        db.starships.aggregate(pipeline)
        return True
    except:
        return False


def find_multiple_pilots():
    """Finding pilots that pilotted multiple ships by using lists"""
    # Error handling
    try:
        # Pipeline to find none ships
        pilot_pipeline = [
            {
                "$match" : { "pilots" : {"$ne" : []}}
            }]

        # Finding all ships without pilots
        piloted_ships = list(db.starships.aggregate(pilot_pipeline))
        pilots = []
        multiple_pilots = []

        # Running through ships
        for ship in piloted_ships:

            # Running through the pilots per ship
            for pilot in ship["pilots"]:

                # Checking if they have pilotted another ship
                if pilot not in pilots:
                    pilots.append(pilot)
                elif pilot not in multiple_pilots:
                    multiple_pilots.append(pilot)

        # Finding the names of the pilots
        multiple_named_pilots = []
        for pilot in multiple_pilots:

            # Finding the pilot according to the Object ID per pilot and adding to a new list
            pilot_name = db.characters.find_one({"_id" : pilot}, {"_id" : 0, "name" : 1})["name"]
            multiple_named_pilots.append(pilot_name)
        return multiple_named_pilots
    except:
        return False



def empty_starships():
    """Finding ships with no pilots"""
    try:
        # Setting pipeline to check for empty pilot lists and return only the name
        empty_pipeline = [
            {"$match" : { "pilots" : {"$eq" : []}}},
            {"$project" : {"_id" : 0, "name" : 1}}
        ]

        # Returning the list of starships without pilots
        return list(db.starships.aggregate(empty_pipeline))
    except:
        return None


def corellian_pilots():
    """Finding all pilots that drove corellian made ships, returning names"""

    # Error Handling
    try:
        # Pipeline to find the ships made by corellian
        corellian_pipeline = [
            {"$match" : { "manufacturer" : {"$eq" : "Corellian Engineering Corporation"}}},
            {"$project" : {"_id" : 0, "pilots" : 1}}
        ]
        # Using a set to have a unique set of characters that pilotted corellian ships
        pilot_set = set()
        for starship in db.starships.aggregate(corellian_pipeline):
            for pilot in starship["pilots"]:
                pilot_set.add(pilot)

        # Adding the pilots from the set into a new names only list
        pilot_names = []
        for pilot in pilot_set:
            pilot_names.append(db.characters.find_one({"_id" : pilot}, {"_id" : 0, "name" : 1})["name"])
        return pilot_names
    except:
        return None



def low_rating_starships():
    """Finding starships with < 1.0 hyperdrive rating"""

    # Error Handling
    try:
        # Adding a new field of numerics to handle with $lt operation
        low_rating_pipeline = [
            {"$addFields": {"numeric_rating": {"$convert": {"input" : "$hyperdrive_rating", "to" : "double", "onError" : None, "onNull" : None}}}},
            {"$match" : { "numeric_rating" : { "$lt" : 1.0}}},
            {"$project" : {"_id" : 0, "name" : 1, "numeric_rating": 1}}
        ]
        return list(db.starships.aggregate(low_rating_pipeline))
    except:
        return None


def imperial_or_sienar_starships():
        """Finding a list of starships made by Sienar or that are Imperial"""

        # Error handling
        try:
            # Pipeline to check manufactur and model entries for Sienar Fleet Systems or Imperial containing entries
            imp_sienar_pipeline = [
                {
                    "$match" : {
                        "$or" : [
                            {"manufacturer": {"$regex": "Sienar Fleet Systems", "$options": "i"}},
                            {"manufacturer": {"$regex": "Imperial", "$options": "i"}},
                            {"model" : {"$regex" : "Imperial", "$options": "i"}}
                        ]
                    }
                },
                {
                    "$project" : {"_id" : 0, "name" : 1, "manufacturer" : 1, "model" : 1}
                }
            ]
            # Returning the starships that satisfy the pipeline
            return list(db.starships.aggregate(imp_sienar_pipeline))
        except:
            return None



def film_count():
    """Creating a dictionary of films and appearances in the starship data"""

    # Error handling
    try:
        # Setting up a dictionary for film counts
        film_count_dict = {}

        # Running through starship entries
        for starship in db.starships.find():
            # Checking if there is any films it is in
            if starship["films"] != []:
                # Running through each film and adding one if it already exists
                for film in starship["films"]:
                    if film not in film_count_dict:
                        film_count_dict[film] = 1
                    else:
                        film_count_dict[film] += 1

        # Dictionary to instead contain the film titles not references to the API
        film_name_dict = {}
        for film in film_count_dict.keys():
            film_name = requests.get(film).json()["title"]
            film_name_dict[film_name] = film_count_dict[film]
        return film_name_dict
    except:
        return None


def film_most_characters():
    """Running through films to find the most characters"""

    # Error handling
    try:
        # Setting up a dictionary to add the amount of characters per film
        films_characters_dict = {}

        # Getting film info from API
        films  = requests.get("https://swapi.dev/api/films")

        # Running through films and adding length of the character
        for film in films.json()["results"]:
            films_characters_dict[film["title"]] = len(film["characters"])

        # Finding the maximum value and key
        largest_key = max(films_characters_dict, key=films_characters_dict.get)

        # Returning the dictionary, biggest entry, and amount of characters
        return [films_characters_dict, largest_key, max(films_characters_dict.keys())]
    except:
        return None



def most_popular_character():
    """Finding the most popular character across all films"""

    # Error handling
    try:

        # Dictionary to add characters and appearances to
        character_app_dict = {}

        # Retrieving information from the API on films
        films = requests.get("https://swapi.dev/api/films")

        # Running through films
        for film in films.json()["results"]:

            # Running through characters per film
            for character in film["characters"]:

                # If that character is not in add, if so add one appearance
                if character not in character_app_dict:
                    character_app_dict[character] = 1
                else:
                    character_app_dict[character] += 1

        # Adding names per characters instead of API references
        names_dict = {}
        for character in character_app_dict.keys():
            character_name = requests.get(character).json()["name"]
            names_dict[character_name] = character_app_dict[character]

        # Finding the highest amount of appearances
        highest_value = max(names_dict.values())
        largest_key = max(names_dict, key=names_dict.get)

        new_dict = names_dict.copy()

        new_dict.pop(largest_key)
        most_popular_character_list = [largest_key]

        # Considering all duplications of the most popular character appearance amount
        while highest_value in new_dict.values():
            new_largest_key = max(new_dict, key=new_dict.get)
            most_popular_character_list.append(new_largest_key)
            new_dict.pop(new_largest_key)

        # Returning the original dictionary and the most popular characters list
        return [names_dict, most_popular_character_list]
    except:
        return [None, None]

