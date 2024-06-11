import random
countries_and_capitals = {
    "China": "Beijing",
    "India": "New Delhi",
    "United States": "Washington DC",
    "Indonesia": "Jakarta",
    "Pakistan": "Islamabad",
    "Brazil": "Brasilia",
    "Sweden": "Stockholm",
    "Bangladesh": "Dhaka",
    "Russia": "Moscow",
    "Mexico": "Mexico City",
    "Japan": "Tokyo",
    "Norway": "Oslo",
    "Philippines": "Manila",
    "Egypt": "Cairo",
    "Finland": "Helsinki",
    "Turkey": "Ankara",
    "Iran": "Tehran",
    "Thailand": "Bangkok",
    "United Kingdom": "London",
    "France": "Paris",
    "Italy": "Rome",
    "Denmark": "Copenhagen",
    "South Africa": "Pretoria",
    "Belgium": "Brussels",
    "South Korea": "Seoul",
    "Spain": "Madrid",
    "Argentina": "Buenos Aires"
}
print("~~~Welcome to the Capital City Guessing Game!~~~")
print("\n~Type 'start' to begin or 'quit' to exit the game.~")
countries = list(countries_and_capitals.keys())
capitals = list(countries_and_capitals.values())
while True:
    user_input = input().strip().upper()
    if user_input == "START":
        index = random.randint(0, len(countries) - 1)
        country = countries[index]
        capital = capitals[index].upper()
        print(f"The capital of {country} has {len(capital)} letters. Can you guess the capital city?")
        count = 1
        while count <= len(capital):
            guess = input("Your guess: ").strip().upper()
            if guess == capital:
                print("\nCorrect!")
                print("\n~Type 'start' to go again or 'quit' to exit the game.~")
                break
            elif count == len(capital):
                print(f"\nSorry, the correct answer was {capital}.")
                print("\n~Type 'start' to go again or 'quit' to exit the game.~")
                break
            else:
                print(f"Hint: {capital[:count]}...")
                count += 1
    elif user_input == "QUIT":
        print("Thank you for playing!")
        break
    else:
        print("Invalid command. Please type 'start' to begin or 'quit' to exit.")