import random
import time

mylist = ["Lamborghini Aventador SV", "Ferrari La Ferrari", "Mclaren P1""Audi R8"]
numbers = [5, 6, 7, 8, 9, 10]
amount_of_cars=3
car_distances=[0,0,0]
display_car_distances=[0,0,0]
money=100000
bet=0
# Define the cars and their speeds
cars = ['Lamborghini Aventador SV', 'Ferrari La Ferrari', 'Mclaren P1']
    
def update_numbers(ml):
    for i in range(500):
        randomresult = random.choice(ml)
        if randomresult in ml:
            numbers[ml.index(randomresult)] += 1

def displaydist(cardist,aimdist): # defines the amount of 0 needed for the display (round to nearest number unless its over the race distance then round to race distance, or if not at finnish but rounds up to finnish number round down)
    if cardist>=aimdist:
        return aimdist
    if round(cardist)==aimdist:
        return aimdist-1
    else:
        return round(cardist)

def print_display(distance,display_distance): # prints the display of the race
    return "0"*round(display_distance)+"/"*(distance-round(display_distance))

def randomcar():
    return random.choice(cars)

def start():
    update_numbers(mylist)
    print(numbers)

    # Get user input for car and distance
    car_choice = input("Choose your car (Lamborghini Aventador SV, Ferrari La Ferrari, Mclaren P1): ")
    distance_choice = int(input("Choose the distance to race (in meters): "))
    while True:
        bet=input(f"you have {money}$ in the pot how much do you want to bet\n> ")
        try:
            bet=int(bet)
            if bet>money:
                print("your not that rich")
                continue
            if isinstance(bet,float):
                pass
            else:
                break
        except ValueError:
            pass

    # Start the race
    print("The race has started!")
    start_time = time.time()
    distance_covered = 0

    winning_car=""

    while True:
        distance_covered += random.uniform(0.5, 1.5)  # add random variation to the speed
        time.sleep(1)  # add delay for visual effect
        
        display_car_distances[0]=displaydist(car_distances[0],distance_choice)
        display_car_distances[1]=displaydist(car_distances[1],distance_choice)
        display_car_distances[2]=displaydist(car_distances[2],distance_choice)

        current_car = randomcar()
        print("-"*distance_choice)
        for i in range(amount_of_cars):
            print(print_display(distance_choice,display_car_distances[i-1])+"    "+str(round(car_distances[i-1],2)))
        print("-"*distance_choice)

        if winning_car != "":
            break

        if current_car == 'Lamborghini Aventador SV':  #checks distance over and over again
            car_distances[0] += distance_covered
            if car_distances[0] >= distance_choice:
                winning_car="Lamborghini Aventador SV"
        elif current_car == 'Ferrari La Ferrari':
            car_distances[1] += distance_covered
            if car_distances[1] >= distance_choice:
                winning_car="Ferrari La Ferrari"
        elif current_car == 'Mclaren P1':
            car_distances[2] += distance_covered
            if car_distances[2] >= distance_choice:
                winning_car="Mclaren P1"

    # Finish the race
    print(f'{winning_car} SV has won')
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\n{car_choice} has finished the race in {total_time:.2f} seconds!")
    # your code goes here
    
start()