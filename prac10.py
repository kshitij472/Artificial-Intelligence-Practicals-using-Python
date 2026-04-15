#represent and evaluate prepositional logic expressions

p = input("p (True/false):").strip().lower() == "True"
q = input("q (True/False):").strip().lower() == "True"
op = input("Operations(AND/OR/NOT):").strip().lower()

if op == "and":
    print(p and q)
elif op == "or":
    print(p or q)
elif op == "not":
    print(not p)
else:
    print("Invalid choice")