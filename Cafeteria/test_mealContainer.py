from datetime import datetime
from unittest import TestCase

from Cafeteria.MealContainer import MealContainer
from Cafeteria.MealDetailsContainer import MealDetailsContainer
from Cafeteria.MealMenuContainer import MealMenuContainer


class TestMealContainer(TestCase):
    def _testSetup(self):
        mealMenuContainerTr = MealMenuContainer(
            main="Ana", pastaOrRice="Pilav ya da makarna", soup="Corba",
            extra1="Eks1", extra2="Eks2", extra3="Eks3")
        mealMenuContainerEn = MealMenuContainer(
            main="Main", pastaOrRice="PastaOrRice", soup="Soup",
            extra1="Extra1", extra2="Extra2", extra3="Extra3")
        mealDetailsContainer = MealDetailsContainer(
            start=datetime(year=2016, month=10, day=27, hour=13),
            end=datetime(year=2016, month=10, day=27, hour=14),
            en_name="EnName",
            tr_name="TrName",
            en_menu=mealMenuContainerEn,
            tr_menu=mealMenuContainerTr
        )

        self.mealContainer = MealContainer(
            datetime(year=2016, month=10, day=27, hour=14),
            mealDetailsContainer
        )

    def test_serialize(self):
        self._testSetup()
        serialized = self.mealContainer.serialize()
        self.assertEqual(serialized[0], datetime(year=2016, month=10, day=27, hour=14))
        self.assertEqual(serialized[11], "Ana")

    def test_toJson(self):
        self._testSetup()

        jsonified = self.mealContainer.toJson()
        self.assertEqual(jsonified['details']['en_name'], "EnName")
        self.assertEqual(jsonified['details']['en_menu']['main'], "Main")
        self.assertEqual(jsonified['details']['tr_menu']['extra3'], "Eks3")
