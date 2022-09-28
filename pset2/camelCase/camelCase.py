def main():
    camelCase = input("camelCase: ")
    for char in camelCase:
        if char.isupper():
            camelCase = camelCase.replace(char, f"_{char.lower()}")
    print(f"snake_case: {camelCase}")      

if __name__ == "__main__":
    main()      



