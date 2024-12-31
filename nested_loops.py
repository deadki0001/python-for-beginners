for seconds in range(60):
    print(seconds)

# We can add a minutes variable and nest the loop above inside another loop that cycles through 60 mins.

for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)    

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)            