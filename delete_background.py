import PIL
from PIL import Image

img = Image.open('F:/FREELANCER/DESIGN GRAFIS/ICON/VECTOR/WEATHER/INDONESIA_MAP.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("F:/FREELANCER/DESIGN GRAFIS/ICON/VECTOR/WEATHER/INDONESIA_MAP_1.png", "PNG")
   
print "FINISH_IMAGE_FFMC"
