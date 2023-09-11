from PIL import Image, ImageDraw
import os

class imagejoin:

  def joinPngs(output: str, folder: str, pngSize: int, drawRegion: bool) -> Image:
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    # Prepare png and search for highest/lowest region coords
    pngs = {}
    for png in os.listdir(folder):
      coords = png.rstrip('.png')
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

    # Create new Image with expected size
    fullimg = Image.new('RGB', (width*pngSize, height*pngSize), (255,255,255))
    for y in range(minY, maxY+1):
      _y = y - minY

      for x in range(minX, maxX+1):
        _x = x - minX

        if f'{x},{y}' in pngs:
          img = Image.open(os.path.join(folder, pngs[f'{x},{y}']))
          if drawRegion:
            draw = ImageDraw.Draw(img)
            draw.line((0,0, pngSize,0), fill='red', width=2)
            draw.line((0,0, 0,pngSize), fill='red', width=2)
            draw.text((5,3), f'r {x},{y}', fill='red')

          fullimg.paste(img, (512*_x,512*_y))

    fullimg.save(output)


