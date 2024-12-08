number = int(input())

if (number % 2 == 0) and (number > 0):
    print("polozhitelnoe 4etnoe 4islo.")
elif (number % 2 != 0) and (number > 0):
    print("polozhitelnoe ne4etnoe 4islo.")
elif (number % 2 == 0) and (number < 0):
    print("otricatelnoe 4etnoe 4islo")
elif (number % 2 != 0) and (number < 0):
    print ("otricatelnoe ne4etnoe 4islo")
else:
    print("4islo ravno nulju")
