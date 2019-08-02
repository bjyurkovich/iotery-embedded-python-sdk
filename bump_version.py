import re
with open("./setup.py", "r") as fh:
    setup = fh.read()
    r = re.search(r'version=*.*.*', setup)
    s = setup[r.span()[0]:r.span()[1]].strip()
    original = s
    s = s[0:-2].split(".")
    bump = int(s[-1])+1
    s[-1] = str(bump)
    s.insert(len(s)-1, ".")
    s.insert(-3, ".")
    s = "".join(s) + "\""
    
    # print(s)
    # print(original)
    setup = setup.replace(original, s+",")
    print(" ")
    print(" ")
    print(" ")
    print(f"Bumped from {original} to {s}")
    print(" ")
    print(" ")
    print(" ")
    
    with open("./setup.py", "w") as fo:
         fo.write(setup)