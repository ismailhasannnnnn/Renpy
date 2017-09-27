# The script of the game goes in this file.
image bg introbg = "introbg.jpg"
image bg black = "black.jpg"
image bg malebedroom = "malebedroom.png"
image bg femalebedroom = "femalebedroom.jpg"
image bg kitchen = "kitchen.jpg"
image bg road = "road.jpg"
image bg school = "school.jpg"
image mom = "sasha.png"


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




define movemom = MoveTransition(3.0)
define flash = Fade(1.0, 0, 3.0, color='#FFFFFF')





# The game starts here.

label start:
    $ ability = 1
    # $ randAbility = renpy.random.randint(1, 3) # TO PRINT, USE %(randAbility)d
    # 1 - Immune to Radiation
    # 2 - PLACEHOLDER
    # 3 - PLACEHOLDER
    
    
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg introbg
    play music "evermindful.mp3"

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
   
    "Hi. This is your adventure."
    "Let's start with a simple question!"
label intro:
    "Are you male or female?"
    menu:
        "Male":
            # $ gender = 1 # 1 is male
            jump male
           
        "Female":
            # $ gender = 2 # 2 is female
            jump female
           
            
label male:
    "I see, you're male."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Arthur"
       
    "I see. Your name is %(playername)s, how fitting!"
    "Okay, so just to be sure, your name is %(playername)s, and you're male?"
    menu:
        "Yes":
            "Awesome! Let's keep going then!"
            jump maleintro2
                
        "No":
            jump intro
    
    
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
    
    "What about your best friend? Are they male or female?"
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
    if bestfriendgender == 1:
        "So they're male, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump maleprologue
                
            "No":
                jump maleintro2
                
    if bestfriendgender == 2:
        "So they're female, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump maleprologue
                
            "No":
                jump maleintro2
                
label femaleintro2:
    
    "What about your best friend? Are they male or female?"
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
    
    "Listen, %(playername)s, it's getting dark. We should probably get going."
    scene bg black
    with fade
    "From then on, nobody knew how incredibly gifted %(playername)s was."
    "Little did he know, a great threat would soon overwhelm America, and his life would be changed forever."
    stop music fadeout 1.0
    jump malechapter1
    
label femaleprologue:
    
    "Listen, %(playername)s, it's getting dark. We should probably get going."
    scene bg black
    with fade
    "From then on, nobody knew how incredibly gifted %(playername)s was."
    "Little did she know, a great threat would soon overwhelm America, and her life would be changed forever."
    stop music fadeout 1.0
    jump femalechapter1    
    
    
    
    
    
    # This ends the game.


    pause
    return
