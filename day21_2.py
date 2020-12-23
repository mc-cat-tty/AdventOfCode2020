"""
Day 21, part 2 - Allergen Assessment

https://adventofcode.com/2020/day/21

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
from typing import List, Set, Dict

class Food:
    def __init__(self, ingredients: List[str], allergens: List[str]):
        self.ingredients: Set[str] = set(ingredients)
        self.allergens: Set[str] = set(allergens)

    def __and__(self, other):
        return self.ingredients & other.ingredients

    def __xor__(self, other):
        return self.ingredients ^ other.ingredients


def main():
    count: int = 0
    foods: List[Food] = list()
    all_allergens: Set[str] = set()
    all_ingredients: Set[str] = set()
    for line in sys.stdin:
        tokenized_line: List[str] = line.rsplit("(")
        ingredients_list: List[str] = tokenized_line[0].split()
        allergens_list: List[str] = tokenized_line[1].strip().replace("contains", "").replace(")", "").strip().split(", ")
        all_allergens.update(allergens_list)
        all_ingredients.update(ingredients_list)
        food: Food = Food(ingredients_list, allergens_list)
        foods.append(food)
    # print(all_allergens)

    # possible_dangerous_ingredients: List[Set[str]] = list()
    allergen_to_possible_dan_ing: Dict[str, Set[str]] = dict()
    for allergen in all_allergens:
        # print(allergen)
        a_foods: List[Food] = [food for food in foods if allergen in food.allergens]
        intersection: Set[str] = set.intersection(*map(lambda f: f.ingredients, a_foods))
        # print(intersection)
        # possible_dangerous_ingredients.append(intersection)
        allergen_to_possible_dan_ing[allergen] = intersection
    
    # print(allergen_to_possible_dan_ing)
    all_to_dan_ing: Dict[str, str] = dict()
    while allergen_to_possible_dan_ing:
        allergen_to_possible_dan_ing = sorted(allergen_to_possible_dan_ing.items(), key=lambda ele: len(ele[1]))
        allergen_to_possible_dan_ing = dict(allergen_to_possible_dan_ing)
        current_all: str = list(allergen_to_possible_dan_ing.keys())[0]
        current_ing: Set[str] = allergen_to_possible_dan_ing.pop(list(allergen_to_possible_dan_ing)[0])
        if not len(current_ing) == 1:
            continue
        for item in allergen_to_possible_dan_ing.values():
            item -= (current_ing & item)
        all_to_dan_ing[current_all] = current_ing
        # print(all_to_dan_ing)
        # print(allergen_to_possible_dan_ing, current_ing)

    sl = sorted(all_to_dan_ing.items(), key=lambda ele: ele[0])
    print(','.join([ele[1].pop() for ele in sl]))

    # union: Set[str] = set.union(*possible_dangerous_ingredients)
    # not_dan_ing: Set[str] = all_ingredients ^ union
    # for ing in not_dan_ing:
    #     for food in foods:
    #         count += list(food.ingredients).count(ing)
    # print(count)
    

if __name__ == "__main__":
    main()
