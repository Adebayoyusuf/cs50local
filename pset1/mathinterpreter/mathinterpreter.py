def main():
    interpreter()

def interpreter():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    

    if y == "+":
        result = x + z
        print(f"{result:.1f}")
    if y == "-":
        result  = x - z
        print(f"{result:.1f}")
    if y == "*":
        result = x * z
        print(f"{result:.1f}")
    if y == "/":
        result = x / z    
        print(f"{result:.1f}")  


main()


      