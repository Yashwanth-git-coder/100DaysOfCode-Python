import art
import random
import game_data
import os

def format_data(account):
  account_name = account["name"]
  account_discri = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_discri} , from {account_country}"

def check_answer(guess, a_follwer_count, b_follwer_count):
  if a_follwer_count > b_follwer_count:
    return guess == 'a'
  else:
    return guess == 'b'

print(art.logo)
score = 0
game_continue = True
account_b = random.choice(game_data.data)
while game_continue:
  
  account_a = account_b
  account_b = random.choice(game_data.data)
  while account_a == account_b:
    account_b = random.choice(game_data.data)
  
  print(f"Compare_A : {format_data(account_a)}")
  print(art.vs)
  print(f"Against_B : {format_data(account_b)}")
  
  guess = input("Guess, who has more followers : type 'A' or 'B' : ").lower()
  
  a_follwer_count = account_a["follower_count"]
  b_follwer_count = account_a["follower_count"]
  is_correct = check_answer(guess, a_follwer_count, b_follwer_count)

  os.system("cls")
  
  if is_correct:
    score += 1
    print(f"Your are right, Current score : {score}")
  else:
    game_continue = False
    print(f"Sorry, Your are worrg, final score : {score}")