
import random

import time

# print game title and instructions
print("== Turbo Titans Car Racing Game ==")
print("------------------------------------")
print("Choose a car (1 to 6) and a race distance (5 to 15)")
print("Roll the die and move forward if the car's number comes up")
print("The first car to reach the race distance wins!")
print("------------------------------------------------------------")

# define car names with corresponding numbers
car_names={
    1: "Turbo Racer",
    2: "Speed Demon",
    3: "Nitro Boost",
    4: "Lightning Bolt",
    5: "Thunder Storm",
    6: "Supercharger"
}
# print out car options for the user
print("Your car choices are:")
for car_num, car_name in car_names.items():
    print(f"{car_num}: {car_name}")


# define choose_car() function to prompt user to choose a car and return car_num and car_name
def choose_car():
    # Ask the user to choose a car
    while True:
        try:
            car_num = int(input("Choose your car (1-6): "))
            if car_num < 1 or car_num > 6:
                raise ValueError
            else:
                car_name = car_names[car_num]
                print(f"You have chosen the {car_name}!")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

    return car_num, car_name

# Call the choose_car() function and assign the return values to car_num and car_name
car_num, car_name = choose_car()

# Print the chosen car number and name
print(f"Car number: {car_num}")
print(f"Car name: {car_name}")

# Print a separator line
print("------------------------------")

# define choose_race_distance() function to prompt user to choose a race distance and return the value
def choose_race_distance():
    # Ask the user to choose a race distance
    while True:
        try:
            race_distance = int(input("Choose your race distance (5-15): "))
            if race_distance < 5 or race_distance > 15:
                raise ValueError
            else:
                print(f"You have chosen a race distance of {race_distance}!")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 5 and 15.")

    return race_distance


# Call the choose_race_distance() function and assign the return value to race_distance
race_distance = choose_race_distance()




# Define the function to ask the user if they want to start the race
def start_race():
    while True:
        start = input("Are you ready to start the race? (y/n): ")
        if start.lower() == 'y':
            print("Let the race begin!")
            break
        elif start.lower() == 'n':
            print("Maybe next time!")
            exit()
        else:
            print("Invalid input. Please enter y or n.")

# Call the start_race() function
start_race()

# Print a separator line
print("------------------------------")



# Define the function to generate a random number
def roll_die():
    return random.randint(1, 6)


# Initialize the total distance for each car to 0
total_distances = {car_name: 0 for car_name in car_names.values()}

# Keep rolling the die and moving each car until a car reaches the finish line
while True:
    for car_name in car_names.values():
        if total_distances[car_name] >= race_distance:
            print(f"{car_name} wins! ")
            print(f"{car_name} won the race after {total_distances[car_name]} moves!") # prints the winner
            exit()
        else:
            roll = roll_die()
            if roll == car_num:
                total_distances[car_name] += 1   # adds a number to the total distance for rolled car
                print(f"{car_name} now at {total_distances[car_name]}.")
                time.sleep(0.2)   # adds a 1 sec space between each line being printed
# your code goes here