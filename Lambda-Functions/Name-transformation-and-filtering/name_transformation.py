import json

with open("names.json", 'r') as names_json:
    names = json.load(names_json)

# 1. Use the lambda function to transform a list of full names to the new format
def transform_names(names):

    formated_names = list(map(lambda name: " ".join(name.split(', ')[::-1]), names))

    return formated_names

# 2.  Filter the list to include only names that contain at least two vowels and are longer than 10 characters
def filter_names(names):

    def valid_name(name):
        vowels = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
        num_vowels = sum(1 for letter in name if letter in vowels)
        return num_vowels >= 2 and len(name) > 10

    filtered_names = list(filter(valid_name, names))
    return filtered_names

print(filter_names(transform_names(names)))