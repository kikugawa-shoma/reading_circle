from app.person import Person

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.personName = "Bob"
        self.personAge = 21

    def testCreatePersonWithNameAndAge(self):
        person = Person(self.personName, self.personAge)
        self.assertEqual(self.personName, person.getName())
        self.assertEqual(self.personAge, person.getAge())
