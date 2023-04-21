#Wilson Xu, section03, assignment 08 part 2


# So I use a lot of try/except that I learned from lecture and module 9 to handle runtime errors from user input.


#add, remove, list, search by name, search by type, and generate a report.

#List
pokemon_names = ['Charmander', 'Squirtle', 'Bulbasaur', 'Gyrados']
pokemon_amounts = [3, 2, 5, 1]
pokemon_fees = [100.00, 50.00, 25.00, 1000.00]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]

valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

def list_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types):
  #  the alignment and width of each column.
  print(f"{'Name':<24}{'Amount Available':<20}{'Adoption Fee':<15}{'Type(s)':<10}")
  for i in range(len(pokemon_names)):
      print(f"{pokemon_names[i]:<24}{pokemon_amounts[i]:<20}{pokemon_fees[i]:<15,.2f}{' '.join(pokemon_types[i]):<10}")


def search_by_name(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types):
    name = input("Enter the name of the Pokemon: ").strip()
    if name.lower() not in [pn.lower() for pn in pokemon_names]:
        print("Pokemon not found")
        return

    index = [pn.lower() for pn in pokemon_names].index(name.lower())
    print(f"Name: {pokemon_names[index]}")
    print(f"Amount Available: {pokemon_amounts[index]}")
    print(f"Adoption Fee: ${pokemon_fees[index]:,.2f}")
    print(f"Type(s): {' '.join(pokemon_types[index])}")

#part 2d 
def search_by_type(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types):
    p_type = input("Enter the type of Pokemon: ").lower()
    # learned enumerate in lecture useful
    results = [i for i, pt in enumerate(pokemon_types) if p_type in pt]
    if not results:
        print("No Pokemon found with this type")
        return

    print(f"Pokemon found with type '{p_type}':")
    for index in results:
        print(f"Name: {pokemon_names[index]}, Amount Available: {pokemon_amounts[index]}, Adoption Fee: ${pokemon_fees[index]:,.2f}")

#part 2e
def add_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types, valid_pokemon_types):
  name = input("Enter name of new pokemon: ").strip()
  if name.lower() in [pn.lower() for pn in pokemon_names]:
      print("Duplicate name, add operation cancelled")
      return

  while True:
      try:
          amount = int(input("How many of these Pokemon are you adding? "))
          if amount <= 0:
              raise ValueError
          break
      except ValueError:
          print("Invalid, please try again")

  while True:
      try:
          fee = float(input("What is the adoption fee for this Pokemon? "))
          if fee <= 0:
              raise ValueError
          break
      except ValueError:
          print("Invalid, please try again")

  print("Next you will be prompted to enter the 'types' for this Pokemon. Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
  new_types = []
  while True:
      p_type = input("What type of Pokemon is this? ").lower()
      if p_type == 'help':
          print("* " + "\n* ".join(valid_pokemon_types))
      elif p_type == 'end':
          if not new_types:
              print("You must enter at least one valid 'type'")
          else:
              break
      elif p_type in valid_pokemon_types:
          new_types.append(p_type)
          print(f"Type {p_type} added")
      else:
          print("This is not a valid type, please try again")
#Use .append
  pokemon_names.append(name)
  pokemon_amounts.append(amount)
  pokemon_fees.append(fee)
  pokemon_types.append(new_types)
  print("Pokemon Added!")

#part 2f
def remove_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types):
  name = input("Enter name of Pokemon to remove: ").strip()
  if name.lower() not in [pn.lower() for pn in pokemon_names]:
      print("Pokemon not found, cannot remove")
      return
#Use pop.() I learn from module 10 to remove and return an value at a specific index in the list.
  index = [pn.lower() for pn in pokemon_names].index(name.lower())
  pokemon_names.pop(index)
  pokemon_amounts.pop(index)
  pokemon_fees.pop(index)
  pokemon_types.pop(index)
  print("Pokemon removed")

#part 2g
def generate_report(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types):
    if not pokemon_names:
        print("No Pokemon in the center")
        return

    highest_priced_index = 0
    lowest_priced_index = 0
    total_cost = 0

    for i in range(len(pokemon_names)):
        if pokemon_fees[i] > pokemon_fees[highest_priced_index]:
            highest_priced_index = i
        if pokemon_fees[i] < pokemon_fees[lowest_priced_index]:
            lowest_priced_index = i
        total_cost += pokemon_amounts[i] * pokemon_fees[i]

    print("Highest priced Pokemon: {} @ ${:,.2f} per Pokemon".format(pokemon_names[highest_priced_index], pokemon_fees[highest_priced_index]))
    print("Lowest priced Pokemon: {} @ ${:,.2f} per Pokemon".format(pokemon_names[lowest_priced_index], pokemon_fees[lowest_priced_index]))
    print("Total cost to adopt all Pokemon in the Center: ${:,.2f}".format(total_cost))

#Main program user input
while True:
    print("\nWelcome to the Pokemon Center!")
    choice = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ").lower()

    if choice == 'a':
        add_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types, valid_pokemon_types)
    elif choice == 'r':
        remove_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types)
    elif choice == 'e':
        generate_report(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types)
    elif choice == 's':
        search_by_name(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types)
    elif choice == 't':
        search_by_type(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types)
    elif choice == 'l':
        list_pokemon(pokemon_names, pokemon_amounts, pokemon_fees, pokemon_types)
    elif choice == 'q':
        print("See you next time!")
        break
    else:
        print("Invalid choice, please try again")
