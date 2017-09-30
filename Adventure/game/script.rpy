
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



init:
    image blossoms = SnowBlossom(Animation("snow.png",count=100,xspeed=100,yspeed=1000))
                                           



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
       
    " THIS IS A PLACEHOLDER INTRO: A past conversation between you and mom. Perhaps make the conversation pertain better to radiation "
    "Mom?"
    who"Yes sweetie?"
    "Where do people go when they die?"
    who"Honey, why do you want to know that?"
    "Cause I'm scared."
    who"All you need to know is that they go to a better place."
    "Did Uncle Justin go to a better place?"
    who"Yes, sweetie. That's what happened to him."
    "Well, why. . ."
    hide blossoms with Fade(1.0, 1.0, 1.0)
    stop music fadeout 4.0
    "Why are you crying then?"
    
    
    
    
    
    play music "music/HeartRate.mp3"
    scene july21
    with fade
    
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
    scene hospital
    with fade
   
    #
    Nurse "Doctor. The patient's awake. Shall we run the diagnostics?"
    Doc"The one for amnesia?"
    Nurse"Yes."
    Doc"Alright. Give me a second."
    Doc"*clears throat*"
    stop music fadeout 1.0
    scene doctor
    with dissolve
    play music "music/evermindful.mp3"
    Doc"Hello! We need to check if that brain of yours is still fully functional"
    Doc"I'm going to ask you a few questions, and you just answer what feels right."
    Doc"Ready?"
    
label ready:
    
    menu:
        "I'm Ready":
            
            jump intro
        "Where am I?":
            Doc"Don't worry. We'll answer the questions after you're done answering yours."
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
    Doc"Well, obviously you are! Don't worry. We're almost done."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Arthur"
       
    Doc"Alright, [playername]! You remember your name!"
    Doc"Awesome! Let's keep going then!"
    jump maleintro2
                
        
    
label female:
    "I see, you're female."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Arthur"
       
    "I see. Your name is %(playername)s, how fitting!"
    "Okay, so just to be sure, your name is %(playername)s, and you're female?"
    menu:
        "Yes":
            "Awesome! Let's keep going then!"
            jump femaleintro2
                
        "No":
            jump intro
   
label maleintro2:
    
    Doc"Do you remember your best friend? Are they male or female?"
    menu:
        "Male":
            $ bestfriendgender = 1 # 1 is male
            
        "Female":
            $ bestfriendgender = 2 # 2 is female   
            
    if bestfriendgender == 1:
        Doc"So he's male."
    if bestfriendgender == 2:
        "So she's female."
    $ bestfriendname = renpy.input("And their name?")
    $ bestfriendname = bestfriendname.strip()
    if bestfriendgender == 1:
        Doc"So they're male, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump maleprologue
                
            "No":
                jump maleintro2
                
    if bestfriendgender == 2:
        Doc"So they're female, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump maleprologue
                
            "No":
                jump maleintro2
                
label femaleintro2:
    
    "Do you remember your best friend? Are they male or female?"
    menu:
        "Male":
            $ bestfriendgender = 1 # 1 is male
            
        "Female":
            $ bestfriendgender = 2 # 2 is female   
            
    if bestfriendgender == 1:
        "Interesting, they're male."
    if bestfriendgender == 2:
        "Interesting, they're female."
    $ bestfriendname = renpy.input("And their name?")
    $ bestfriendname = bestfriendname.strip()
    if bestfriendname == "":
        $ bestfriendname = "Justin"
    if bestfriendgender == 1:
        "So they're male, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump femaleprologue
                
            "No":
                jump femaleintro2
                
    if bestfriendgender == 2:
        "So they're female, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump femaleprologue
                
            "No":
                jump femaleintro2
                
label maleprologue:
    
    Doc"Alright, %(playername)s. I think you're good to go!"
    Doc"Just give that knee two to three days to heal and it'll be like it never broke on you!"
    scene doctor
    with fade
    stop music fadeout 1.0
    Doc"Hello?"
    Doc"[playername]? Are you still with me?"
    scene doctor
    with fade 
    Nurse"Check the heartrate! The heartrate!!"
    scene doctor
    with Fade(0.4,0.2,0.5)
    Doc"Connect him to life support RIGHT NOW!"
    scene death
    with Fade(0.2,0.5,0.2)
    unknown"{i}For thou art the beginning of the end.{i}"
    scene doctor
    with Fade(0.1,0.2,0.2)
    Nurse"We're losing him! Plug in the life support!"
    
    
    scene black
    with fade
    
    
    jump malechapter1
    
label femaleprologue:
    
    "Alright, %(playername)s. I think you're good to go!"
    "Just give that knee two to three days to heal and it'll be like it never broke on you!"
    
    scene bg black
    with fade
    
    stop music fadeout 1.0
    jump femalechapter1    
    
    pause
    return
