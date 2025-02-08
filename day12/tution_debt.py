# At one college, the tuition for a full-time student is $8000 oer semester.
# It has been announced that the tution will increase by 3 % each year for the next 5 years.
# Write a program with a loop that displays the projected semester tution for the next 5 years.

# The tution therefore per year will equals $16000 as x2 semesters makes a academic year.
# The tution will increase by 3% per year
# THe loop needs to diplay the prohect tution for 5 years

tution = 16000

for year in range(1, 6):
    tution *= 1.03
    print(f"Year {year}: ${tution:,.2f}")