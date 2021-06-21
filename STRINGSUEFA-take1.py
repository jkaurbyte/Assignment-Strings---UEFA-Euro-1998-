# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_scored_goal = 'Ruud Gullit'
second_scored_goal = 'Marco van Basten'
# tijdvandescores
goal_1 = str(32)
goal_2 = str(54)
scorers = (first_scored_goal + '  ' + goal_1  +  ',' + '  ' + second_scored_goal + '  ' + goal_2)
print(scorers)
firstplayer = {'name': first_scored_goal, 'goaltime' : goal_1}
secondplayer = {'name': second_scored_goal, 'goaltime' : goal_2}
report = f"{firstplayer['name']} scored in the {firstplayer['goaltime']} nd minute, {secondplayer['name']} scored in the {secondplayer['goaltime']} th minute"
print(report)
#leerpunten: niet snappen charting, in de war met vraag 3- hoe te zetten. wrm str wat is het. haakjes weg bij namen, zijn ook gwn variabelen '' is anders dan ""
player = 'Ronald Koeman'
first_name = player.find('Ronald')
print(first_name)
last_name_len = player.find('Koeman')
print(last_name_len)
len(player)
print(len(player))
last_name_len = 'Koeiman'
print(len(last_name_len))
name_short = 'R. Koeman'
chant = 'Ronald!' * 6
print(chant)
print(2 != 3)
print(2 != 2)
print(2 !=3) == (2 != 2)
