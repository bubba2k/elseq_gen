from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random as rnd


#Welcome to bubba2k's elseq art generator



#config

#filename prefix and number of files to be generated
output_prefix = '5tile'
output_n = 10

#image size in px (always square), and amount of tiles
size = 1200
tiles = 5

#colors (standard: canvas=(255,255,255), shape=(35,31,32)
canvas_color = (255,255,255)
shape_color = (35,31,32)

#if use_custom_scales = False, accurate Elseq scales are used
use_custom_scales = False
scale_circle_tiny =      1/3
scale_circle_small =     2/3
scale_circle_medium =    3/3 * 0.95
scale_circle_large =     1.08
scale_circle_huge =      0.975
scale_square =           0.95

#probability of each shape getting drawn per tile
prob_circle_tiny =      0.7
prob_circle_small =     0.7
prob_circle_medium =    0.3
prob_circle_large =     0.1
prob_circle_huge =      0.05
prob_square =           0.5

#/config




if use_custom_scales == False:
    scale_circle_tiny =      1/3
    scale_circle_small =     2/3
    scale_circle_medium =    3/3 * 0.95
    scale_circle_large =     1.08
    scale_circle_huge =      0.975
    scale_square =           0.95

tilesize = size // tiles
tilelist = []
cornerpoints  = []
for i in range(tiles):
    for j in range(tiles):
        tilelist.append([(tilesize*i, tilesize*j), (tilesize*i + tilesize, tilesize*j+tilesize)])

for i in range(tiles):
    for j in range(tiles):
        if 0 < i < tiles+1 and 0 < j < tiles+1:
            cornerpoints.append([tilesize*i, tilesize*j])
            
            

def circle_tiny(drawer,index):
    if rnd.random() < prob_circle_tiny:
        tile = tilelist[index]
        a, b = tile[0], tile[1]
        scale = scale_circle_tiny
        offset = (tilesize - int(tilesize * scale)) // 2
        ax, ay = (np.add(a, offset))
        bx, by = (np.add(b, -offset))
        coords = (ax,ay,bx,by)
        drawer.ellipse(coords,shape_color)

def circle_small(drawer,index):
    if rnd.random() < prob_circle_small:
        tile = tilelist[index]
        a, b = tile[0], tile[1]
        scale = scale_circle_small
        offset = (tilesize - int(tilesize * scale)) // 2
        ax, ay = (np.add(a, offset))
        bx, by = (np.add(b, -offset))
        coords = (ax,ay,bx,by)
        drawer.ellipse(coords,shape_color)

def circle_medium(drawer,index):
    if rnd.random() < prob_circle_medium:
        tile = tilelist[index]
        a, b = tile[0], tile[1]
        scale = scale_circle_medium
        offset = (tilesize - int(tilesize * scale)) // 2
        ax, ay = (np.add(a, offset))
        bx, by = (np.add(b, -offset))
        coords = (ax,ay,bx,by)
        drawer.ellipse(coords,shape_color)

def circle_large(drawer,index):
    if rnd.random() < prob_circle_large:
        tile = tilelist[index]
        a, b = tile[0], tile[1]
        scale = scale_circle_large
        offset = (tilesize - int(tilesize * scale)) // 2
        ax, ay = (np.add(a, offset))
        bx, by = (np.add(b, -offset))
        coords = (ax,ay,bx,by)
        drawer.ellipse(coords,shape_color)

def circle_huge(drawer,index):
    if rnd.random() < prob_circle_huge:
        center = cornerpoints[index]
        centerx, centery = center[0], center[1]
        offset = tilesize * scale_circle_huge
        ax, ay = centerx-offset, centery-offset
        bx, by = centerx+offset, centery+offset
        
        coords = (ax,ay,bx,by)
        drawer.ellipse(coords,shape_color)

def square(drawer,index):
    if rnd.random() < prob_square:
        tile = tilelist[index]
        a, b = tile[0], tile[1]
        scale = scale_square
        offset = (tilesize - int(tilesize * scale)) // 2
        ax, ay = (np.add(a, offset))
        bx, by = (np.add(b, -offset))
        coords = (ax,ay,bx,by)
        drawer.rectangle(coords,shape_color)


def main():
    
    
    for i in range(output_n):
        canvas = Image.new('RGB', (size, size), canvas_color)
        draw = ImageDraw.Draw(canvas, 'RGB')
        for j in range(tiles*tiles):
            circle_tiny(draw,j)
            circle_small(draw,j)
            circle_medium(draw,j)
            circle_large(draw,j)
            square(draw,j)
        for k in range(len(cornerpoints)):
            circle_huge(draw,k)
        
        filtered = canvas.filter(ImageFilter.SMOOTH_MORE)
        filtered.save(output_prefix + str(i) + '.png')

    #print(tilelist)
    #print(tilelist_large)

main()
