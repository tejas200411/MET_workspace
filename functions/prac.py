# def one_to_there():
#     print(1,2,3)
 
# def three_to_seven():
#     print(3,4,5,6,7)

# def seven_to_ten():
#     print(7,8,9,10)

# three_to_seven()
# one_to_there()
# seven_to_ten()

# def greet(lang, name):

#     if lang == "en":
#         print("Hello")

#     elif lang == "fr":
#         print("Bonjour")

#     else:
#         print("Hola")

# greet()
 
#  greet("eu", "joy")

data = [
    {
        "name": "raju",
        "age" : 18  
    },
    {
        "name":"prasant",
        "age" :"16"
    }
]

def get_names(details):
    name1 = details[0]["name"]
    name2 = details[1]["name"]
    return [name1,name2]




names = get_names(data)

print("mubarak")

print(names)