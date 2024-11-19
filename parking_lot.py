import random
import time
import sys

parkingSpotNumbers = random.sample(range(1,21),5)
while(True):
    print("Welcome to Kia's Automatic Parking Lot!")
    time.sleep(0.5)
    print("Would you like to park here? Type Y for Yes to continue")
    response = input()
    if response == "Y" or response == "y":
        time.sleep(1)
        if len(parkingSpotNumbers) > 0:
            print("Hello, we have", len(parkingSpotNumbers), "parking spots:", parkingSpotNumbers)
            while(True):
                print("For how long do you want to park? The maximum duration is 12 hours and the minimum is 0.5 hours.") 
                hours_response = float(input())
                if hours_response > 0.5 and hours_response < 12:
                    min_parkingSpot = min(parkingSpotNumbers)
                    time.sleep(1)
                    print("Okay! You can park for", str(hours_response), "hours at parking spot #"+ str(min_parkingSpot))
                    print("Thank you for using the automated parking system!")
                    parkingSpotNumbers.remove(min_parkingSpot)
                    time.sleep(2)
                    break
                else:
                    print("That is an invalid selection. Please try again!")
        else:
            print("Sorry, there are no parking spots available at the moment!") 
            print("A spot will be available in hours, please come back then or reserve your spot now!")
            sys.exit()
    else:
        print("Okay! Thank you for coming!")