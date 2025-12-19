introvert_points=0
extrovert_points=0
ambivert_points=0

answer1=input ("do you prefer to A be alone B be with others C both")
if answer1== "A" or answer1== "a":
    introvert_points += 1
elif answer1== "B" or answer1== "b":
    extrovert_points += 1
elif answer1== "C" or answer1== "c":
    ambivert_points += 1
print("")
print("")
answer2=input ("if your friend was having a dinner would you A have it just the 2 of you B have with lots of friends C might bring a friend you know just in case")
if answer2== "A" or answer2== "a":
    introvert_points += 1
elif answer2== "B" or answer2== "b":
    extrovert_points += 1
elif answer2== "C" or answer2== "c":
    ambivert_points += 1
print("")
print("")
answer3=input ("would you choose to A work alone B work with others C no preference")
if answer3== "A" or answer3== "a":
    introvert_points += 1
elif answer3== "B" or answer3== "b":
    extrovert_points += 1
elif answer3== "C" or answer3== "c":
    ambivert_points += 1
print("")
print("")
answer4=input ("do you A charge your social battery alone B charge your social battery with others C depends on the type of day")
if answer4== "A" or answer4== "a":
    introvert_points += 1
elif answer4== "B" or answer4== "b":
    extrovert_points += 1
elif answer4== "C" or answer4== "c":
    ambivert_points += 1
print("")
print("")
answer5=input ("at a restaurant do you A have someone oder for you B order for yourself C depends who is there")
if answer5== "A" or answer5== "a":
    introvert_points += 1
elif answer5== "B" or answer5== "b":
    extrovert_points += 1
elif answer5== "C" or answer5== "c":
    ambivert_points += 1
print("")
print("")
if introvert_points > extrovert_points and introvert_points > ambivert_points:
    print ("you are most likely to be a introvert")
elif extrovert_points > introvert_points and extrovert_points > ambivert_points:
    print ("you are most likely to be a extrovert")
elif ambivert_points > extrovert_points and ambivert_points > introvert_points:
    print ("you are a mix of both")