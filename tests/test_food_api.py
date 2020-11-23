import unittest
from food_api.food_api import FoodApi


class FoodApiTest(unittest.TestCase):
    def setUp(self):
        self.api = FoodApi()

    def test_get_meals_by_name(self):
        response = self.api.get_meals_by_name('Arrabiata')
        self.assertEqual(response['meals'][0]['idMeal'], '52771')

    def test_get_meals_by_first_letter(self):
        response = self.api.get_meals_by_first_letter('a')
        meal_names = []
        for meal in response['meals']:
            meal_names.append(meal['strMeal'])
        self.assertCountEqual(meal_names, ['Apple & Blackberry Crumble', 'Apple Frangipan Tart'])

    def test_get_meal_by_id(self):
        response = self.api.get_meal_by_id(52772)
        self.assertEqual(response['meals'][0]['strMeal'], 'Teriyaki Chicken Casserole')

    def test_get_random_meal(self):
        response = self.api.get_random_meal()
        self.assertEqual(len(response['meals']), 1)

    def test_get_meal_categories(self):
        response = self.api.get_meal_categories()
        categories = []
        for meal in response['categories']:
            categories.append(meal['strCategory'])
        self.assertCountEqual(categories, [
            'Beef',
            'Chicken',
            'Dessert',
            'Lamb',
            'Miscellaneous',
            'Pasta',
            'Pork',
            'Seafood',
            'Side',
            'Starter',
            'Vegan',
            'Vegetarian',
            'Breakfast',
            'Goat'
        ])

    def test_get_categories_list(self):
        response = self.api.get_categories_list()
        self.assertEqual(len(response['meals']), 14)

    def test_get_areas_list(self):
        response = self.api.get_areas_list()
        self.assertEqual(len(response['meals']), 25)

    def test_get_ingredients_list(self):
        response = self.api.get_ingredients_list()
        ingredient_name = ''
        for ingredient in response['meals']:
            if ingredient['idIngredient'] == '370':
                ingredient_name = ingredient['strIngredient']
                break
        self.assertEqual(ingredient_name, 'Paccheri Pasta')

    def test_get_filter_meals_by_ingredient(self):
        response = self.api.get_filter_meals_by_ingredient('chicken_breast')
        meals = []
        for meal in response['meals']:
            meals.append(meal['idMeal'])
        self.assertCountEqual(meals, [
            '53016',
            '52850',
            '52818',
            '52875',
            '53011',
            '52951',
            '52993',
            '52820',
            '52933'
        ])

    def test_get_filter_meals_by_category(self):
        response = self.api.get_filter_meals_by_category('Seafood')
        meal_id = ''
        for meal in response['meals']:
            if meal['strMeal'] == 'Seafood fideuà':
                meal_id = meal['idMeal']
                break
        self.assertEqual(meal_id, '52836')

    def test_get_filter_meals_by_area(self):
        response = self.api.get_filter_meals_by_area('Canadian')
        self.assertEqual(len(response['meals']), 13)

    def tearDown(self):
        self.api = None


if __name__ == '__main__':
    unittest.main()
