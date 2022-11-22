#
# fomap_gen_file_desert.py
# for FOnline engine maps (.fomap)
# tested in FOnline: 2238 Mapper, version 1.29.0
#

from random import *


########################
##  Initial Settings  ##
########################
print("This program will write a .fomap to current directory.")
print("If the name you choose already exists, it will overwrite that file.\n")
filename = input("Enter name of map, not including extension: ")
ext = '.fomap'

MaxHexX = int(input("Enter X-length of map: "))
MaxHexY = int(input("Enter Y-length of map: "))

print("Writing map file...")
f = open(filename+ext, 'w')



####################
##  Makes Header  ##
####################
#(lines 1 to 15)
f.write("[Header]\n")
f.write("Version              4\n")
f.write("MaxHexX              "+str(MaxHexX)+'\n')
f.write("MaxHexY              "+str(MaxHexY)+'\n')
f.write("WorkHexX             "+str(MaxHexX//2)+'\n')
f.write("WorkHexY             "+str(MaxHexY//2)+'\n')
f.write("ScriptModule         map_encounter\n")
f.write("ScriptFunc           map_init\n")
f.write("NoLogOut             0\n")
f.write("Time                 -1\n")
f.write("DayTime              300  600  1140 1380\n")
f.write("DayColor0            18  18  53\n")
f.write("DayColor1            128 128 128\n")
f.write("DayColor2            103 95  86\n")
f.write("DayColor3            51  40  29\n\n")



###################
##  Makes Tiles  ##
###################
f.write("[Tiles]\n")

if (MaxHexX%2 == 0):
    MaxHexX += 1

x_col = 0 
y_col = 0
tile_frm_type = "edg" #desert tiles, randomly placed
tile_frm_num  = 5003  #desert tiles

while (y_col <= MaxHexY - 2):
    f.write("tile       ")
    f.write(str(x_col) + "    ");
    x_col += 2;
    f.write(str(y_col) + "              ")
   
    if (x_col >= MaxHexX - 2):
        y_col += 2
        x_col = 0

    tile_frm_num = randrange(5000, 5008)
    f.write("art\\tiles\\"+ tile_frm_type + str(tile_frm_num) + ".frm\n")



#####################
##  Makes Objects  ##
#####################
f.write("[Objects]\n")

#tree7 = 1820
#tree8 = 1821
#tree9 = 1822
#tall big tree is 9730
#less tall big tree is 9731
#apple tree is 9910
#weed01 is 2102
#weed02 is 2103
#weed03 is 2104
#weed04 is 2105
#weed24 is 2125
#weed26 is 2127


#Makes Trees:
MapObjType = 1
TREE_NUM = 100
for i in range(0, TREE_NUM):
    MapX_rand = randrange(MaxHexX)
    MapY_rand = randrange(MaxHexY)
    ProtoId   = randrange(1820, 1823) #currently trees, random
   
    f.write("MapObjType           " + str(MapObjType) + '\n' )
    f.write("ProtoId              " + str(ProtoId)    + '\n' )
    f.write("MapX                 " + str(MapX_rand)  + '\n' )
    f.write("MapY                 " + str(MapY_rand) +'\n\n' )




#Mob Spawn is 21001, MapObjType 1.
   
"""
MapObjType           1
ProtoId              1820
MapX                 83
MapY                 41
ScriptName           prod_tree_firewood
FuncName             _EncTree
"""


###########################
##  Map Border Creation  ##
###########################
""" # these are Scroll Blockers:
MapObjType           2
ProtoId              4012
MapX                 145
MapY                 108
""" #


x_hex = int(MaxHexX/2)
y_hex = 0
hex_counter = 0

#Left Vertical Boundary:
while (x_hex < MaxHexX - 2 ):
    f.write("MapObjType           "+"2\n"       )
    f.write("ProtoId              "+"4012\n"    )
    f.write("MapX                 "+str(x_hex)+'\n')
    f.write("MapY                 "+str(y_hex)+'\n\n')
    if   (hex_counter == 0):
        hex_counter += 1
        x_hex += 1
        y_hex += 1
    elif (hex_counter == 1):
        hex_counter += 1
        y_hex += 1
    elif (hex_counter == 2):
        hex_counter += 1
        x_hex += 1
    elif (hex_counter == 3):
        y_hex += 1
        hex_counter = 0

#note: upper right corner seems to be about at MaxHexY/3

       
#Top Horizontal Boundary:
x_hex = int(MaxHexX/2)
y_hex = 1
hex_counter = 0
while (x_hex > 0):
    f.write("MapObjType           "+"2\n"       )
    f.write("ProtoId              "+"4012\n"    )
    f.write("MapX                 "+str(x_hex)+'\n')
    f.write("MapY                 "+str(y_hex)+'\n\n')
    if   (hex_counter == 0):
        x_hex -= 1
        y_hex += 1
        hex_counter += 1
    elif (hex_counter == 1):
        x_hex -= 1
        hex_counter = 0

#Right Vertical Boundary:
hex_counter = 0
while (y_hex < MaxHexY - 2):
    f.write("MapObjType           "+"2\n"       )
    f.write("ProtoId              "+"4012\n"    )
    f.write("MapX                 "+str(x_hex)+'\n')
    f.write("MapY                 "+str(y_hex)+'\n\n')
    if   (hex_counter == 0):
        hex_counter += 1
        x_hex += 1
        y_hex += 1
    elif (hex_counter == 1):
        hex_counter += 1
        y_hex += 1
    elif (hex_counter == 2):
        hex_counter += 1
        x_hex += 1
    elif (hex_counter == 3):
        y_hex += 1
        hex_counter = 0

#Bottom Horizontal Boundary:
hex_counter = 0
while (x_hex < MaxHexX - 2):
    f.write("MapObjType           "+"2\n"       )
    f.write("ProtoId              "+"4012\n"    )
    f.write("MapX                 "+str(x_hex)+'\n')
    f.write("MapY                 "+str(y_hex)+'\n\n')
    if   (hex_counter == 0):
        x_hex += 1
        y_hex -= 1
        hex_counter += 1
    elif (hex_counter == 1):
        x_hex += 1
        hex_counter = 0

f.close()
print("Done. Press Enter to quit.", end=""); input();

###
