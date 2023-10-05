
class User:
   def __init__(self, user_name:str, password:str, email:str, meals:list):
      self.__user_name = user_name
      self.__password = password
      self.__email = email
      self.__meals = meals

   def change_password(self, email:str):
      pass

   def create_meal(self):
      pass

   def delete_meal(self):
      pass

class Food:
   def __init__(self, food_name:str, caloriesper:float, food_description:str):
       self.__food_name = food_name
       self.__caloriesper = caloriesper
       self.__food_description = food_description

   def get_calores(self):
      pass

   def get_fooddescription(self):
      pass

class Drink:
   def __init__(self, drink_name:str, caloriesper:float, drink_description:str):
      self.__drink_name = drink_name
      self.__caloriesper = caloriesper
      self.__drink_description = drink_description

   def get_calories(self):
      pass

   def get_drinkdescription(self):
      pass