import re
#good ol' boilerplate code
f = open("Day 2/d2i.txt", "r")
lines = f.readlines()
game_id_sum = 0
max_red = 12
max_green = 13
max_blue = 14
for line in lines:
    #string manipulation
    #this gets us the played games
    game_results = (line.split(": "))[-1]
    game_list = game_results.split("; ")
    #this gets us the id
    game_title = (line.split(": "))[0]
    game_id  = int((game_title.split("Game "))[-1])

    #the plan is to check if all plays are valid
    #so we need to check if the game is valid
    game_valid = True
    for game in game_list:
        plays = game.split(", ")
        for play in plays:
            #this section is annoying but it's checking to see if any of them broke the limit
            if(re.findall(r"(?=(red))", play)):
                num_red = int((play.split(" red"))[0])
                if num_red > max_red:
                    game_valid = False
            if(re.findall(r"(?=(green))", play)):
                num_green = int((play.split(" green"))[0])
                if num_green > max_green:
                    game_valid = False
            if(re.findall(r"(?=(blue))", play)):
                num_blue = int((play.split(" blue"))[0])
                if num_blue > max_blue:
                    game_valid = False
    #if all plays are valid the game is valid so we add it to the tally
    if (game_valid):
        game_id_sum +=game_id
print(game_id_sum)
    