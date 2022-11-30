# Wahl-O-Selfie - v1
<a href="https://www.python.org/downloads/release/python-3107/"><img src="https://img.shields.io/badge/python-3.10.7-success?style=for-the-badge&logo=python&logoColor=white"></img></a>
<img src="https://img.shields.io/badge/Last%20update-30.11.2022-blue?style=for-the-badge"></img>
<a href="https://github.com/TachLaif/Discord-bot-for-SkyBlock-graph/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TachLaif/Discord-bot-for-SkyBlock-graph?style=for-the-badge"></img></a>

## Description
Wahl-O-Selfie (v1) is using a self-trained machine learning model which categorizes human faces into (german) political partys similar to "<a href="https://www.wahl-o-mat.de">Wahl-O-Mat</a>[^1]".


## Table of Contents
- <a href="#description">Description</a>
- <a href="#table-of-contents">Table of Contents</a>
- <a href="#how-to-install">How to install</a>
  - <a href="#installing-face_recognition-for-windows2">Installing face_recognition (for Windows)</a>
  - <a href="#installing-tensorflow-keras3">Installing TensorFlow Keras</a>
  - <a href="#installing-the-other-dependencies">Installing the other dependencies</a>
  - <a href="#installing-wahl-o-selfie">Installing Wahl-O-Selfie</a>
- <a href="#how-to-use">How to use</a>
- <a href="#how-it-works">How it works</a>
  - <a href="#machine-learning-model">Machine learning model</a>
  - <a href="#wahl-o-selfie-program">Wahl-O-Selfie program</a>
- <a href="#tests-and-results">Tests and results</a>
  - <a href="#test-1">Test 1</a>
  - <a href="#test-2">Test 2</a>
- <a href="#problems">Problems</a>
- <a href="#license-and-credits">License and credits</a>
- <a href="#postscript">Postscript</a>

## How to install
Wahl-O-Selfie (v1) requires:
- <a href="https://www.python.org/downloads/release/python-3107/">Python 3.10.7</a>
- <a href="https://pypi.org/project/face-recognition/">face_recognition</a>
  - <a href="https://visualstudio.microsoft.com/de/">Microsoft Visual Studio 2015 (or newer)</a>
  - <a href="https://cmake.org/download/">CMake</a>
  - <a href="https://pypi.org/project/dlib/">dlib</a>
- <a href="https://pypi.org/project/Pillow/">pillow</a>
- <a href="https://pypi.org/project/tensorflow/">TensorFlow Keras</a>
  - <a href="https://learn.microsoft.com/de-DE/cpp/windows/latest-supported-vc-redist?view=msvc-170">Microsoft Visual C++ Redistributable</a>
- <a href="https://pypi.org/project/numpy/">numpy</a>
- <a href="https://pypi.org/project/matplotlib/">matplotlib</a>
- os

### Installing face_recognition (for Windows)[^2]
To install face_recognition you have to have <a href="https://www.python.org/downloads/release/python-3107/">Python 3.10.7</a> and <a href="https://visualstudio.microsoft.com/de/">Microsoft Visual Studio 2015 (or newer)</a> with C/C++ Compiler  installed. After that you have to install <a href="https://cmake.org/download/">CMake</a> for Windows and **add it to your system variables**. Then you have to install <a href="https://pypi.org/project/dlib/">dlib</a> using pip:

```bash
pip install dlib
```

and finally you can install the <a href="https://pypi.org/project/face-recognition/">face_recognition</a> library, also by using pip:

```bash
pip install face_recognition
```

### Installing TensorFlow Keras[^3]

1. System requirements
   - Windows 7 or higher (64-bit)
2. Install Microsoft Visual C++ Redistributable
   - Got to the <a href="https://learn.microsoft.com/de-DE/cpp/windows/latest-supported-vc-redist?view=msvc-170">Microsoft Visual C++ downloads</a>
   - Scroll down the page to the _Visual Studio 2015, 2017 and 2019_ section.
   - Download and install the _Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019_ for your platform.
Make sure <a href="https://superuser.com/questions/1119883/windows-10-enable-ntfs-long-paths-policy-option-missing">long paths are enabled</a> on Windows
3. Install TensorFlow
   - First, run the command:
   ```bash
   pip install --upgrade pip
   ```
   to ensure that you have the most recent version of pip installed on your machine.
   - Then, install TensorFlow with pip:
   ```bash
   pip install tensorflow
   ```
   - And finally, install keras with pip:
   ```bash
   pip install keras
   ```

### Installing the other dependencies

Finally, you can install the other dependencies with pip:

```bash
pip install pillow numpy matplotlib
```

The library _os_ is pre-installed with python.

### Installing Wahl-O-Selfie
Download the project as a _.zip file_ and unzip it on your machine. Then open **main.py** with a code editor, preferably with <a href="https://code.visualstudio.com/download">Microsoft Visual Studio Code</a>, but make sure that you have the **Python extension** installed. 

## How to use

A few seconds after running the program a window should open up showing you a picture of a guy with a graph at the bottom, which gives you the results.
In addition to that there are a few new files in the program folder, most importantly _result.jpg_ and _result2.jpg_. _result.jpg_ is just a saved version of the picture you already saw in the window that opened up earlier and _result2.jpg_ is a different way of showing the results. Be aware that these files will be overwritten everytime you run the program, so if you see something you like copy-and-paste it to somewhere else.

If you want to use your own photo, you have to replace _testimage.jpg_ in the program folder. Make sure, that you use the JPG format and that it is called "testimage", otherwise the program will not recognize it. Please be aware, that Wahl-O-Selfie v1 can only process images that contain one face, more or less faces will result in an error.

## How it works

### Machine learning model

Wahl-O-Selfie v1 is using a pre-trained Keras model which was trained with 385 pictures of 79 different german politicians from 6 political partys. The pictures used for training the machine learning model were first run through another program which cut-out only the face to make sure that the training data is as accurate as possible without any other data influencing the results. 

This means that this photo:

<img src="https://user-images.githubusercontent.com/104715363/198629395-aa4f5daf-2ae1-442c-b87f-7c74e76fe4ae.jpg" title="Felix Banaszak" width="384" height="384">
(Picture of <a href="https://gruene-nrw.de/person/felix-banaszak-kv-duisburg/">Felix Banaszak - Die Grünen</a>)

is now this photo:

<img src="https://user-images.githubusercontent.com/104715363/198632965-849b8022-d8b1-4fa4-9436-c39e290922a0.jpg" title="processed Felix Banaszak">

which is way better training data.

All of the processed pictures were then used in <a href="https://teachablemachine.withgoogle.com">Teachable Machine</a> picture model with the different party names as class names and the corresponding politicians as training data for each class. After trainig the model you can download the trained keras model. The Keras model can be found in "trained_model/keras_model.h5" with a "lables.txt", which contains all the class names and was also downloaded from <a href="https://teachablemachine.withgoogle.com">TeachableMachine</a>. "lables.txt" is not used in Wahl-O-Selfie v1, instead it was just used to get the political partys in the program in the right order as I wanted to associate every party with their corresponding color.

Every political party has around 65 pictures of 13 different politicians meaning that there are around 5 different photos per politician which was supposed to ensure that the machine learning model focuses only on the face data and not on other parts of the image, like the background color.

### Wahl-O-Selfie program

After loading all the necessary librarys the program continues with loading the pre-trained keras model

```python
model = load_model('./trained_model/keras_model.h5')
```

and the picture

```python
picture = face_recognition.load_image_file('testimage.jpg')
```

The default-picture is a photograph made by <a href="https://thispersondoesnotexist.com">This person does not exist</a>.

<a href="https://thispersondoesnotexist.com"><img src="https://user-images.githubusercontent.com/104715363/177036941-a9307801-cd9d-4888-8326-1dfb430ee9ff.jpg" alt="testimage" width="384" height="384" title="https://thispersondoesnotexist.com"></img></a><br>
(Picture by "https://thispersondoesnotexist.com")

The loaded picture then gets analyzed by the face_recognition library and all recognized face locations get stored in a list called "face_locations":

```python
face_locations = face_recognition.face_locations(picture)
```

By using _len()_ the program can get the amount of elements in a list, which is used to get the amount of faces in the picture. Wahl-O-Selfie v1 can only process one face per picture which is why it checks if "face_locations" has more or less elements than one. If one of these if-statements is **True** it prints out the corresponding error in the terminal. There are a few commented out lines in the _more than one face_ case, which are purely for debugging:

```python
   # for(top, right, bottom, left) in face_locations:
   #     draw = ImageDraw.Draw(pil_image)
   #     draw.rectangle(((left, top), (right, bottom)), outline = (255, 0, 0), width = 4)
   #     pil_image.save("error.jpg")
   #     del draw
```

When these lines are not commented out they draw red rectangles around all the recognized faces and save the edited version as "error.jpg" so that the user can see all places where the program identified a face and verify that the program works properly.

However, if there is only one face in the picture it crops out the part where the face is located, scales it to 224x224 pixel and runs it through the machine learning model to get the prediction of which party the face most likely belongs to. The predictions are small numbers which first get stored in a "prediction" variable and right after they are safed in their own variables which I named after the political partys, in the order they stand in "lables.txt".

```python
    prediction = model.predict(data)

    AFD = prediction[0, 0]
    CDU_CSU = prediction[0, 1]
    Gruenen = prediction[0, 2]
    Linke = prediction[0, 3]
    FDP = prediction[0, 4]
    SPD = prediction[0, 5]
```

The prediction data then gets converted into percentages for easier handling and the coordinates of the face are used to draw a red rectangle around that area.

<img src="https://user-images.githubusercontent.com/104715363/177036948-2051a9c9-c752-4fda-b8e9-7a1dec9deddf.jpg" width="384" height="384">

The program also gets the biggest value and to which party it belongs to identify which party is the most likeliest.

```python
max = max(AFD, CDU_CSU, Gruenen, Linke, FDP, SPD)
```

Afterwards it prints out the predictions in percent to the terminal followed by the most likeliest party.

e.g.
```txt
AFD: 2.8%
CDU/CSU: 2.1%
Die Grünen: 0.0%
Linke: 94.5%
FDP: 0.4%
SPD: 0.1%
----------------------------------------
Die Linke
```

At the end it generates two forms of presenting the data in image form.

For the first version ("result.jpg") the program generates a graph to put under the photo.

```python
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
```

This code handles generating a graph with all the percentage values for each party and formatting it so that every bar graph has the right color corresponding to the party it is associated with, printing the corresponding party names besides each graph and putting additional text above and below the bar graph. Furthermore, there is some code which handles what should happen if the testimage is thinner or thicker than the bar graph, so that the graph is always centered.

<img src="https://user-images.githubusercontent.com/104715363/198905504-7fbf4d19-bd1e-4d67-977b-6e6554b19f44.jpg" width="512">

For the second version ("result2.jpg") the program is just printing the party names with their percentages under the red square.

```python
    text_width, text_height = draw.textsize('Die Grünen - 100.0%')
    draw.rectangle(((left,(bottom + 5) + (text_height * 5 + 5)), (right, bottom)), fill = (0, 0, 0), outline = (0, 0, 0))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 70)), 'AFD - ' + str(AFD_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 60)), 'CDU/CSU - ' + str(CDU_CSU_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 50)), 'Die Grünen - ' + str(Gruenen_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 40)), 'Die Linke - ' + str(Linke_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 30)), 'FDP - ' + str(FDP_percent) + '%', fill=(255, 255, 255))
    draw.text((left + 6, (bottom + 5) + (text_height * 6 - 20)), 'SPD - ' + str(SPD_percent) + '%', fill=(255, 255, 255))
    pil_image.save('result2.jpg')
```

<img src="https://user-images.githubusercontent.com/104715363/177036952-62863484-e06c-495a-858b-b286f619a32b.jpg" width="512" height="512">

```python
    os.remove('graph.png')
    img.show()
```

Finally, it is using the _os library_ to delete a temporarily created "graph.png" file which contained the previously generated graph for "result.jpg" and it is showing said result.jpg.

## Tests and results

Program tested in **Python 3.10.7**.

### Test 1

For Test #1 I used different pictures from people that are in the machine learning model to test if the model learned how these people look like and if it is able to recognize them in other pictures.

| Test #1 | Results |
| --- | --- |
| Combined results | <img src="https://user-images.githubusercontent.com/104715363/199010275-76d4751d-2e5b-4d87-a6c0-8220b948b7d3.png" width="512"> |
| AFD | <img src="https://user-images.githubusercontent.com/104715363/199010438-e5848f09-2df8-4015-a1d9-c905041448d4.png" width="512"> |
| CDU/CSU | <img src="https://user-images.githubusercontent.com/104715363/199010442-17f404f4-b891-4217-bd54-6386f41cd5e9.png" width="512"> |
| Die Grünen | <img src="https://user-images.githubusercontent.com/104715363/199010445-5cdae09e-8077-48bd-9578-11075adb16b7.png" width="512"> |
| Die Linke | <img src="https://user-images.githubusercontent.com/104715363/199010447-ab205bda-af7c-4026-9191-b4953a8e7b05.png" width="512"> |
| FDP | <img src="https://user-images.githubusercontent.com/104715363/199010443-4d2a902e-ce87-43ce-8c88-5121a17a6083.png" width="512"> |
| SPD | <img src="https://user-images.githubusercontent.com/104715363/199010448-869473d1-be32-454e-9074-1946180aac17.png" width="512"> |

**Test 1 results:**
<br><img src="https://img.shields.io/badge/test%201-30%20tested,%2020%20true,%2010%20false-critical?style=for-the-badge"><br>
- <details><summary>AFD: 5 Tested; 2 True, 3 False</summary>
  <p>
  AFD: 2 <br>
  CDU/CSU: 1 <br>
  Die Grünen: 2 <br>
  Die Linke: 0 <br>
  FDP: 0 <br>
  SPD: 0 
  </p>
  </details>
- <details><summary>CDU/CSU: 5 Tested; 3 True, 2 False</summary>
  <p>
  AFD: 0 <br>
  CDU/CSU: 3 <br>
  Die Grünen: 1 <br>
  Die Linke: 1 <br>
  FDP: 0 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>Die Grünen: 5 Tested; 4 True, 1 False</summary>
  <p>
  AFD: 0 <br>
  CDU/CSU: 0 <br>
  Die Grünen: 4 <br>
  Die Linke: 0 <br>
  FDP: 1 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>Die Linke: 5 Tested; 3 True, 2 False</summary>
  <p>
  AFD: 0 <br>
  CDU/CSU: 1 <br>
  Die Grünen: 0 <br>
  Die Linke: 3 <br>
  FDP: 1 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>FDP: 5 Tested; 5 True, 0 False</summary>
  <p>
  AFD: 0 <br>
  CDU/CSU: 0 <br>
  Die Grünen: 0 <br>
  Die Linke: 0 <br>
  FDP: 5 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>SPD: 5 Tested; 3 True, 2 False</summary>
  <p>
  AFD: 1 <br>
  CDU/CSU: 1 <br>
  Die Grünen: 0 <br>
  Die Linke: 0 <br>
  FDP: 0 <br>
  SPD: 3
  </p>
  </details>

Test 1 had an overall accuracy of **66.6667%** which shows that the machine learning model has a good understanding of how the people in the training data looked like and it was mostly able to sort them in their corresponding party.

### Test 2

For Test #2 I used random pictures of other people in the political partys to see if the machine learning model learned which aspects were important to confidently sort faces into a political party.

| Test #2 | Results |
| --- | --- |
| Combined results | <img src="https://user-images.githubusercontent.com/104715363/199027234-a22a51a3-569a-4157-b5b6-5873096874aa.png" width="512"> |
| AFD | <img src="https://user-images.githubusercontent.com/104715363/199027237-235784df-25a5-4f01-bd1f-39567183d37c.png" width="512"> |
| CDU/CSU | <img src="https://user-images.githubusercontent.com/104715363/199027238-21158cf4-11b7-4b0c-bb75-97e72ced4a43.png" width="512"> |
| Die Grünen | <img src="https://user-images.githubusercontent.com/104715363/199027241-85928f5b-ae10-4b0c-b397-576c7d256e22.png" width="512"> |
| Die Linke | <img src="https://user-images.githubusercontent.com/104715363/199027244-54c8f70f-831d-486d-980e-c51806734082.png" width="512"> |
| FDP | <img src="https://user-images.githubusercontent.com/104715363/199027239-d824b40f-4f29-4bc0-8ed9-6438de69f0a1.png" width="512"> |
| SPD | <img src="https://user-images.githubusercontent.com/104715363/199027235-60143459-71e4-4631-9a9b-faa54a25658e.png" width="512"> |

**Test 2 results:**
<br><img src="https://img.shields.io/badge/test%202-30%20tested,%206%20true,%2024%20false-critical?style=for-the-badge"><br>
- <details><summary>AFD: 5 Tested; 1 True, 4 False</summary>
  <p>
  AFD: 1 <br>
  CDU/CSU: 2 <br>
  Die Grünen: 0 <br>
  Die Linke: 1 <br>
  FDP: 1 <br>
  SPD: 0 
  </p>
  </details>
- <details><summary>CDU/CSU: 5 Tested; 2 True, 3 False</summary>
  <p>
  AFD: 1 <br>
  CDU/CSU: 2 <br>
  Die Grünen: 0 <br>
  Die Linke: 2 <br>
  FDP: 0 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>Die Grünen: 5 Tested; 2 True, 3 False</summary>
  <p>
  AFD: 0 <br>
  CDU/CSU: 1 <br>
  Die Grünen: 2 <br>
  Die Linke: 1 <br>
  FDP: 1 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>Die Linke: 5 Tested; 0 True, 5 False</summary>
  <p>
  AFD: 1 <br>
  CDU/CSU: 4 <br>
  Die Grünen: 0 <br>
  Die Linke: 0 <br>
  FDP: 0 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>FDP: 5 Tested; 0 True, 5 False</summary>
  <p>
  AFD: 2 <br>
  CDU/CSU: 2 <br>
  Die Grünen: 1 <br>
  Die Linke: 0 <br>
  FDP: 0 <br>
  SPD: 0
  </p>
  </details>
- <details><summary>SPD: 5 Tested; 1 True, 4 False</summary>
  <p>
  AFD: 1 <br>
  CDU/CSU: 2 <br>
  Die Grünen: 1 <br>
  Die Linke: 0 <br>
  FDP: 0 <br>
  SPD: 1
  </p>
  </details>

Test #2 had only an accuracy of **20%** which shows that the machine learning model could not identify the reason why someone is in a party instead it could just remember that someone is in a party. This means that the machine learning model is way too small to be able to learn which face should be in which party.
  
## Problems
Wahl-O-Selfie v1 is just a proof of concept, meaning that the dataset used to determin the political party of a face is rather small with an insufficient diversity, resulting in wrong and/or inaccurate results. 

## License and credits

This work is made available under the <a href="https://github.com/TachLaif/wahl-o-selfie-v1/blob/main/LICENSE">**GNU Affero General Public License v3.0**</a>.

Project made by **<a href="https://github.com/TachLaif">TechLife</a>**.
<br><br><a href="https://discord.com"><img src="https://img.shields.io/badge/TechLife-4447-informational?style=for-the-badge&logo=discord&logoColor=white"></a><br><a href="https://twitter.com/_Tech4Life_"><img src="https://img.shields.io/badge/Twitter-@__Tech4Life__-informational?style=for-the-badge&logo=twitter&logoColor=white"></a><br><a href="https://www.buymeacoffee.com/TechLife"><img src="https://img.shields.io/badge/Buy%20me%20a-coffee-red?style=for-the-badge&logo=buymeacoffee&logoColor=white" title="I like coffee!"></a>

## Postscript

While writing this readme file I found out that something similar was actually build with a much bigger dataset which contained the self-reported political orientation of over a million participants from Facebook and dating website accounts from three countries (the U.S, the UK and Canada). This facial recognition model achieved an accuracy of around 72%. If you want to read the article yourself you can find it <a href="https://rdcu.be/cYEvm">HERE</a>.

[^1]: The "<a href="https://www.wahl-o-mat.de">Wahl-O-Mat</a>" is a website by the german <a href="www.bpb.de">bpb</a> with questions which you can fill out and afterwards you can see which political partys have similar interests. This is supposed to help people make up their mind about who they should vote for.
[^2]: https://github.com/ageitgey/face_recognition/issues/175#issue-257710508
[^3]: https://www.tensorflow.org/install/pip
