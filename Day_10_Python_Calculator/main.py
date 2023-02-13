from art import logo


#Add
def add(n1, n2):
  return n1+n2
#Substract
def substract(n1, n2):
  return n1-n2
#Multiply
def multiply(n1, n2):
  return n1*n2
#Divide
def divide(n1, n2):
  return n1/n2
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}
def calculator():
  print(logo)
  
  num1=float(input("What is the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol=input("Pick an operation: ")
    num2=float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Tipe 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
      num1 = answer
      
    else:
      should_continue = False
      calculator()
calculator()