from PIL import Image
import os

jdirectory = "day"
pngSize = 512

minX = 0
maxX = 0
minY = 0
maxY = 0

pngs = {}

for png in os.listdir(jdirectory):
    coords = png[:-4]
    x, y = coords.split(',')
    x=int(x)
    y=int(y)
    pngs[coords] = png

    minX = minX if x > minX else x
    maxX = maxX if x < maxX else x
    minY = minY if y > minY else y
    maxY = maxY if y < maxY else y

width = maxX - minX + 1
height = maxY - minY + 1

print(minX, maxX, " - ", minY, maxY, " - ", width, height)

Matrix = [['-' for y in range(width)] for x in range(height)]

for y in range(minY, maxY+1):
    _y = y - minY
    #Matrix[_y] = list('-'*width)

    for x in range(minX, maxX+1):
        _x = x - minX

        if f'{x},{y}' in pngs:
            Matrix[_y][_x] = 'X'


for line in Matrix:
    print(''.join(line))


wholemap = Image.new('RGB', (width*pngSize, height*pngSize), (255,255,255))

# Imaging
for y in range(minY, maxY+1):
    _y = y - minY

    for x in range(minX, maxX+1):
        _x = x - minX

        if f'{x},{y}' in pngs:
            img = Image.open(os.path.join(jdirectory, pngs[f'{x},{y}']))

            wholemap.paste(img, (512*_x,512*_y))
        

wholemap.save('result.png', 'PNG')




exit()

#Read the two images
image1 = Image.open('images/elephant.jpg')
image1.show()
image2 = Image.open('images/ladakh.jpg')
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("images/merged_image.jpg","JPEG")
new_image.show()

