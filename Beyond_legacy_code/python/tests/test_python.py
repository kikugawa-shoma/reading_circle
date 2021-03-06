from app.person import Person, AgeBelowMinimumException, AgeAboveMaximumException

import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.personName = "Bob"
        self.personAge = 21

    def testCreatePersonWithNameAndAge(self):
        person = Person(self.personName, self.personAge)
        self.assertEqual(self.personName, person.getName())
        self.assertEqual(self.personAge, person.getAge())

    def testConstraints(self):
        self.assertEqual(Person.MINIMUM_AGE, 1)
        self.assertEqual(Person.MAXIMUM_AGE, 200)

    def testConstructorThrowsExceptionWhenAgeBelowMinimum(self):
        with self.assertRaises(AgeBelowMinimumException):
            person = Person(self.personName, Person.MINIMUM_AGE-1)

    def testConstructorThrowsExceptionWhenAgeAboveMaximum(self):
        with self.assertRaises(AgeAboveMaximumException):
            person = Person(self.personName, Person.MAXIMUM_AGE + 1)
