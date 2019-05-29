from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import base64
import logging
import math
from google.cloud import firestore
from google.cloud import storage
from io import BytesIO
import csv
import random
import facebook

BUCKET_NAME = 'evangelion-images'

def post_image(img):
    saved = BytesIO()
    img.save(saved, format='PNG')
    saved.seek(0)
    with open('token') as f:
        token = f.read()
    graph = facebook.GraphAPI(access_token=token)
    graph.put_photo(image=saved.read())
    return True

def list_blobs_to_db():
    logging.info('starting list blobs to db')
    store = storage.Client()
    bucket = store.get_bucket(BUCKET_NAME)
    blobs = bucket.list_blobs()
    blob_names = [blob.name for blob in blobs]
    to_db = {}
    for i in range(len(blob_names)):
        to_db.update({str(i): blob_names[i]})
    db = firestore.Client()
    db.collection(u'files').document('list').set(to_db)
    logging.info('finished list blobs to db')

def get_random_document(db, collection_name):
    return random.choice(
        [
            doc.to_dict() for doc in db.collection(collection_name).stream()
        ]
    )

def get_subtitle_text():
    db = firestore.Client()
    choice = get_random_document(db, 'subtitles')
    subtitle = choice[random.choice(list(choice.keys()))]
    logging.info('subtitle selected', subtitle)
    return subtitle

def get_episode_name():
    db = firestore.Client()
    choice = get_random_document(db, u'titles')
    episode_name = choice[random.choice(list(choice.keys()))]
    logging.info('episode selected', episode_name)
    return episode_name

def get_random_file():
    store = storage.Client()
    bucket = store.get_bucket(BUCKET_NAME)

    db = firestore.Client()
    filenames = db.collection(u'files').document('list').get().to_dict()
    choice = random.choice(list(filenames.keys()))
    blob = bucket.get_blob(filenames[choice])
    logging.info("image selected", filenames[choice])
    f = BytesIO()
    blob.download_to_file(f)
    return f


def generate_title_card(data, context):
    episode_number = random.randint(1,26)
    img = Image.open('title.jpg')
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype('LiberationSerif-Regular.ttf', 60)
    episode_num_font = ImageFont.truetype('DejaVuSans-Bold.ttf', 50)
    draw.text((4,500), "EPISODE:{}".format(episode_number), (255,255,255), font=episode_num_font)
    draw.text((4,600), get_episode_name(), (255,255,255), font=title_font)
    post_image(img)

def generate_episode_frame(data, context):
    img = Image.open(get_random_file())
    draw = ImageDraw.Draw(img)
    font_size = 24
    subtitle_font = ImageFont.truetype('DejaVuSans.ttf', font_size)
    texts = get_subtitle_text().split('\n')
    longest = max(texts, key=len)
    w, h = draw.textsize(longest, font=subtitle_font)
    x = int(img.size[0] - w) / 2
    y = img.size[1] - 60
    for text in texts:
        for i in [-2,-1,1,2]:
            for j in [-2,-1,1,2]:
                draw.text((x+i,y+j), text, (0,0,0), font=subtitle_font)
        draw.text((x,y), text, (255,255,204), font=subtitle_font)
        y += font_size
    post_image(img)

#generate_title_card()
# get_episode_frame()
# list_blobs_to_db()
#get_random_filename()
#generate_episode_frame()
# get_subtitle_text()

