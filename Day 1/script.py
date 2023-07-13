import random;

print("Welcome to my Band Generator World")
while True:
  city = input("Where are you from? \n")
  if city.strip() != "":
    print("Great you are a step closer")
    break
while True:
  pet = input("What's your favourite pet's name? \n")
  if pet.strip() != "":
    print("You are almost there")
    break
while True:
  name = input("What is your name \n")

  if name.strip() != "":
    bandChoices = [name, pet, city]
    random.shuffle(bandChoices)

    generatedName = ""
    for index, item in enumerate(bandChoices):
        if index != len(bandChoices)-1:
          generatedName += item + "_"
        else:
          generatedName += item
          
    print(f'Your generated Band name is {generatedName}')
    break