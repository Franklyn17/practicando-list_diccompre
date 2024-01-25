
#def dict_square_root():# firts exercise
 #   dict_of_number = {number:round(number ** (1/2), 3) for number in range(1, 21)}
  #  return dict_of_number

    #tem1 = int(input(f"increse una temperatura: "))
    #tem2 = int(input(f"increse una temperatura: "))
    #tem3 = int(input(f"increse una temperatura: "))

     
def dic_celcius(dict_tempsF): # second exercise
    dict_tempsC = {key:round((val - 32)/1.8, 3) for (key, val) in dict_tempsF.items()}
    return dict_tempsC
   
def run():
   dict_tempsF = {'temp1':50, 'temp2':32, 'temp3':77}
   dict_tempsC = dic_celcius(dict_tempsF)
   print(dict_tempsC)

if __name__ == '__main__':
     run()

def dict_even_odd():# three exercise
   dict_of_number2 = {number:("even" if number % 2 == 0 else "odd") for number in range(1, 37)}
   return dict_of_number2

def run():
  dict_of_number2 = dict_even_odd()
  print(dict_of_number2)

if __name__ == '__main__':
     run()
# zio es comado que incluye las dos lista en el diccionario
def dict_with_list(list1, list2):# four exercise
   dict_from_list = {key:val for key, val in zip(list1, list2)}
   return dict_from_list

def run():
  name = ["pedro", "Juan", "luis"]
  age = [22, 20, 25]
  dict_from_list = dict_with_list(name, age)
  print(dict_from_list)

if __name__ == '__main__':
     run()

def dict_repeated_letter(text):# five exercise
   repeated_dict = {letter:text.count(letter) for letter in text.replace(" ","")}
   return repeated_dict

def run():
    text = "esta letra se repite"
    repeated_dict = dict_repeated_letter(text)  
    print(repeated_dict)

if __name__ == '__main__':
     run()