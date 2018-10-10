# find percent of females and males registered for class. 
# 10/10/2018
# CTI-110 P2HW2 - Male Female Percentage
# Benjamin Clark

# Find number of males and females registerd for class.

males = int( input( " Please enter the number of males in the class: "))

females = int( input( " Please enter the number of females in the class: "))
# Find total number 
totalStudents = males + females

# malePercent = ( males / totalStudents )

# femalePercent = ( females / totalStudents ) 

malePercent = males / totalStudents

femalePercent = females / totalStudents

print( " Male Percentage: " , format( malePercent,'.0%' ))
print( " Female Percentage: " , format( femalePercent,'.0%' ))
