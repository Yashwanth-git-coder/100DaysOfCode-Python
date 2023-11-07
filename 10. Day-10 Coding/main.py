import art
#add a number
def add(num1,num2):
  return num1 + num2

#subtract a number
def sub(num1,num2):
  return num1 - num2

#multiply a number
def mul(num1,num2):
  return num1 * num2

#divide a number
def div(num1,num2):
  return num1 / num2

oparetion_dictionary = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}
def calculation():
  print(art.logo)
  num1 = int(input("What is your first number : "))
  for symbol in oparetion_dictionary:
    print(symbol)
  should_continue = True
  while should_continue:
    oparetion_symbol = input("Pick oparetor to perform : ")
    num2 = int(input("What is your next number : "))
    oparetion_function = oparetion_dictionary[oparetion_symbol]
    answer = oparetion_function(num1,num2)
    print(f"{num1} {oparetion_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue with {answer} or 'n' to start new caluclation : ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculation()

calculation()