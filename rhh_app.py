#========================================================================================================================================Importing Packages
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from matplotlib.patches import Arc
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import time
import datetime
import os
from py_imessage import imessage
#========================================================================================================================================Defining Positions
width = 68; height = 52.5

marker_size = 45
marker_radius = np.sqrt(marker_size/np.pi)
offset = height/42
step = (height - 2*offset - 2*marker_radius)/5

class w:
    lwb = lw = width*0.1
    lb = lm = lam = width*0.15
    lam = width*0.2
    lcb = lcm = ls = lf = width*0.35
    ldm = width*0.4
    gk = cb = cdm = cm = cam = cf = st = width*0.5
    rdm = width*0.6
    rcb = rcm = rs = rf = width*0.65
    ram = width*0.8
    rb = rm = width*0.85
    rwb = rw = width*0.9

class h:
    gk = marker_radius + offset
    lb = lcb = cb = rcb = rb = marker_radius + offset + step
    lwb = rwb = marker_radius + offset + 1.5*step
    ldm = cdm = rdm = marker_radius + offset + 2*step
    lm = lcm = cm = rcm = rm = marker_radius + offset + 3*step
    lam = cam = ram = cf = marker_radius + offset + 4*step
    lf = rf = lw = rw = marker_radius + offset + 4.5*step
    ls = st = rs = marker_radius + offset + 5*step

class ht:
    gk = 0
    b = 1
    wb = 2
    dm = 3
    m = 4
    am = cf = 5
    f = w = 6
    st = s = 7
    
class colours:
    gk = 'darkorange'; defs = 'gold'; mids = 'limegreen'; atts = 'cornflowerblue'
    
#Goalkeeper
gk = (w.gk,h.gk)
#Defenders
lwb = (w.lwb,h.lwb); lb = (w.lb,h.lb); lcb = (w.lcb,h.lcb); cb = (w.cb,h.cb); rcb = (w.rcb,h.rcb); rb = (w.rb,h.rb); rwb = (w.rwb,h.rwb) 
#Midfielders
ldm = (w.ldm,h.ldm); cdm = (w.cdm,h.cdm); rdm = (w.rdm,h.rdm); lm = (w.lm,h.lm); lcm = (w.lcm,h.lcm); cm = (w.cm,h.cm); rcm = (w.rcm,h.rcm); rm = (w.rm,h.rm); lam = (w.lam,h.lam); cam = (w.cam,h.cam); ram = (w.ram,h.ram)
#Forwards
lf = (w.lf,h.lf); cf = (w.cf,h.cf); rf = (w.rf,h.rf); lw = (w.lw,h.lw); ls = (w.ls,h.ls); st = (w.st,h.st); rs = (w.rs,h.rs); rw = (w.rw,h.rw)


#========================================================================================================================================Drawing The Pitch
def draw_pitch(x_min=0, x_max=height*2,y_min=0, y_max=width,pitch_color="w",line_color="grey",line_thickness=1.5,point_size=20,ax=None):
    first = 1; second = 0; arc_angle = 90
    rect = plt.Rectangle((x_min, y_min),y_max, x_max,facecolor=pitch_color,edgecolor="none",zorder=-2)
    ax.set_ylim(0, x_max/2); ax.axis("off"); ax.add_artist(rect)
    x_conversion = x_max / 100; y_conversion = y_max / 100
    pitch_x = [0,5.8,11.5,17,50,83,88.5,94.2,100]; pitch_x = [x * x_conversion for x in pitch_x]
    pitch_y = [0, 21.1, 36.6, 50, 63.2, 78.9, 100]; pitch_y = [x * y_conversion for x in pitch_y]
    goal_y = [45.2, 54.8]; goal_y = [x * y_conversion for x in goal_y]
    # side and goal lines
    lx1 = [x_min, x_max/2, x_max/2, x_min, x_min]; ly1 = [y_min, y_min, y_max, y_max, y_min]
    # outer boxed
    lx3 = [0, pitch_x[3], pitch_x[3], 0]; ly3 = [pitch_y[1], pitch_y[1], pitch_y[5], pitch_y[5]]
    # 6 yard boxes
    lx7 = [0, pitch_x[1], pitch_x[1], 0]; ly7 = [pitch_y[2],pitch_y[2], pitch_y[4], pitch_y[4]]
    # penalty spots, and kickoff spot
    lx8 = [pitch_x[4]]; ly8 = [0]
    lines = [[lx1, ly1],[lx3, ly3],[lx7, ly7],[lx8, ly8]]
    points = [[pitch_x[6], pitch_y[3]],[pitch_x[2], pitch_y[3]],[pitch_x[4], pitch_y[3]]]
    circle_points = [pitch_x[4], pitch_y[3]]
    arc_points2 = [pitch_x[2], pitch_y[3]]
    for line in lines: ax.plot(line[first], line[second],color=line_color,lw=line_thickness,zorder=-1)
    for point in points: ax.scatter(point[first], point[second],color=line_color,s=point_size,zorder=-1)
    circle = plt.Circle((circle_points[first], circle_points[second]),x_max * 0.088,lw=line_thickness,color=line_color,fill=False,zorder=-1)
    ax.add_artist(circle)
    arc2 = Arc((arc_points2[first], arc_points2[second]),height=x_max * 0.088 * 2,width=x_max * 0.088 * 2,angle=arc_angle,theta1=308.75,theta2=51.25,color=line_color,lw=line_thickness,zorder=-1)
    ax.add_artist(arc2)
    ax.set_aspect("equal")
    return ax


#========================================================================================================================================Plotting Formation
def form_plot(formation, allocation = []):
    #Setting up the plot
    axes = plt.gca().set_aspect(1)
    plt.axis('off')
    
    pos_text = marker_size/2.5; name_text = marker_size/3
    
    #Array of relevant positions
    positions = formation[1]   
    
    #Arrays of all positions      
    goalkeeper = [('gk',gk,'GK')]
    def_pos = [('lwb',lwb,'LWB'),('lb',lb,'LB'),('lcb',lcb,'LCB'),('cb',cb,'CB'),('rcb',rcb,'RCB'),('rb',rb,'RB'),('rwb',rwb,'RWB')]
    mid_pos = [('ldm',ldm,'LDM'),('cdm',cdm,'CDM'),('rdm',rdm,'RDM'),('lm',lm,'LM'),('lcm',lcm,'LCM'),('cm',cm,'CM'),('rcm',rcm,'RCM'),('rm',rm,'RM'),('lam',lam,'LAM'),('cam',cam,'CAM'),('ram',ram,'RAM')]
    att_pos = [('lf',lf,'LF'),('cf',cf,'CF'),('rf',rf,'RF'),('lw',lw,'LW'),('ls',ls,'LS'),('st',st,'ST'),('rs',rs,'RS'),('rw',rw,'RW')]
    
    #Positional corrections
    if formation[0] == '451':
        mid_pos[8] = ('lam',(0.325*width,h.lam),'LAM')
        mid_pos[10] = ('ram',(0.675*width,h.ram),'RAM')    

    if formation[0][0] == '3' or formation[0][0] == '5':
        def_pos[2] = ('lcb',(width*0.3,h.lcb),'LCB')
        def_pos[4] = ('rcb',(width*0.7,h.rcb),'RCB')
        
    all_positions = goalkeeper + def_pos + mid_pos + att_pos

    #Plotting names
    for pos in all_positions:
        for allo in allocation:
            if pos[0] == allo[1]:
                plt.text(pos[1][0],pos[1][1]-marker_radius*1.3,str.upper(allo[0][0]) + str.lower(allo[0][1:len(allo[0])+1]),horizontalalignment = 'center', fontsize = name_text, color = 'w')
    
    
    
    
    #Plotting each position
    plt.plot(gk[0],gk[1], marker = 'o', color = colours.gk, markersize = marker_size)
    plt.text(gk[0],gk[1]-marker_size/45, 'GK', horizontalalignment = 'center', fontsize = pos_text)
    
    for i in def_pos:
        if i[0] in positions:
            plt.plot(i[1][0],i[1][1], marker = 'o', color = colours.defs, markersize = marker_size)
            plt.text(i[1][0],i[1][1]-marker_size/45, i[2], horizontalalignment = 'center', fontsize = pos_text)    
    for i in mid_pos:
        if i[0] in positions:
            plt.plot(i[1][0],i[1][1], marker = 'o', color = colours.mids, markersize = marker_size)
            plt.text(i[1][0],i[1][1]-marker_size/45, i[2], horizontalalignment = 'center', fontsize = pos_text)
    for i in att_pos:
        if i[0] in positions:
            plt.plot(i[1][0],i[1][1], marker = 'o', color = colours.atts, markersize = marker_size)
            plt.text(i[1][0],i[1][1]-marker_size/45, i[2], horizontalalignment = 'center', fontsize = pos_text)
    return all_positions



#========================================================================================================================================Stipulation Function
def random_stipulation(check = 0):
    stips = ['Choose Position',
             'Flair Assists',
             'Headers & Volleys',
             'Height & Weight',
             'Long Shots',
             'No Sprint',
             'Pro Camera',
             'Tiki Taka',
             'Sweats Only',
             'Compilation Goal',
             'No Calling The Ball',
            ]
    
    if check != 0:
        return stips
    
    stip_choice = random.choice(stips)
    if stip_choice == 'Height & Weight':
        h = random.randint(160,201)*0.0328084
        ft = int(h)
        inch = int((h % ft)*12)
        return str(ft) + 'ft ' + str(inch) + 'in ' + str(random.randint(99, 253)) + 'lbs'            
    else:        
        return stip_choice


#========================================================================================================================================Player Images
def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=zoom)  




#========================================================================================================================================Random Hat Hat Function
def RandomHat(names,choice,goalkeeper,defenders,stipulation,photos):
    
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
        plt.text(width+1,height-diff,'Goalkeeper:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(width+14,height-diff,'No',horizontalalignment = 'left',fontsize = info_text,color = 'red')
        diff += 3
    else:
        plt.text(width+1,height-diff,'Goalkeeper:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(width+14,height-diff,'Yes',horizontalalignment = 'left',fontsize = info_text,color = 'green')
        diff += 3
        
    if defenders == 'n':
        positions[:] = [item for item in positions if item[-1] != 'b']
        plt.text(width+1,height-diff,'Defenders:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(width+13,height-diff,'No' ,horizontalalignment = 'left',fontsize = info_text,color = 'red')
        diff += 3
    else:
        plt.text(width+1,height-diff,'Defenders:' ,horizontalalignment = 'left',fontsize = info_text,color = check_colour)
        plt.text(width+13,height-diff,'Yes' ,horizontalalignment = 'left',fontsize = info_text,color = 'green')
        diff += 3
        
    if stipulation == 'y':
        rand_stip  = random_stipulation()
        stip_colour = 'darkblue'
    else:
        rand_stip = 'No'
        stip_colour = 'red'
    
    if len(positions) < len(name_list):
        return RandomHat(names,choice,goalkeeper,defenders,stipulation,photos)
    
    while len(allocation) < names_len:
        random_name, random_pos = random.choice(name_list), random.choice(positions)
        allocation.append([random_name,random_pos])
        positions.remove(random_pos); name_list.remove(random_name)
    
    diff += 3
    
    if rand_stip == 'Choose Position':
        plt.text(width+1,height-diff,'Stipulation:',horizontalalignment = 'left',fontsize = info_text,color = check_colour)        
        plt.text(width+14,height-diff,rand_stip + ':',horizontalalignment = 'left',fontsize = info_text,color = stip_colour)
        plt.text(width+32,height-diff,random.choice(['Your own!','Next player!']),horizontalalignment = 'left',fontsize = info_text,color = stip_colour)
        diff+=3
        num = 1
        for i in allocation:
            plt.text(width+1,height-diff, str(num) + '. ',horizontalalignment = 'left',fontsize = name_text,color = 'black')
            plt.text(width+4,height-diff, str.upper(i[0][0]) + str.lower(i[0][1:len(i[0])+1]),horizontalalignment = 'left',fontsize = name_text,color = name_colour)
            diff += 2.5
            num += 1
        allocation = []
    else:
        plt.text(width+1,height-diff,'Stipulation:',horizontalalignment = 'left',fontsize = info_text,color = check_colour)        
        plt.text(width+14,height-diff,rand_stip,horizontalalignment = 'left',fontsize = info_text,color = stip_colour)
        diff += 3
    
    #Title
    plt.title(formation[0], fontsize = formation_text)
    
    fig.set_facecolor('w')
    form_plot(formation,allocation)
    draw_pitch(pitch_color='darkgreen', 
               line_color="black",
               ax=ax)
        
    if photos == 'y':
        #Plotting Faces
        for pos in form_plot(formation,allocation):
            for allo in allocation:
                if pos[0] == allo[1]:
                    for path in paths:
                        if allo[0] in path:
                            isFile = os.path.isfile(path)
                            if isFile == True:
                                ab = AnnotationBbox(getImage(path, zoom = 1/Image.open(path).size[0] * marker_size * 1.1), (pos[1][0], pos[1][1]), frameon=False)
                                ax.add_artist(ab)
      
    plt.savefig('/Users/thomas795/Library/Mobile Documents/com~apple~CloudDocs/coding/proclubs/rhh/rhh_app/Formation.jpeg', dpi = 500, bbox_inches = 'tight')
    plt.savefig('/Users/thomas795/desktop/Formation.jpeg', dpi = 500, bbox_inches = 'tight')

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

stipulation = str.lower(input('Would you like to use a stipulation? [y/n]: ' ))
while stipulation not in y_n:
    print('Try again...')
    stipulation = str.lower(input('Would you like to use a stipulation? [y/n]: ' ))

photos = str.lower(input('Would you like to use player images? [y/n]: ' ))
while photos not in y_n:
    print('Try again...')
    photos = str.lower(input('Would you like to use a stipulation? [y/n]: ' ))



#========================================================================================================================================Execution                   
RandomHat(players
          ,choice = choice
          ,goalkeeper = goalkeeper
          ,defenders = defenders
          ,stipulation = stipulation
          ,photos = photos)
