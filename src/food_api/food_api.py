import requests


class FoodApi:
    def get_meals_by_name(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+name)
        return meals.json()

    def get_meals_by_first_letter(self, letter):
        if type(letter) != str:
            raise TypeError('Letter must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?f='+letter)
        return meals.json()

    def get_meal_by_id(self, id):
        if type(id) != str and type(id) != int:
            raise TypeError('Id must be a string or an integer')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+str(id))
        return meal.json()

    def get_random_meal(self):
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        return meal.json()

    def get_meal_categories(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        return categories.json()

    def get_categories_list(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
        return categories.json()

    def get_areas_list(self):
        areas = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
        return areas.json()

    def get_ingredients_list(self):
        ingredients = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
        return ingredients.json()

    def get_filter_meals_by_ingredient(self, ingredient):
        if type(ingredient) != str:
            raise TypeError('Ingredient must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?i='+ingredient)
        return meals.json()

    def get_filter_meals_by_category(self, category):
        if type(category) != str:
            raise TypeError('Category must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c='+category)
        return meals.json()

    def get_filter_meals_by_area(self, area):
        if type(area) != str:
            raise TypeError('Area must be a string')
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?a='+area)
        return meals.json()
