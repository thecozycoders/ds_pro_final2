import speech_recognition as sr
import turtle as tr
import alphabets
from PIL import Image
#creating a instance of Recognizer to recognize the speech

r = sr.Recognizer()

#mic will behave as original mic for listening to our audio and returns AudioData object

mic = sr.Microphone()

#Program initiates here 
with mic as source:
    r.adjust_for_ambient_noise(source)
    #print(type(source))
    audio = r.listen(source)
# not added try except block yet which are need because of unknown value found exception
audio = r.recognize_google(audio)
t = tr.Turtle()
def microphone_classification(audio):
    #checking what is given by the microphone
    print(audio)
    if (audio.lower() == "start"):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Entering the graphic zone")
            audio = r.listen(source)
            audio = r.recognize_google(audio)
        if(audio.lower() == "geometric"):
            print("We are now in the world of geometry")
            print("The avaiable shapes are:")
            print("Triangle ::: Rectangle ::: Square ::: Circle ::: Trapezium ::: Line")
            with mic as source2:
                r.adjust_for_ambient_noise(source2)
                audio = r.listen(source2)
            audio = r.recognize_google(audio)    
            draw_geometric_shapes(audio)
        #Alphabet section of my project    
        elif(audio.lower() == "alphabet" or audio.lower() =="alphabets"):
            print("Entered the alphabets")
            print("Now you can draw single alphabets or complete name (say name for a word first)")
            with mic as source2:
                r.adjust_for_ambient_noise(source2)
                audio = r.listen(source2)
            audio = r.recognize_google(audio)
            #Where alphabets will be converted in to name
            if(audio.lower() == "name" or audio.lower() == "names"):
                print("Entered the naming zone")
                print("You said name now say that word which you want to be drawn")
                with mic as source3:
                    r.adjust_for_ambient_noise(source3)
                    audio = r.listen(source3)
                audio = r.recognize_google(audio)
                drawName(audio)
            else:
                drawAlpha(audio)
        elif(audio.lower() == "fruits" or audio.lower() == "fruit" or audio.lower() == "vegetable" or audio.lower() == "vegetables"):
            print("Entered in the healthy zone : Hmmmmmmmm Talking about fruits and vegetables right and Yes Indeed")
            with mic as source4:
                r.adjust_for_ambient_noise(source4)
                audio = r.listen(source4)
            audio = r.recognize_google(audio)
            image_viewer(audio)

        elif(audio.lower() == "home"):
            draw_home()
        else:
            print("Sorry I still make a lot of errors in recognising your speech Sir please try again")
            with mic as source5:
                r.adjust_for_ambient_noise(source5)
                audio = r.listen(source5)
            audio = r.recognize_google(audio)
            microphone_classification(audio)
            
#function containing code for drawing different kind of shapes
def draw_geometric_shapes(shape):
    shape_lower = shape.lower()
    if shape_lower == "triangle":
        print("Drawing Triangle")
        t.forward(50)
        t.left(60)
        t.forward(50)
        t.left(60)
        t.forward(50)

    elif shape_lower == "square":
        print("Drawing Square")
        t.forward(60)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(60)
        
    elif shape_lower == "rectangle":
        print("Drawing Rectangle")
        t.forward(60)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(30)
        
    elif shape_lower == "circle":
        print("Drawing Circle")
        for i in range(360):
            t.forward(1)
            t.left(1)

    elif shape_lower == "line":
        print("Drawing line")
        t.forward(60)

    elif shape_lower == "trapezium":
        print("Drawing Trapezium")
        t.forward(60)
        t.left(60)
        t.left(60)
        t.forward(20)
        t.left(60)
        t.forward(30)
        t.left(60)
        t.forward(20)
    else:
        print("Wrong shape Wrong geometry")

#function for drawing a conventional hut like structure
def draw_home():
    t.forward(80)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.penup()
    t.forward(80)
    t.pendown()
    t.forward(140)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(140)
    t.right(37)
    t.forward(50)
    t.left(127)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(40)
    t.pendown()
    t.right(143)
    t.forward(50)

def drawAlpha(audio_alpha,index):
    if(audio_alpha.lower() == "a"):
        alphabets.A(index)
    elif(audio_alpha.lower() == "b"):    
        alphabets.B(index)
    elif(audio_alpha.lower() == "c"):
        alphabets.C(index)
    elif(audio_alpha.lower() == "d"):
        alphabets.D(index)
    elif(audio_alpha.lower() == "e"):
        alphabets.E(index)    
    elif(audio_alpha.lower() == "f"):
        alphabets.F(index)
    elif(audio_alpha.lower() == "g"):
        alphabets.G(index)
    elif(audio_alpha.lower() == "h"):
        alphabets.H(index)
    elif(audio_alpha.lower() == "i"):
        alphabets.I(index)
    elif(audio_alpha.lower() == "j"):
        alphabets.J(index)
    elif(audio_alpha.lower() == "k"):
        alphabets.K(index)
    elif(audio_alpha.lower() == "l"):
        alphabets.L(index)            
    elif(audio_alpha.lower() == "m"):
        alphabets.M(index)
    elif(audio_alpha.lower() == "n"):
        alphabets.N(index)
    elif(audio_alpha.lower() == "o"):
        alphabets.O(index)
    elif(audio_alpha.lower() == "p"):
        alphabets.P(index)
    elif(audio_alpha.lower() == "q"):
        alphabets.Q(index)    
    elif(audio_alpha.lower() == "r"):
        alphabets.R(index)
    elif(audio_alpha.lower() == "s"):
        alphabets.S(index)
    elif(audio_alpha.lower() == "t"):
        alphabets.T(index)
    elif(audio_alpha.lower() == "u"):
        t.forward(30)
        alphabets.U(index)
    elif(audio_alpha.lower() == "v"):
        alphabets.V(index)
    elif(audio_alpha.lower() == "w"):
        alphabets.W(index)
    elif(audio_alpha.lower() == "x"):
        alphabets.X(index)
    elif(audio_alpha.lower() == "y"):
        alphabets.Y(index)
    elif(audio_alpha.lower() == "z"):
        alphabets.Z(index)
    else:
        print("Sorry didn't matched any letter are you really speaking english hihihi hahaha hohoho")    
            
    
    
def image_viewer(audio_image):
    print("HERE COMES YOUR %s ",(audio_image))
    image = Image.open(r"C:\Users\vish1\OneDrive\Desktop\ds_pro\{}.jpeg".format(audio_image))
    image.show()

def drawName(audio_name):
    print(audio_name)
    for i in audio_name:
        drawAlpha(i,audio_name.index(i))

        
microphone_classification(audio)        

