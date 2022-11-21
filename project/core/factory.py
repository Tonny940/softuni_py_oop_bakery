from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Factory:
    food_types = {
        'Cake': Cake,
        'Bread': Bread
    }

    drink_types = {
        'Tea': Tea,
        'Water': Water
    }

    table_types = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def create_food(self, food_type, name, price):
        return self.__class__.food_types[food_type](name, price)

    def create_drink(self, drink_type, name, portion, brand):
        return self.__class__.drink_types[drink_type](name, portion, brand)

    def create_table(self, table_type, table_num, capacity):
        return self.__class__.table_types[table_type](table_num, capacity)
