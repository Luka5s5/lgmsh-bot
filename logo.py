import random
from PIL import Image, ImageDraw, ImageFont
import os


def create_picture():
    coolors = [[(249, 231, 231), (222, 214, 214), (210, 203, 203), (173, 160, 166), (125, 147, 138)], [(236, 145, 216), (255, 170, 234), (255, 190, 239), (255, 211,   218), (233, 211, 208)], [(203, 72, 183), (46, 45, 77), (51, 115, 87), (109, 159, 113), (228, 227, 211)], [(109, 163, 77), (86, 68, 93), (84, 134, 135), (143, 188, 148), (197, 233, 155)], [(240, 162, 2), (241, 136, 5), (217, 93, 57), (14, 20, 40), (123, 158, 137)], [(140, 255, 152), (170, 217, 34), (111, 124, 18), (72, 53, 25), (0, 0, 0)], [(71, 229, 188), (129, 228, 218), (174, 207, 223), (159, 159, 173), (147, 116, 138)], [(143, 148, 145), (188, 163, 172), (229, 206, 220), (243, 234, 244), (234, 221, 225)], [(48, 54, 47), (98, 88, 52), (165, 145, 50), (255, 251, 219), (218, 116, 34)], [(9, 8, 9), (244, 0, 0), (244, 78, 63), (244, 121, 107), (244, 153, 141)], [(117, 119, 128), (210, 204, 161), (56, 119, 128), (219, 212, 211), (232, 49, 81)], [(44, 54, 63), (231, 90, 124), (242, 245, 234), (214, 219, 210), (187, 199, 164)], [(130, 255, 158), (169, 251, 195), (181, 148, 182), (147, 95, 167), (155, 72, 155)], [(219, 205, 198), (234, 215, 209), (221, 153, 187), (123, 80, 111), (31, 26, 56)], [(232, 235, 228), (210, 213, 221), (184, 186, 207), (153, 154, 198), (121, 128, 113)], [(226, 252, 239), (155, 40, 123), (92, 22, 78), (64, 32, 57), (23, 15, 17)], [(152, 193, 217), (105, 105, 179), (83, 58, 123), (75, 36, 74), (37, 23, 26)], [(86, 65, 56), (46, 134, 171), (246, 245, 174), (245, 247, 73), (242, 66, 54)], [(86, 71, 135), (219, 203, 216), (242, 253, 255), (154, 212, 214), (16, 25, 53)], [(4, 42, 43), (94, 177, 191), (205, 237, 246), (239, 123, 69), (216, 71, 39)], [(97, 97, 99), (68, 255, 210), (135, 246, 255), (218, 245, 255), (255, 191, 160)], [(41, 23, 17), (71, 75, 36), (95, 187, 151), (141, 220, 164), (99, 50, 110)], [(124, 254, 240), (107, 255, 184), (44, 234, 163), (40, 150, 90), (42, 96, 65)], [(246, 81, 29), (255, 180, 0), (0, 166, 237), (127, 184, 0), (13, 44, 84)], [(191, 215, 234), (145, 174, 193), (80, 140, 164), (10, 135, 84), (0, 79, 45)], [(0, 0, 0), (12, 24, 33), (27, 42, 65), (50, 74, 95), (204, 201, 220)], [(150, 173, 200), (215, 255, 171), (252, 255, 108), (216, 157, 106), (109, 69, 76)], [(239, 121, 138), (247, 169, 168), (97, 63, 117), (229, 195, 209), (152, 139, 142)], [(88, 107, 164), (50, 67, 118), (245, 221, 144), (246, 142, 95), (247, 108, 94)], [(57, 64, 83), (78, 74, 89), (110, 99, 98), (131, 144, 115), (124, 174, 122)], [(249, 224, 217), (230, 219, 208), (125, 97, 103), (117, 79, 91), (93, 73, 84)], [(21, 30, 63), (3, 0, 39), (242, 243, 217), (220, 158, 130), (193, 110, 112)], [(26, 20, 35), (61, 49, 74), (104, 71, 86), (150, 112, 91), (171, 132, 118)], [(199, 232, 243), (191, 154, 202), (142, 65, 98), (65, 57, 62), (237, 162, 192)], [(156, 255, 250), (172, 243, 157), (176, 197, 146), (169, 124, 115), (175, 62, 77)], [(230, 57, 70), (241, 250, 238), (168, 218, 220), (69, 123, 157), (29, 53, 87)], [(66, 54, 41), (79, 93, 47), (125, 126, 117), (176, 178, 184), (207, 214, 234)], [(211, 97, 53), (127, 176, 105), (236, 228, 183), (230, 170, 104), (2, 2, 11)], [(242, 84, 91), (169, 63, 85), (25, 50, 60), (243, 247, 240), (140, 94, 88)], [(23, 190, 187), (46, 40, 42), (205, 83, 52), (237, 184, 139), (250, 216, 214)], [(205, 247, 246), (143, 184, 222), (154, 148, 188), (155, 80, 148), (106, 96, 92)], [(0, 0, 0), (47, 16, 0), (98, 27, 0), (148, 86, 0), (199, 80, 0)], [(204, 218, 209), (156, 174, 169), (120, 133, 133), (111, 104, 102), (56, 48, 46)], [(117, 221, 221), (80, 137, 145), (23, 42, 58), (0, 67, 70), (9, 188, 138)], [(237, 212, 178), (208, 169, 143), (77, 36, 61), (202, 194, 181), (236, 220, 201)], [(226, 241, 175), (227, 216, 136), (132, 113, 79), (90, 58, 49), (49, 35, 30)], [(95, 15, 64), (154, 3, 30), (251, 139, 36), (227, 100, 20), (15, 76, 92)], [(187, 190, 100), (142, 85, 114), (242, 247, 242), (188, 170, 153), (68, 56, 80)], [(152, 68, 71), (173, 217, 244), (71, 108, 155), (70, 140, 152), (16, 20, 25)], [(216, 203, 199), (204, 63, 12), (154, 109, 56), (51, 103, 59), (25, 35, 26)]]

    sun_radius = [290, 288]

    fond_fonts = os.listdir("fonts")
    DENSITY = random.randint(24, 64)
    CANVAS_SIZE = 800
    text = "ЛГМШ"
    font_path = f"fonts/{random.choice(fond_fonts)}"
    font = ImageFont.truetype(font_path, 120, encoding="utf-8")
    
    #choose a color
    random_colors_set = random.choice(coolors)[:]
    random.shuffle(random_colors_set)
    dark_set = list(map(sum, random_colors_set))

    color_of_backside = random_colors_set[dark_set.index(min(dark_set))]
    del random_colors_set[dark_set.index(min(dark_set))], dark_set[dark_set.index(min(dark_set))]
    
    color_of_font = random_colors_set[dark_set.index(max(dark_set))]
    del random_colors_set[dark_set.index(max(dark_set))], dark_set[dark_set.index(max(dark_set))]

    color_of_lines = random_colors_set[0], random_colors_set[1], random_colors_set[2]

    img = Image.new('RGB', (CANVAS_SIZE, CANVAS_SIZE), color_of_backside)
    draw = ImageDraw.Draw(img)
    
    #ornament pattern
    for row in range(DENSITY):
        for col in range(DENSITY):
            draw_line(row, col, CANVAS_SIZE, DENSITY, draw, color_of_lines)
    
    f = random.randint(-10, 10)
    
    #sun and text 138
    index_of_sun_pattern = random.randint(0, 1)
    size_of_font = font.getsize(text)
    size_of_sun = int(sum(map(lambda x: x ** 2, size_of_font)) ** (1 / 2) * 512 / sun_radius[index_of_sun_pattern]) + size_of_font[1] // 2
    sun = Image.open(f"sun{index_of_sun_pattern}.png").resize((size_of_sun, size_of_sun), Image.Resampling.LANCZOS)
    
    fontimage = Image.new('L', (size_of_sun, size_of_sun))
    text_w, text_h = fontimage.size
    fontimage.paste(255, box=(0, 0), mask=sun)
    ImageDraw.Draw(fontimage).text((text_w // 2, text_h // 2), text, anchor="mm", fill=255, font=font)
    fontimage = fontimage.rotate(f, resample=Image.BICUBIC, expand=True)
    img.paste(color_of_font, box=((CANVAS_SIZE - text_w) // 2, (CANVAS_SIZE - text_h) // 2), mask=fontimage)
            
    #save the picture
    img.save(f"photos/LGMSH.png")
    return "photos/LGMSH.png"
    
    
def draw_line(row, col, CANVAS_SIZE, DENSITY, draw, color_of_lines):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY),
        (row * CANVAS_SIZE / DENSITY)
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY),
        ((row + 1) * CANVAS_SIZE / DENSITY)
    )
    lower_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY),
        (row * CANVAS_SIZE / DENSITY)
    )
    upper_left = (
        (col * CANVAS_SIZE / DENSITY),
        ((row + 1) * CANVAS_SIZE / DENSITY)
    )

    res = random.randint(0, 1)

    if res == 0:
    	draw.line((upper_left[0], upper_left[-1], lower_right[0], lower_right[-1]), fill=random.choice(color_of_lines), width=3)
    else:
    	draw.line((lower_left[0], lower_left[-1], upper_right[0], upper_right[-1]), fill=random.choice(color_of_lines), width=3)
    
    
if __name__ == "__main__":
    print(create_picture())