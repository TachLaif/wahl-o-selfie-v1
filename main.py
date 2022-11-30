# Copyright (C) 2022 - Benjamin Hupf
#
# Wahl-O-Selfie ver. 1 (https://github.com/TachLaif/wahl-o-selfie-v1)
# - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 30.11.2022
#
# This work is made available under the GNU Affero General Public License v3.0
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

__version__ = 1.0

import face_recognition
from PIL import Image, ImageDraw, ImageOps
from keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import os

model = load_model('./trained_model/keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


picture = face_recognition.load_image_file('testimage.jpg')
face_locations = face_recognition.face_locations(picture)
pil_image = Image.fromarray(picture)

if len(face_locations) < 1:
    print('No face found. Please use a picture with an easy to see face.')
elif len(face_locations) > 1:
    print('More than one face found. Please use a picture with only one face.')
    #for(top, right, bottom, left) in face_locations:
    #    draw = ImageDraw.Draw(pil_image)
    #    draw.rectangle(((left, top), (right, bottom)), outline = (255, 0, 0), width = 4)
    #    pil_image.save("error.jpg")
    #    del draw
else:
    top, right, bottom, left = face_locations[0]
    face_image = picture[top:bottom, left:right]
    ai_image = Image.fromarray(face_image)
    size = (224, 224)
    prepared_ai_image = ImageOps.fit(ai_image, size, Image.ANTIALIAS)
    image_array = np.asarray(prepared_ai_image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    AFD = prediction[0, 0]
    CDU_CSU = prediction[0, 1]
    Gruenen = prediction[0, 2]
    Linke = prediction[0, 3]
    FDP = prediction[0, 4]
    SPD = prediction[0, 5]
    max = max(AFD, CDU_CSU, Gruenen, Linke, FDP, SPD)
    AFD_percent = round(AFD * 1000) / 10
    CDU_CSU_percent = round(CDU_CSU * 1000) / 10
    Gruenen_percent = round(Gruenen * 1000) / 10
    Linke_percent = round(Linke * 1000) / 10
    FDP_percent = round(FDP * 1000) / 10
    SPD_percent = round(SPD * 1000) / 10

    print("AFD: " + str(AFD_percent) + "%")
    print("CDU/CSU: " + str(CDU_CSU_percent) + "%")
    print("Die Grünen: " + str(Gruenen_percent) + "%")
    print("Linke: " + str(Linke_percent) + "%")
    print("FDP: " + str(FDP_percent) + "%")
    print("SPD: " + str(SPD_percent) + "%")

    top, right, bottom, left = face_locations[0]
    draw = ImageDraw.Draw(pil_image)
    draw.rectangle(((left, top), (right, bottom)), outline = (255, 0, 0), width = 4)
    print("----------------------------------------")
    if max == AFD: party = "AFD"
    if max == CDU_CSU: party = "CDU/CSU"
    if max == Gruenen: party = "Die Grünen"
    if max == Linke: party = "Die Linke"
    if max == FDP: party = "FDP"
    if max == SPD: party = "SPD"
    print(party) 
    partys = [
    'AFD - ' + str(AFD_percent) + '%', 
    'CDU/CSU - ' + str(CDU_CSU_percent) + '%', 
    'Die Grünen - ' + str(Gruenen_percent) + '%', 
    'Die Linke - ' + str(Linke_percent) + '%', 
    'FDP - ' + str(FDP_percent) + '%',
    'SPD - ' + str(SPD_percent) + '%']
    colors = ("blue", "black", "green", "red", "yellow", "red")
    data = [AFD_percent, CDU_CSU_percent, Gruenen_percent, Linke_percent, FDP_percent, SPD_percent]
    fig, ax = plt.subplots()
    y_pos = np.arange(len(partys))
    ax.barh(y_pos, data, align="center", color=colors)
    ax.set_yticks(y_pos, labels=partys)
    
    ax.invert_yaxis()
    ax.set_xlabel('Procent')
    ax.set_title('Wahl-O-selfie')
    plt.savefig('graph.png', bbox_inches = "tight")
    #text_width, text_height = draw.textsize(party)
    #draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (0, 0, 0), outline = (0, 0, 0))
    #draw.text((left + 6, bottom - text_height - 5), party, fill=(255, 255, 255))
    w, h = pil_image.size
    if w < 653:
        img = Image.new(mode = 'RGB', size = (653, h + 455), color="white")
    else:
        img = Image.new(mode = 'RGB', size = (w, h + 455), color="white")
    img_w, img_h = img.size
    img.paste(pil_image, (round((img_w - w) / 2), 0))
    graph = Image.open('graph.png')
    img.paste(graph, (round((img_w - 653) / 2), h))
    img.save('result.jpg')    
    #pil_image.save('processed.jpg')
    text_width, text_height = draw.textsize('Die Grünen - 100.0%')
    draw.rectangle(((left,(bottom + 5) + (text_height * 5 + 5)), (right, bottom)), fill = (0, 0, 0), outline = (0, 0, 0))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 70)), 'AFD - ' + str(AFD_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 60)), 'CDU/CSU - ' + str(CDU_CSU_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 50)), 'Die Grünen - ' + str(Gruenen_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 40)), 'Die Linke - ' + str(Linke_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 30)), 'FDP - ' + str(FDP_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 20)), 'SPD - ' + str(SPD_percent) + '%', fill=(255, 255, 255))
    pil_image.save('result2.jpg')
    del draw
    os.remove('graph.png')
    img.show()
#pil_image.show()
#ai_image.show()
#ai_image.save('processed.jpg')