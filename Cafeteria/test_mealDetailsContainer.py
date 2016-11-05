from unittest import TestCase
from Cafeteria.MealDetailsContainer import MealDetailsContainer
from Cafeteria.MealMenuContainer import MealMenuContainer
from datetime import datetime

class TestMealDetailsContainer(TestCase):
    def _testSetup(self):
        mealMenuContainerTr = MealMenuContainer(
            main="Ana", pastaOrRice="Pilav ya da makarna", soup="Corba",
            extra1="Eks1", extra2="Eks2", extra3="Eks3")
        mealMenuContainerEn = MealMenuContainer(
            main="Main", pastaOrRice="PastaOrRice", soup="Soup",
            extra1="Extra1", extra2="Extra2", extra3="Extra3")
        self.mealDetailsContainer = MealDetailsContainer(
        start=datetime(year=2016, month=10, day=27, hour=13),
        end=datetime(year=2016, month=10, day=27, hour=14),
        en_name="EnName",
        tr_name="TrName",
        en_menu=mealMenuContainerEn,
        tr_menu=mealMenuContainerTr
        )

    def test_serialize(self):
        self._testSetup()

        serialized = self.mealDetailsContainer.serialize()
        self.assertEqual(serialized[2], "EnName")
        self.assertEqual(serialized[0], datetime(year=2016, month=10, day=27, hour=13))
        self.assertEqual(serialized[4], "Main")
        self.assertEqual(serialized[10], "Ana")

    def test_toJson(self):
        self._testSetup()

        jsonified = self.mealDetailsContainer.toJson()
        self.assertEqual(jsonified['en_name'], "EnName")
        self.assertEqual(jsonified['en_menu']['main'], "Main")
        self.assertEqual(jsonified['tr_menu']['extra3'], "Eks3")
