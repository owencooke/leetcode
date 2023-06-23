import math

memo = {}

def generate(expr, num):
    if len(expr) < 7:
        # Creating Postfix combinations of all operators
        generate(expr+[4], num+1)
        generate(expr+["+"], num)
        generate(expr+["-"], num)
        generate(expr+["/"], num)
        generate(expr+["*"], num)
    elif num == 4:
        compute(expr)

def compute(expr):
    # Computes postfix expression, result stored as key in memo
    #order = False
    vals = []
    try:
        for i in range(len(expr)):
            if expr[i] == 4:
                vals.append(4)
            elif expr[i] == "+":
                # if order:
                #     return
                y = vals.pop()
                x = vals.pop()
                vals.append(x+y)
            elif expr[i] == "-":
                # if order:
                #     return
                y = vals.pop()
                x = vals.pop()
                vals.append(x-y)
            elif expr[i] == "*":
                #order = True
                y = vals.pop()
                x = vals.pop()
                vals.append(x*y)
            elif expr[i] == "/":
                #order = True
                y = vals.pop()
                x = vals.pop()
                try:
                    vals.append(math.floor(x/y))
                except ZeroDivisionError: 
                    pass
        # Result is last value remaining, add to memo
        memo[vals.pop()] = expr
    except IndexError:
        pass
    
if __name__ == "__main__":
    expr = [4, 4]
    generate(expr, 2)
    m = int(input())
    for i in range(m):
        n = int(input())
        # Check if n is possible (in memo)
        try:
            expr = memo[n]
            # Convert from postfix to infix output
            vals = []
            for i in range(len(expr)):
                if expr[i] == 4:
                    vals.append("4")
                else:
                    y = vals.pop()
                    x = vals.pop()
                    vals.append(x + expr[i] + y)
            print(vals.pop())

        except KeyError:
            print("no solution")
