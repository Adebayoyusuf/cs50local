def main():
    fuel_level()


def fuel_level():
    while True:
        try:
            fuel = input("Fracion: ")
            x, y =fuel.split("/")
            x = int(x)
            y = int(y)
            indicate = (x/y) *100
            if indicate <=1:
                print("E")
            elif 99 < indicate <=100:
                print("F")
            elif 1 < indicate < 99:
                print(f"{round(indicate)}%") 
            else:
                continue
            break   
        except (ValueError, ZeroDivisionError):
            pass
    return fuel
        

if __name__ == "__main__":
    main()    