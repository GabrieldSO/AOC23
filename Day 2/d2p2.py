import re
#good ol' boilerplate code
f = open("Day 2/d2i.txt", "r")
lines = f.readlines()
power_sum = 0
for line in lines:
    #string manipulation
    #this gets us the played games
    game_results = (line.split(": "))[-1]
    game_list = game_results.split("; ")
    #we're gonna tally the results for each game, tally the highest 
    red_tally = []
    green_tally = []
    blue_tally = []
    for game in game_list:
        plays = game.split(", ")
        for play in plays:
            #this section is annoying but it's tallying all the results
            if(re.findall(r"(?=(red))", play)):
                num_red = int((play.split(" red"))[0])
                red_tally.append(num_red)
            if(re.findall(r"(?=(green))", play)):
                num_green = int((play.split(" green"))[0])
                green_tally.append(num_green)
            if(re.findall(r"(?=(blue))", play)):
                num_blue = int((play.split(" blue"))[0])
                blue_tally.append(num_blue)
    red_max = max(red_tally)
    green_max = max(green_tally)
    blue_max = max(blue_tally)
    power = red_max * green_max * blue_max
    power_sum += power

print(power_sum)
    