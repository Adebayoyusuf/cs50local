def main():
    word = str(input("Input: ")).lower()
    vowels = ["a", "e", "i", "o", "u"]
    letter = ""

    for char in word:
        if char.lower() not in vowels:
            letter += char

    print(f"Output: {letter}")        
            

if __name__ == '__main__':
    main()    