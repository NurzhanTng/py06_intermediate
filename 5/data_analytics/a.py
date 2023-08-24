from data import data
import json


def get_average_rating(data: list[dict[str, str]]) -> float:
    summ = 0
    for el in data: 
        summ += float(el["rating"])
    return int(summ / len(data) * 1000) / 1000


def get_all_categories(data: list[dict[str, str]]) -> list[str]:
    all_categories = set()
    for el in data:
        for category in el["category"].split('|'):
            all_categories.add(category)
    return list(all_categories)


def get_count_for_categories(data: list[dict[str, str]], categories: list) -> dict[str, int]:
    categories_count = {}
    
    for category in categories:
        categories_count[category] = 0
    
    for el in data:
        for el_category in el['category'].split('|'):
            categories_count[el_category] += 1
    
    return categories_count


def print_dict(data):
    print(json.dumps(data, indent=4))



average_rating = get_average_rating(data)
categories = get_all_categories(data)
categories_count = get_count_for_categories(data, categories)

print_dict(categories_count)