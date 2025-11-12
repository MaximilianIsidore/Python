import json

person = {"name" : "eric", "age" : 20, "degree": [ "Doctor", "Engineer"]}

print(person)

person_json = json.dumps(person, indent=4)
print(person_json)

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)


loaded = json.loads(person_json)
print(loaded)

with open('person.json', 'r') as file:
    loaded_file = json.load(file)
    print(loaded_file)