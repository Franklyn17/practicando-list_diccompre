# Diccionario comprenhencia

def run():
   dict_of_number = {number:number * 2 for number in range(1, 11) if number % 2 == 0}
   print(dict_of_number)

if __name__ == "__main__":
    run()