favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    "erin": "javascript",
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
    print()

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# fav_cars = {
#     "erik": "camaro",
#     "krista": "infinity",
#     "katie": "hyundai",
#     "nick": "jeep",
#     "alex": "toyota",
# }

# for name in fav_cars.keys():
#     print(name.title())
