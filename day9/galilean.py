# Write a program that creates a dictionary, containing the names of the Galilean moons of Jupiter as Kyes
# Write their mean radiuses (in Kilometers) as values.
# The dictionary should contain the following key-pair values

moons_of_jupiter = [
    {
        "Moon": "Io",
        "Means_Radius": 1821.6,
        "Surface_Gravity": 1.796,
        "Orbital_Period": 1.769
    },
    {
        "Moon": "Europa", 
        "Means_Radius": 1560.8, 
        "Surface_Gravity": 1.314,
        "Orbital_Period": 3.551               
    },
    {      
        "Moon": "Ganymede",
        "Means_Radius": 2634.1,
        "Surface_Gravity": 1.428,
        "Orbital_Period": 7.154               
    },
    {  
        "Moon": "Callisto",
        "Means_Radius": 2410.3,
        "Surface_Gravity": 1.235,
        "Orbital_Period": 16.689               
    }        
]

# The program should let teh user enter a name of a Galilean moon of Jupiter, then it should display the moon's mean radius, surface gravity and orbital period.

userInput = input("Enter the name of a Galilean Moon of Jupiter: ")

for moon in moons_of_jupiter:
    if moon["Moon"].lower() == userInput.lower():
        print(f"\nDetails for {userInput}: ")
        print(f"Mean Radius {moon['Means_Radius']} km ")
        print(f"Surface Gravity {moon['Surface_Gravity']} m/s²")
        print(f"Orbital Period {moon['Orbital_Period']} days")
        break
else:
    print(f"\nSorry, {userInput} is not a Galilean moon of Jupiter.")    

                
    