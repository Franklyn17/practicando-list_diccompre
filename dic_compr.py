# Diccionario comprenhencia

#def run():
 #  dict_of_number = {number:number * 2 for number in range(1, 21) if number % 2 == 0}
  # print(dict_of_number)

#if __name__ == "__main__":
 #   run()
def dict_square_root():
    dict_of_number = {number:round(number ** (1/2), 3) for number in range(1, 21)}
    return dict_of_number

def run():
   dict_of_number = dict_square_root()
   print(dict_of_number)

if __name__ == "__main__":
     run()