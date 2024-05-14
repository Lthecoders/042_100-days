import os
import random
import time

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
black = "\033[30m"
reset = "\033[0m"

print(yellow, "\n\n🌟  MokeBeast Generator  🌟\n\n\n")

MOKEbest_data = {
    '\n name of MokeBest: ': '',
    '\n TYPE OF MOKEBEST: ': '',
    '\n special move of MokeBest: ': '',
    '\n starting HP: ': '',
    '\n starting MP: ': ''
}

print("Loading....", reset)
time.sleep(3)
os.system("clear")
print(yellow, "\n\n🌟  MokeBeast Generator  🌟\n\n\n", reset)
print(
    red,
    """Please make sure, You can only choose between fire, grass, water, electric,
  ice, flyfing, rock or Psychic. 
  \n\n """, reset)
for collect_user_data in MOKEbest_data:
  MOKEbest_data[collect_user_data] = input(
      f'{collect_user_data}').strip().lower()

os.system("clear")
print("\nSaving...")
time.sleep(3)
os.system("clear")
print(green, "\nSaved successfully in Moke'dex. 👍\n\n")
print("Loding your mokeDex....", reset)
time.sleep(4)
os.system("clear")
print(yellow, "-------------- Moke'Dex -------------\n", reset)

print()
print()
for x, y in MOKEbest_data.items():
  if MOKEbest_data["\n TYPE OF MOKEBEST: "] == "fire":
    print(f" {red} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "grass":
    print(f" {green} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "water":
    print(f" {blue} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "electric":
    print(f" {yellow} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "ice":
    print(f" {cyan} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "flying":
    print(f" {reset} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "rock":
    print(f" {black} ", end="")

  elif MOKEbest_data["\n TYPE OF MOKEBEST: "] == "psychic":
    print(f" {magenta} ", end="")

  else:
    print(f" {reset} ", end="")

for x, y in MOKEbest_data.items():
  print(f" {x} : {y} ", end="")

print()
print(reset)
