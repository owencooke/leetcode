#############################################
##
##  Name: Owen Cooke
##  Date: May 1, 2022
##  Kattis - Adding Words
##
#############################################

running = True
defs = {}
while running:
    try:
        line = input()
        words = line.split()
        if words[0] == "def":
            # Add definition to hash
            defs[words[1]] = int(words[2])
        elif words[0] == "calc":
            # Compute calculation
            unknown = False
            add = True
            try:
                result = defs[words[1]]
                for i in range(2, len(words)):
                    if i % 2 == 0:
                        if words[i] == "+":
                            add = True
                        else:
                            add = False
                    else:
                        if add:
                            result += defs[words[i]]
                        else:
                            result -= defs[words[i]]
            except KeyError:
                unknown = True
            # Output result
            if unknown:
                print(line[5:len(line)], "unknown")
            else:
                # Get key from result value
                unknown = True
                for key, value in defs.items():
                    if result == value:
                        print(line[5:len(line)], key)
                        unknown = False
                        break
                if unknown:
                    print(line[5:len(line)], "unknown")
        elif words[0] == "clear":
            defs.clear()

    except EOFError:
        running = False