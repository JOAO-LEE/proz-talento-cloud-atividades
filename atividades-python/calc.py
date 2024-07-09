def calculadora(num_one, num_two, operation):
  if operation == "+":
    return num_one + num_two
  elif operation == "-":
    return num_one - num_two
  elif operation == "*":
    return num_one * num_two
  elif operation == "/":
    return num_one / num_two
  else:
    return 0

print(calculadora(244, 2, "-"))