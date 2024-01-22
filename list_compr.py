# list compresion

def is_consonant(letter):
    vocals = "aeiou"
    return letter.isalpha() and letter.lower() not in vocals

def run():
    paragraph = "lleno de palabra"
    filter_list = [letter for letter in paragraph if is_consonant(letter)]
    print(filter_list)

if __name__ == "__main__":
    run()

    

#list_of_number = [number for number in range(1, 101) if number % 2 == 0]

#print(list_of_number)
