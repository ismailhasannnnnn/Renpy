# The script of the game goes in this file.
image bg introbg = "introbg.jpg"
image bg black = "black.jpg"
image bg malebedroom = "malebedroom.jpg"
image bg femalebedroom = "femalebedroom.jpg"
image bg kitchen = "kitchen.jpg"
image mom = "sasha.png"


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("playername")
define bf = Character("bestfriendname")
define unknown = Character("???", color='#FFFFFF')
define mom = Character("Mom", color='#FFFFFF')
define dad = Character("Dad", color='#FFFFFF')
define movemom = MoveTransition(3.0)
define flash = Fade(1.0, 0, 3.0, color='#FFFFFF')



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
    
label malechapter1:
    
    "..."
    "..."
    unknown"These violent delights have violent ends, %(playername)s."
    "...!"

        
label femalechapter1:
    
    "..."
    "..."
    unknown"These violent delights have violent ends, %(playername)s."
    "...!"
    scene bg femalebedroom
    with dissolve
    playername"(What the hell was that?)"
    show mom at right
    with dissolve
    mom"You're gonna be late for school!"
    mom"Come downstairs and eat breakfast now!"
    scene bg kitchen
    with fade
    dad"Well, look who finally decided to wake up!"
    dad"I'm just messin, %(playername)s, you just took a while to wake up."
    mom"Anyhow, you're gonna be late to school, so eat your breakfast fast!"
    menu:
        "Eat breakfast with your parents. Risk being late.":
            jump femalechapter1breakfast
        
        "Skip breakfast and leave for school.":
            playername"Sorry guys, I don't have any time to eat. I'm already way late for school."
            dad"That's exactly the reason why you're going to stay and eat breakfast with us. A few more minutes won't kill you. You're already late, anyway."
            jump femalechapter1nobreakfast
        
label femalechapter1breakfast:

    "As you sit down to eat, you hear the TV new anchor blabber about rising tensions between the Sovereignity and the U.S."
    dad"Hey, %(playername)s, look at the crap they're feeding us on the news. They're saying that North Korea's gonna nuke us!"
    dad"No way they'd ever do it. Seriously. They know that if they did, we'd completely obliterate them."
    dad"Besides, haven't they ever heard of Mutually Assured Destruction?"
    
label fm1:
    
    menu:
        "They said something about Sovereignity. What's that?":
            dad"C'mon kiddo, what're they teaching you in history? It's the North Korean-Russian alliance."
            dad"I should start looking for other schools maybe."
            jump fm1
            
        "What's Mutually Assured Destruction?":
            mom"Wow, they really aren't teaching anything in that school of yours! Should I have a parent-teacher conference?"
            dad"Let's just say that North Korea won't get a second chance to nuke us. You know, cause they're gonna be dead."
            jump fm1
            
        "I'm seriously gonna be so late for school. Thanks for the food mom. Bye!":
            mom"Have fun at school, sweetie!"
            dad"Tell your teachers to explain more things to you! If they don't then I definitely will!"
            jump femalechapter1nobreakfast


label femalechapter1nobreakfast:
    "As you sprint towards your school, you run into a familiar face. %(bestfriendname)s, who you've known since you were born."
    if bestfriendgender == 1:
        "Just like always, he starts running along with you, to get to school as fast as possible."
    if bestfriendgender == 2:
        "Just like always, she starts running along with you, to get to school as fast as possible."
        
    bestfriendname"Yo, we're hanging out at MoonBucks after school today right? I've really been wanting to try their Blueberry Sour Latte."
    playername"Yeah, of course we are. We planned this out over the last few days remember? It was hard for me to convince my parents to let me go though."
    bestfriendname"They don't even know, do they?"
    playername"Nope. They think I have extracurricular activites after school."
    bestfriendname"You lying son of a bitch."
    bestfriendname"By the way, did you hear what those people on the news were saying about the nuke?"
    playername"Yeah, my dad was just telling me about it before I left."
    bestfriendname"Seems like a bunch of bullshit, don't you think?"
    playername"After what my dad said, yep. No way they're gonna nuke us."
    "As you both approach the school, there is a familiar feeling of sadness and hatred that grows stronger with every step you make."
    "Fortunately, you were late, which means you won't have to be in the school for as long."
    
        
    
    
    
    
    # This ends the game.


    pause
    return
