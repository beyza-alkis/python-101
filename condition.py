a = [1, 2, 3]

# type control
if isinstance(a, list):
    print("Bu variable integer")
elif isinstance(a, str):
    print("Bu variable string")
else:
    print("Int ve string değil")


# type control
if type(a) is int:
    print("Bu variable integer")
elif type(a) is str:
    print("Bu variable string")
else:
    print("Int ve string değil")