# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_first_goal = 'Ruud Gullit'
scorer_second_goal = 'Marco van Basten'
# tijdvandescores
goal_0 = 32
goal_1 = 54
scorers = (scorer_first_goal + '  ' + str(goal_0)  +  ',' + '  ' + scorer_second_goal + '  ' + str(goal_1))
print(scorers)
firstplayer = {'name': scorer_first_goal, 'goaltime' : goal_0}
secondplayer = {'name': scorer_second_goal, 'goaltime' : goal_1}
report = f"{firstplayer['name']} scored in the {firstplayer['goaltime']}nd minute, {secondplayer['name']} scored in the {secondplayer['goaltime']}th minute"
print(report)

soccerplayer = 'Ronald Koeman'
# first_name: use slicing and the find-method (help) to isolate and store the player's first name.
space_location = soccerplayer.find(' ')
print(space_location)
#last_name_len: use find, slicing and len to isolate and store the length of their last name.
first_name_sliced = soccerplayer[:space_location]
last_name_sliced = soccerplayer[space_location:]
print(first_name_sliced, last_name_sliced)


last_name_len = len(last_name_sliced)
print(last_name_len)
# name_short: isolate and store the player's name in this format: 'R. Koeman'
name_short = first_name_sliced[0] + '.'  + last_name_sliced
print(name_short)

#variabelenminmogelijkhouden, dus variabelfirstnamegebruiken, spatie weghalen om format te behouden dus Ronald ipv Ronald_- had ook in begin gekunt)
first_name_len = len(first_name_sliced)
chant = (first_name_sliced + '!'+' ') * first_name_len

print(chant)

good_chant = chant[0:-1]   #isoleren van tekens die ik wel wil behouden dus tm laatste !
print(good_chant)
print(good_chant[-1] != ' ')
#leerpunten: geen rood/ nieuwe var. str -> var voor later gebruik, niet snappen charting, in de war met vraag 3- hoe te zetten. wrm str wat is het. haakjes weg bij namen, zijn ook gwn variabelen '' is anders dan ""
#zo min mogelijk nieuwe variabelen maken, oude herbruiken
# 