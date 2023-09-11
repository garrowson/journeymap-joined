import imagejoin
import os

jdirectory = "D:\\Programme\\Minecraft\\Instances\\Forge1.19.2-RK (1)\\journeymap\\data\\mp\\1~19~2~RKServer~reloaded~_74c389a9~2f41~4b50~a751~8f459cef4a62\\DIM0\\day"
pngSize = 512

imagejoin.imagejoin.joinPngs(output="result.png", folder=jdirectory, pngSize=pngSize, drawRegion=True)
