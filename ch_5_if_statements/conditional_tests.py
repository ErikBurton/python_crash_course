car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

drummer = 'eric singer'
print("\nIs drummer != 'neil peart'? I predict False.")
print(drummer == 'stewart copeland')

print("Is drummer == 'neil peart'? I predict True.")
print(drummer == 'neil peart')
print(f"The drummer is {drummer.title()}.")

drum_brands = ["dw", "pearl", "tama", "sonar"]

best_drum = "dw"

if best_drum in drum_brands:
    print(f"The best drum brand is {best_drum.upper()}!")
else:
    print("You need a better set of drums!")
