# Assuming the ocean's levels is currently rising at about 1.6 mm per year, 
# Create an application that displays the number of Milimeters that the ocean will have risen each year for the next 25 years.


# mm_per_year = 1.6
# years = 25

# # 1 year = 1.6mm how would we display this in 

# if mm_per_year == 1.6:
#     for year in years:
#         print(f"The Ocean has risen {year} this year")

print("Year\t", "Sea level Rise\n")
for currentYear in range(1, 26):
    seaLevelRise = currentYear * 1.6
    print(currentYear, "\t", format(seaLevelRise, ".2f"))