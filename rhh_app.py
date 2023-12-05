#========================================================================================================================================Importing Packages
import matplotlib.pyplot as plt
import random
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import os

#============Importing Scripts
import plotting


#========================================================================================================================================Player Images
def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=zoom)  

#========================================================================================================================================Random Hat Hat Function
def RandomHat(names,choice,goalkeeper,defenders,photos):
    
    name_list = []
    for name in names:
        name_list.append(str.upper(name[0]) + str.lower(name[1:len(name)+1]) )

    
    
    # If more than 5 people are playing, no goalkeeper/defenders excludes 5-back formations
    #if len(name_list) > 5:
     #   goalkeeper = 'y'
      #  print('Due to the number of players, we overrode your goalkeeper preference')
    
    # If more than 6 people are playing, no goalkeeper/defenders excludes 4-back formations
    #elif len(name_list) > 6:
     #   goalkeeper = 'y'
      #  defenders = 'y'
       # print('Due to the number of players, we overrode your defender and goalkeeper preference')
    
    paths = []
    for name in name_list:
        paths.append('/Users/thomas795/Library/Mobile Documents/com~apple~CloudDocs/coding/proclubs/rhh/rhh_app/Faces/'+ str.upper(name[0]) + str.lower(name[1:len(name)+1]) +'.png')
    all_formations = [('3142', ['gk', 'lcb', 'cb', 'rcb', 'cdm', 'lcm', 'rcm', 'lm', 'rm', 'ls', 'rs']), ('3412', ['gk', 'lcb', 'cb', 'rcb', 'lcm', 'rcm', 'lm', 'rm', 'cam', 'ls', 'rs']), ('3421', ['gk', 'lcb', 'cb', 'rcb', 'lcm', 'rcm', 'lm', 'rm', 'lf', 'st', 'rf']), ('343', ['gk', 'lcb', 'cb', 'rcb', 'lcm', 'rcm', 'lm', 'rm', 'lw', 'st', 'rw']), ('352',  ['gk', 'lcb', 'cb', 'rcb', 'ldm', 'rdm', 'lm', 'rm', 'cam', 'ls', 'rs']), ('41212',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lm', 'rm', 'cam', 'ls', 'rs']), ('41212(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lcm', 'rcm', 'cam', 'ls', 'rs']), ('4132', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lm', 'cm', 'rm', 'ls', 'rs']), ('4141', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lm', 'lcm', 'rcm', 'rm', 'st']), ('4222',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'ldm', 'rdm', 'lam', 'ram', 'ls', 'rs']), ('4231',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'ldm', 'rdm', 'lam', 'cam', 'ram', 'st']), ('4231(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'ldm', 'rdm', 'lm', 'cam', 'rm', 'st']), ('424', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lcm', 'rcm', 'lw', 'ls', 'rs', 'rw']), ('4312', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lcm', 'cm', 'rcm', 'cam', 'ls', 'rs']), ('4321', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lcm', 'cm', 'rcm', 'lf', 'st', 'rf']), ('433', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lcm', 'cm', 'rcm', 'lw', 'st', 'rw']), ('433(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lcm', 'rcm', 'lw', 'st', 'rw']), ('433(3)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'ldm', 'rdm', 'cm', 'lw', 'st', 'rw']), ('433(4)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lcm', 'rcm', 'cam', 'lw', 'st', 'rw']), ('433(5)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'cdm', 'lcm', 'rcm', 'lw', 'cf', 'rw']), ('4411', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'lcm', 'rcm', 'rm', 'cf', 'st']), ('4411(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'lcm', 'rcm', 'rm', 'cam', 'st']), ('442', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'lcm', 'rcm', 'rm', 'ls', 'rs']), ('442(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'ldm', 'rdm', 'rm', 'ls', 'rs']), ('451', ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'cm', 'rm', 'lam', 'ram', 'st']), ('451(2)',  ['gk', 'lb', 'lcb', 'rcb', 'rb', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'st']), ('5212',  ['gk', 'lwb', 'lcb', 'cb', 'rcb', 'rwb', 'lcm', 'rcm', 'cam', 'ls', 'rs']), ('5221',  ['gk', 'lwb', 'lcb', 'cb', 'rcb', 'rwb', 'lcm', 'rcm', 'lw', 'st', 'rw']), ('532', ['gk', 'lwb', 'lcb', 'cb', 'rcb', 'rwb', 'lcm', 'cm', 'rcm', 'ls', 'rs']), ('541', ['gk', 'lwb', 'lcb', 'cb', 'rcb', 'rwb', 'lm', 'lcm', 'rcm', 'rm', 'st'])]
    fig, ax = plt.subplots(figsize=(11, 7))
    positions = []; allocation = []
    names_len = len(name_list)
    
    formation_text = 25; info_text = 15; name_text = 15
    check_colour = 'black'
    name_colour = 'darkviolet'
    
    
    diff = 3
    if choice == 0:
        formation = random.choice(all_formations)
    else:
        formation = all_formations[int(choice)-1]  
    for i in formation[1]:
        positions.append(i)
    if goalkeeper == 'n':
        positions.remove('gk')
        plt.text(plotting.width+1,plotting.height-diff,'Goalkeeper:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(plotting.width+14,plotting.height-diff,'No',horizontalalignment = 'left',fontsize = info_text,color = 'red')
        diff += 3
    else:
        plt.text(plotting.width+1,plotting.height-diff,'Goalkeeper:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(plotting.width+14,plotting.height-diff,'Yes',horizontalalignment = 'left',fontsize = info_text,color = 'green')
        diff += 3
        
    if defenders == 'n':
        positions[:] = [item for item in positions if item[-1] != 'b']
        plt.text(plotting.width+1,plotting.height-diff,'Defenders:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(plotting.width+13,plotting.height-diff,'No' ,horizontalalignment = 'left',fontsize = info_text,color = 'red')
        diff += 3
    else:
        plt.text(plotting.width+1,plotting.height-diff,'Defenders:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(plotting.width+13,plotting.height-diff,'Yes' ,horizontalalignment = 'left',fontsize = info_text,color = 'green')
        diff += 3
    
    if len(positions) < len(name_list):
        return RandomHat(names,choice,goalkeeper,defenders,photos)
    
    while len(allocation) < names_len:
        random_name, random_pos = random.choice(name_list), random.choice(positions)
        allocation.append([random_name,random_pos])
        positions.remove(random_pos); name_list.remove(random_name)
    
    #Title
    plt.title(formation[0], fontsize = formation_text)
    
    fig.set_facecolor('w')
    plotting.form_plot(formation,allocation)
    plotting.draw_pitch(pitch_color='darkgreen', 
               line_color="black",
               ax=ax)
        
    if photos == 'y':
        #Plotting Faces
        for pos in plotting.form_plot(formation,allocation):
            for allo in allocation:
                if pos[0] == allo[1]:
                    for path in paths:
                        if allo[0] in path:
                            isFile = os.path.isfile(path)
                            if isFile == True:
                                ab = AnnotationBbox(getImage(path, zoom = 1/Image.open(path).size[0] * marker_size * 1.1), (pos[1][0], pos[1][1]), frameon=False)
                                ax.add_artist(ab)
      
    plt.savefig('Formation.jpeg', dpi = 500, bbox_inches = 'tight')

#========================================================================================================================================Inputs

num_players = int(input(('How many people will be playing?: ')))
while num_players > 11:
    print('Try again...')
    num_players = int(input('How many people will be playing?: '))

    
players = []
for i in range(num_players):
    player = input('Player {}: '.format(i+1))
    players.append(player)


###################################################
print('')
print('Formation Table:')
print(' _______________ _______________ _______________')
print('| 1 : 3142      | 11 : 4231     | 21 : 4411     |')
print('| 2 : 3412      | 12 : 4231 (2) | 22 : 4411 (2) |')
print('| 3 : 3421      | 13 : 424      | 23 : 442      |')
print('| 4 : 343       | 14 : 4312     | 24 : 442 (2)  |')
print('| 5 : 352       | 15 : 4321     | 25 : 451      |')
print('| 6 : 41212     | 16 : 433      | 26 : 451 (2)  |')
print('| 7 : 41212 (2) | 17 : 433 (2)  | 27 : 5212     |')
print('| 8 : 4132      | 18 : 433 (3)  | 28 : 5221     |')
print('| 9 : 4141      | 19 : 433 (4)  | 29 : 532      |')
print('| 10 : 4222     | 20 : 433 (5)  | 30 : 541      |')
print('|                                               |')
print('|              0 : Random Formation             |')
print(' --------------- --------------- ---------------')
print('')
###################################################

num_range = range(31)
nums = []
for i in num_range:
    nums.append(str(i))

choice = input('Which formation would you like to use?: ')
while choice not in nums:
    print('Try again...')
    choice = input('Which formation would you like to use?: ')

choice = int(choice)
    
y_n = ('y','n')

if num_players > 5:
    print('Due to the number of players:')
    print('- Goalkeeper must be included')
    goalkeeper = 'y'
else:
    goalkeeper = str.lower(input('Would you like to include a goalkeeper? [y/n]: '))
    while goalkeeper not in y_n:
        print('Try again...')
        goalkeeper = str.lower(input('Would you like to include a goalkeeper? [y/n]: '))
    
if num_players > 6:
    print('- Defenders must be included')
    defenders = 'y'
else:
    defenders = str.lower(input('Would you like to include the defenders? [y/n]: '))
    while defenders not in y_n:
        print('Try again...')
        defenders = str.lower(input('Would you like to include the defenders? [y/n]: '))

photos = str.lower(input('Would you like to use player images? [y/n]: ' ))
while photos not in y_n:
    print('Try again...')
    photos = str.lower(input('Would you like to use player images? [y/n]: ' ))



#========================================================================================================================================Execution                   
RandomHat(players
          ,choice = choice
          ,goalkeeper = goalkeeper
          ,defenders = defenders
          ,photos = photos)
