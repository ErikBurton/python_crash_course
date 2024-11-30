favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# language = favorite_languages['bob'].title()
# print(f"Jen's favorite language is {language}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
