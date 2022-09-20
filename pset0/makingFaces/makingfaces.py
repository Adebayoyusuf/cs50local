def main():
    faces = str(input("faces: "))
    result = convert(faces)
    print(result)

def convert(faces):

    faces=faces.replace(":)", '🙂').replace(":(",'🙁')
    return faces


main()


