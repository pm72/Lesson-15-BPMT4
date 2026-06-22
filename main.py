print("Hello, world!..")


def my_func(a, b):
  if a < b:
    a, b = b, a

  return a - 3 * b



# ====================
result = my_func(25, 7)

print(f"Result: {result}")

print("Hi Vs Code")

result = my_func(1.056, 0.0096)