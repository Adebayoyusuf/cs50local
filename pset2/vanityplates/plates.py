def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #checks for no of characters
    if len(s) < 2 and len(s) > 6:
        return False
    #checks if the first 2 letters is alphabet    
    if s[0:2].isalpha():
        return False
    #checks if the string contians only alphabet and no    
    if s.isalnum():
        return True

    #checks if the string ends with a no(s)  
    #also checks if the no in the str doesnt start with a no     

    for character in s[2:]:
        if character.isalpha():
            continue
        elif character.isdigit() and character != "0":  
            return False      




    

if __name__ == "__main__":
    main()
