import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

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