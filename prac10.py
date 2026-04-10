p = input("p(True/False):").strip().lower() == "true"
q = input("q(True/False):").strip().lower() == "true"
op = input("op(AND/OR/NOT):").strip().lower()

if op == "and":
    print(p and q)
elif op == "or":
    print(p or q)
elif op == "not":
    print(not p)
else:
    print("invalid")