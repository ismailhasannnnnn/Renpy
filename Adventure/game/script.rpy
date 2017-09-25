# The script of the game goes in this file.
image bg introbg = "introbg.jpg"
image bg black = "black.jpg"
image bg malebedroom = "malebedroom.jpg"
image bg femalebedroom = "femalebedroom.jpg"


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define player = Character("%(playername)s")
define bestfriend = Character("%(bestfriendname)s")
define unknown = Character("???", color='#000000')



# The game starts here.

label start:

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
            $ gender = 1 # 1 is male
            
        "Female":
            $ gender = 2 # 2 is female   
            
    if gender == 1:
        "I see, you're male."
    if gender == 2:
        "I see, you're female."
    $ playername = renpy.input("What's your name?")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Arthur"
       
    "I see. Your name is %(playername)s, how fitting!"
    if gender == 1:
        "Okay, so just to be sure, your name is %(playername)s, and you're male?"
        menu:
            "Yes":
                jump intro2
                
            "No":
                jump intro
                
    if gender == 2:
        "Okay, so just to be sure, your name is %(playername)s, and you're female?"
        menu:
            "Yes":
                "Awesome! Let's keep going then!"
                jump intro2
                
            "No":
                jump intro
   
label intro2:
    
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
                jump prologue
                
            "No":
                jump intro2
                
    if bestfriendgender == 2:
        "So they're female, and their name is %(bestfriendname)s?"
        menu:
            "Yes":
                jump prologue
                
            "No":
                jump intro2
                
label prologue:
    
    "Listen, %(playername)s, it's getting dark. We should probably get going."
    scene bg black
    with fade
    "From then on, nobody knew how incredibly gifted %(playername)s was."
    if gender == 1:
        "Little did he know, a great threat would soon overwhelm America, and his life would be changed forever."
    if gender == 2:
        "Little did she know, a great threat would soon overwhelm America, and her life would be changed forever."
    stop music fadeout 1.0
    jump chapter1
    
label chapter1:
    
    "..."
    "..."
    unknown"These violent delights have violent ends, %(playername)s."
    "...!"
    if gender == 1:
        scene bg malebedroom
        with fade
    if gender == 2:
        scene bg femalebedroom
        with fade
    
    # This ends the game.


    
    return
