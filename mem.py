from PIL import Image, ImageDraw, ImageFont

def generate_meme(path,txt1,txt2):
    im1 = Image.open("mem-lgmsh2.jpg")
    im2 = Image.open(path)
    im2=im2.resize((753,424))
    im1.paste(im2,(264,53))
    im1 = im1.convert('RGB')
    imDraw = ImageDraw.Draw(im1)
    f = ImageFont.truetype("Ubuntu-Regular.ttf", 80)
    l=f.getlength(txt1)
    imDraw.text(((1277-l)/2,509),txt1,font=f)
    f = ImageFont.truetype("Ubuntu-Regular.ttf", 50)
    l=f.getlength(txt2)
    imDraw.text(((1277-l)/2,617),txt2,font=f)
    im1.save("test.jpeg",mod="jpeg")
    im1.show()

path=input()
txt1=input()
txt2=input()
generate_meme(path,txt1,txt2)

