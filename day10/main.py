from art import logo
from replit import clear
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2 
def multiply(n1, n2):
  return n1 * n2 
def divide(n1, n2):
  return n1 / n2

calci_dicts = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calci():
  clear()
  print(logo)
  num1 = float(input("What's the first number?: "))  
  for operand in calci_dicts:
    print(operand)

  choice = True
  while choice:
  
    operation_symbol = input("Pick an operation?: ")   
    if operation_symbol not in ('+','-','*','/'):
      print("Invalid operation!!")
      exit(1)
    compute = calci_dicts[operation_symbol]
    num2 = float(input("What's the next number?: "))
    answer = compute(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
     
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new: ") == "y":
      num1 = answer
    else:
      choice = False
      calci()
calci()








