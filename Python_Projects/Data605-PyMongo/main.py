from star_wars_project import *
from querying import *

starships = import_starships()

db = import_db()
if starships != None and db != None:
    starships_replaced = replace_pilots(db, starships)
    update_pilots(db, starships_replaced)

print("Finding pilots who pilot > 1 starship.")
print(find_multiple_pilots())

print("\nFinding starships with no pilots.")
print(empty_starships())

print("\nFinding characters that pilot starships with corellian manufacturing")
print(corellian_pilots())

print("\nFinding starships with < 1 hyperdrive rating")
print(low_rating_starships())

print("\nFinding starships that are imperial or made by Sienar")
print(imperial_or_sienar_starships())

print("\nFinding film counts per film")
print(film_count())

print("\nFinding film with the most characters")
fmc = film_most_characters()
print(fmc[0], "\n The highest character film is", fmc[1])

print("\n Finding the most popular character")
mpc = most_popular_character()
print(mpc[0],"\n", mpc[1])