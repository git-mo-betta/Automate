#!/usr/bin/python3 

#alt shift 3 gives the line numbers
import time

print("Whats up?") 
time.sleep(1)
print("How ya doin?")
time.sleep(1)
print("lets get down to business")
weight = int(input("How much do you weigh(Pounds)?"))
protein = float(.7 * weight)
protein = int(protein) 
print(f"You should be eating {protein} grams of protein a day")


