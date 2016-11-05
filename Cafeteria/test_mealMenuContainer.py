from unittest import TestCase
from Cafeteria.MealMenuContainer import MealMenuContainer


class TestMealMenuContainer(TestCase):
    def test_serialize(self):
        mealMenuContainer = MealMenuContainer(main="Main", pastaOrRice="PastaOrRice", soup="Soup",
                                              extra1="Extra1", extra2="Extra2", extra3="Extra3")

        serialized = mealMenuContainer.serialize()

        self.assertEqual(serialized[0], "Main")
        self.assertEqual(serialized[5], "Extra3")

    def test_toJson(self):
        mealMenuContainer = MealMenuContainer(main="Main", pastaOrRice="PastaOrRice", soup="Soup",
                                              extra1="Extra1", extra2="Extra2", extra3="Extra3")

        jsonified = mealMenuContainer.toJson()

        self.assertEqual(jsonified['main'], "Main")
        self.assertEqual(jsonified['extra3'], "Extra3")
