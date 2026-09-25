import pymongo
import unittest
import star_wars_project as sw
import mongomock

class UnitTesting(unittest.TestCase):

    def test_import_starships(self):
        starships = sw.import_starships()
        assert isinstance(starships, dict)
        self.assertEqual(starships['results'][0]['name'], 'CR90 corvette')

    def test_import_db(self):
        db = sw.import_db()
        assert isinstance(db, pymongo.database.Database)
        self.assertEqual(db.characters.find()[0]['name'], 'Ackbar')

    def test_starships_replace(self):
        starships = sw.import_starships()
        db = sw.import_db()
        character = db.characters.find_one({"name" : "Chewbacca"})
        starships_replaced = sw.replace_pilots(db, starships)
        self.assertEqual(starships_replaced['results'][4]['pilots'][0], character["_id"])

    def setUp(self):
        self.db = mongomock.MongoClient()['star_wars']
        self.db.characters.insert_one({"name": "Luke Skywalker", "_id": "123456"})

    def test_replace_pilots(self):
        starships = {
            "results": [{
                "name": "Millennium Falcon",
                "pilots": ["https://swapi.dev/api/people/1/"],
            }]
        }
        result = sw.replace_pilots(self.db, starships)

        # 5. Assert that the pilot's name/URL was successfully replaced with the database _id
        self.assertEqual(result["results"][0]["pilots"], ["123456"])