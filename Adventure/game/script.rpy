
# The script of the game goes in this file.
image bg introbg = "introbg.jpg"
image bg black = "black.jpg"
image bg malebedroom = "malebedroom.png"
image bg femalebedroom = "femalebedroom.jpg"
image bg kitchen = "kitchen.jpg"
image bg road = "road.jpg"
image bg school = "school.jpg"
image mom neutral = "momn.png"
image dad = "Daddy.png"
image hospital = "INTRO.png"
image doctor = "IntroWithDoctor.png"
image death = "IntroWithMarcus.png"
image july21 = "july21.png"
image aug23 = "August23.png"
image j = "j.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[playername]")
define bf = Character("bestfriendname")
define unknown = Character("???", color='#FFFFFF')
define mom = Character("Mom", color='#FFFFFF')
define dad = Character("Dad", color='#FFFFFF')
define teacher = Character("Mr. Sharp", color='#FFFFFF')
define f1 = Character("Josh", color='#FFFFFF')
define f2 = Character("Ericka", color='#FFFFFF')
define who = Character("Mom", color='#c41b13')
define Doc = Character("Doctor", color ='#FFFFFF')
define Nurse = Character("Assistant Nurse", color='#FFFFFF')




define movemom = MoveTransition(3.0)
define flash = Fade(1.0, 0, 3.0, color='#FFFFFF')
define slowfade = Fade(5.0, 0, 1)



init:
    image blossoms = SnowBlossom(Animation("snow.png",count=100,xspeed=100,yspeed=1000))

label splashscreen:
    scene black
    with Pause(.5)

    scene j
    with dissolve
    with Pause(2)

    scene black
    with dissolve
    with Pause(.5)


    return


# The game starts here.

label start:
    $ ability = 1
    # $ randAbility = renpy.random.randint(1, 3) # TO PRINT, USE %(randAbility)d
    # 1 - Immune to Radiation
    # 2 - PLACEHOLDER
    # 3 - PLACEHOLDER



    scene bg black
    show blossoms

    play music "music/River.mp3"

    show text "Winter, Years Ago"
    pause
    show text "Mom?"
    pause
    show text "{color=#00BFFF}Yes sweetie?{/color}"
    pause
    show text "Where do people go when they die?"
    pause
    show text"{color=#00BFFF}Honey, why do you want to know that?{/color}"
    pause
    show text "Cause I'm scared."
    pause
    show text"{color=#00BFFF}All you need to know is that they go to a better place.{/color}"
    pause
    show text"Did Uncle Justin go to a better place?"
    pause
    show text"{color=#00BFFF}Yes, sweetie. That's what happened to him.{/color}"
    pause
    show text"Well, why are you crying then?"
    pause
    scene black
    with dissolve


    hide blossoms with Fade(1.0, 1.0, 1.0)
    stop music fadeout 2.0

    play sound "music/HeartRate.mp3" loop
    show text"Fifteen Years Later"
    pause















    #with Fade(0.5, 1.0, 0.5)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.










    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

   # e"Test"
   # e"This is me testing to see if any of this actually works"
   # e"If it doesn't well then i suck"
   # e"If it does, cool!"
   # e"Heres to the beginning of our story."
   # $ player_name = renpy.input("What is your name?")
   # $ player_name = player_name.strip()
   # if player_name == "":
   #     $ player_name = "Loser"

   # "Ah! Your name is %(player_name)s!"
    play music "music/Hum.mp3" fadein 2.0
    scene hospital
    with fade

    #

    Nurse "Doctor, The patient's awake. Shall we run the diagnostics?"
    Doc"The one for amnesia?"
    Nurse"Yes."
    Doc"Alright. Give me a second."
    Nurse"Doc, can we please unplug that heartrate sensor? It's driving me crazy."
    Doc"Gotcha."
    stop sound
    Doc"*clears throat*"
   # stop music fadeout 2.0

    scene doctor
    with dissolve
   # play music "music/evermindful.mp3"
    Doc"Good morning! or should I say, evening!"
    Doc"You've been out for three days! That anesthesia really took a toll on you!"
    Nurse"You gave him an overdose, Doc."
    Doc"Okay. Maybe I did. Maybe I didn't. Anyway. Let's cut to the chase."
    Doc"I'm going to ask you a few questions, and you just answer what feels right."
    Doc"They might sound stupid, but the faster you answer, the faster you'll get outta here."
    Doc"Ready?"

label ready:

    menu:
        "'I'm Ready'":

            jump intro
        "'Where am I?'":
            Nurse"See Doc? Why didn't we just call in Betty for the anesthesia?"
            Doc"Haha. Just ignore her. We'll answer the questions after you're done answering yours."
            jump intro

label intro:
    Doc"Alright."
    Doc"Are you male or female?"
    menu:
        "Male":
            # $ gender = 1 # 1 is male
            jump male

        "Female":
            # $ gender = 2 # 2 is female
            jump female


label male:
    Doc"Awesome! You passed the first question! Don't worry. We're almost done."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Arthur"

    Doc"Alright, [playername]! You remember your name!"
    Doc"Great! Let's keep going then!"
    jump maleintro2



label female:
    "Awesome! You passed the first question! Don't worry. We're almost done."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Karolina"

    Doc"Perfect, [playername], you remember your name!"
    Doc "Great! Let's keep going then!"
    jump femaleintro2

label maleintro2:

    Doc"Do you remember your best friend? Are they male or female?"
    menu:
        "Male":
            $ bestfriendgender = 1 # 1 is male

        "Female":
            $ bestfriendgender = 2 # 2 is female

    if bestfriendgender == 1:
        Doc"He'll be happy to hear you didn't forget he was a guy."
    if bestfriendgender == 2:
        Doc"She'll be ecstatic to hear you didn't forget she was a girl."
    $ bestfriendname = renpy.input("And their name?")
    $ bestfriendname = bestfriendname.strip()
    if bestfriendname == "":
        if bestfriendgender == 1:
            $ bestfriendname ="male"
        if bestfriendgender == 2:
            $ bestfriendname = "female"
    if bestfriendgender == 1:
        Doc "Perfect! You remember his name as well!"
        jump maleprologue

    if bestfriendgender == 2:
        Doc "Perfect! You remember her name as well!"
        jump maleprologue

label femaleintro2:

    "Do you remember your best friend? Are they male or female?"
    menu:
        "Male":
            $ bestfriendgender = 1 # 1 is male

        "Female":
            $ bestfriendgender = 2 # 2 is female

    if bestfriendgender == 1:
        Doc"He'll be happy to hear you didn't forget he was a guy."
    if bestfriendgender == 2:
        Doc"She'll be ecstatic to hear you didn't forget she was a girl."
    $ bestfriendname = renpy.input("And their name?")
    $ bestfriendname = bestfriendname.strip()
    if bestfriendname == "":
        $ bestfriendname = "Justin"
    if bestfriendgender == 1:
        Doc "Perfect! You remember his name as well!"
        jump femaleprologue

    if bestfriendgender == 2:
        Doc "Perfect! You remember her name as well!"
        jump femaleprologue

label maleprologue:

    Doc"Alright, %(playername)s. I think you're good to go!"
    Doc"Just give that knee two to three days to heal and it'll be like it never broke on you!"
    stop music
    with fade
    scene black
    with slowfade
    Doc"I didn't think he'd survive."
    Nurse "Why didn't you tell him the truth about the surgery?"
    Doc"To keep him alive."
    with Pause(3.0)
    jump malechapter1

label femaleprologue:

    "Alright, %(playername)s. I think you're good to go!"
    "Just give that knee two to three days to heal and it'll be like it never broke on you!"
    stop music
    with fade
    scene black
    with slowfade
    Doc"I didn't think she'd survive."
    Nurse "Why didn't you tell her the truth about the surgery?"
    Doc"To keep her alive."
    with Pause(3.0)
    jump femalechapter1

    scene bg black
    with fade

    stop music fadeout 1.0
    jump femalechapter1

    pause
    return
