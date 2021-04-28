from PIL import Image , ImageEnhance , ImageFilter
import os

# img1 = Image.open("tiger.png")
# img1.show("tiger.pdf")

# resize  = (250,250)
# img1.thumbnail(resize)
# img1.save("small.png")

# for item in os.listdir():
#     if item.endswith(".png"):
#         img1 = Image.open(item)
#         imagename,extension = os.path.splitext(item)
#         img1.save(f"{imagename}.jpg")

# img1 = Image.open("tiger.png")
# enhancer = ImageEnhance.Sharpness(img1) #imageinhance is module and sharpness is class
# enhancer.enhance(2).save("tiger_edit.png")  #0----blurry.......1---original .........2----incerase sharpness

# img1= Image.open("tiger.png")
#  enhancer = ImageEnhance.Color(img1)           #brightness...
#enhancer.enhance(4).save("color_tiger.png")

# img1.filter(ImageFilter.GaussianBlur(radius = 4)).save("blurtiger.png")