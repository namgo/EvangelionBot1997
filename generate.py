from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import random
'''
CSVs obtained from epguides.com
'''

# deprecated function
def gen_template():
    img = Image.new(mode='RGB', size=(400,400), color=(0,0,0))
    draw = ImageDraw.Draw(img)
    font_0 = ImageFont.truetype('LiberationSerif-Bold.ttf', 50)
    font_1 = ImageFont.truetype('LiberationSerif-Bold.ttf', 56)
    draw.text((4,0), "NEON",(255,255,255), font=font_0)
    draw.text((4,38), "GENESIS",(255,255,255), font=font_0)
    draw.text((4,76), "EVANGELION",(255,255,255), font=font_1)
    img.save('title.png')

def draw_text():
    with open('all.lst', 'r') as f:
        episode_name = random.choice(f.readlines())
        
    episode_number = random.randint(1,26)
    img = Image.open('title.jpg')
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype('LiberationSerif-Regular.ttf', 60)
    episode_num_font = ImageFont.truetype('DejaVuSans-Bold.ttf', 50)
    draw.text((4,500), "EPISODE:{}".format(episode_number), (255,255,255), font=episode_num_font)
    draw.text((4,600), episode_name, (255,255,255), font=title_font)
    img.save('episode.png')



draw_text()
