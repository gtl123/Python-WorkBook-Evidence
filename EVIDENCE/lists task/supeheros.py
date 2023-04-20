heroes = ["Batman", "Wonder Woman", "Superman", "Spiderman"]
print("Current pilot: ", heroes[0])
print("Current copilot: ", heroes[1])
heroes[2] = "Hit Girl"

print("The full list of superheroes currently in the Alliance:")
for i, hero in enumerate(heroes):
    print(f"{i+1}. {hero}")

member_to_replace = int(input(f"Which member would you like to replace (a number from 1 to {str(len(heroes))})? ")) - 1
new_hero = input("What is the name of the new superhero? ")

heroes[member_to_replace] = new_hero

print("Here's the updated list of superheroes currently in the Alliance:")
for i, hero in enumerate(heroes):
    print(f"{i+1}. {hero}")