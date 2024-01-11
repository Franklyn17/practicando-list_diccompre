import requests

def main():

    '''
    this funcions take a city and return weather of that city
    '''
    city = input("Give me a city: ")
    url = f"https://wttr.in/{city}"
    weather = requests.get(url).text
    print(weather)


if __name__ == "__main__": 
    main()
