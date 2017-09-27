label malechapter1:
    
    "..."
    "..."
    unknown"These violent delights have violent ends, %(playername)s."
    "...!"
    scene bg malebedroom
    with dissolve
    playername"(What the hell was that?)"
    "As you wake up, you hear a familiar voice shout for your name."
    show mom at right
    with dissolve
    mom"[playername]! You're gonna be late for school!"
    mom"Get dressed and eat breakfast now!"
    hide mom
    with dissolve
    scene bg black
    with fade
    play sound "clothes.mp3" 
    "You get dressed and go downstairs."
    stop sound fadeout 1.0
    
    scene bg kitchen
    with fade
    dad"Well, look who finally decided to wake up!"
    dad"I'm just messin, %(playername)s, you just took a while to wake up."
    mom"Anyhow, you're gonna be late to school, so eat your breakfast fast!"
    menu:
        "Eat breakfast with your parents. Risk being late.":
            jump malechapter1breakfast
        
        "Skip breakfast and leave for school.":
            playername"Sorry guys, I don't have any time to eat. I'm already way late for school."
            dad"That's exactly the reason why you're going to stay and eat breakfast with us. A few more minutes won't kill you. You're already late, anyway."
            jump malechapter1breakfast


        
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
    mom"[playername]! You're gonna be late for school!"
    mom"Get dressed and eat breakfast now!"
    hide mom
    with dissolve
    scene bg black
    with fade
    play sound "clothes.mp3" 
    "You get dressed and go downstairs."
    stop sound fadeout 1.0
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
            jump femalechapter1breakfast
        
label femalechapter1breakfast:

    "As you sit down to eat, you hear the TV new anchor blabber about rising tensions between the Sovereignity and the U.S."
    dad"Hey, %(playername)s, look at the crap they're feeding us on the news. They're saying that North Korea's gonna nuke us!"
    dad"No way they'd ever do it. Seriously. They know that if they did, we'd completely obliterate them."
    dad"Besides, haven't they ever heard of Mutually Assured Destruction?"
    jump fm1
    
label malechapter1breakfast:
    "As you sit down to eat, you hear the TV new anchor blabber about rising tensions between the Sovereignity and the U.S."
    dad"Hey, %(playername)s, look at the crap they're feeding us on the news. They're saying that North Korea's gonna nuke us!"
    dad"No way they'd ever do it. Seriously. They know that if they did, we'd completely obliterate them."
    dad"Besides, haven't they ever heard of Mutually Assured Destruction?"
    jump mm1
    
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
            jump femalechapter1toschool

label mm1:
    
    menu:
        "They said something about Sovereignity. What's that?":
            dad"C'mon kiddo, what're they teaching you in history? It's the North Korean-Russian alliance."
            dad"I should start looking for other schools maybe."
            jump mm1
            
        "What's Mutually Assured Destruction?":
            mom"Wow, they really aren't teaching anything in that school of yours! Should I have a parent-teacher conference?"
            dad"Let's just say that North Korea won't get a second chance to nuke us. You know, cause they're gonna be dead."
            jump mm1
            
        "I'm seriously gonna be so late for school. Thanks for the food mom. Bye!":
            mom"Have fun at school, sweetie!"
            dad"Tell your teachers to explain more things to you! If they don't then I definitely will!"
            jump malechapter1toschool

label femalechapter1toschool:
    scene bg road
    with fade
    "As you sprint towards your school, you run into a familiar face. %(bestfriendname)s, who you've known since you were born."
    if bestfriendgender == 1:
        "Just like always, he starts running along with you, to get to school as fast as possible."
    if bestfriendgender == 2:
        "Just like always, she starts running along with you, to get to school as fast as possible."
        
    bestfriendname"Yo, we're hanging out at MoonBucks after school today right? I've really been wanting to try their Blueberry Sour Latte."
    p"Yeah, of course we are. We planned this out over the last few days remember? It was hard for me to convince my parents to let me go though."
    bestfriendname"They don't even know, do they?"
    p"Nope. They think I have extracurricular activities after school."
    bestfriendname"You lying son of a bitch."
    bestfriendname"By the way, did you hear what those people on the news were saying about the nuke?"
    p"Yeah, my dad was just telling me about it before I left."
    bestfriendname"Seems like a bunch of bullshit, don't you think?"
    p"After what my dad said, yep. No way they're gonna nuke us."
    scene bg school at center with fade:
        easeout 5 xzoom 1.3 yzoom 1.3
        #ease 0.5 zoom 1.3
    
    "As you both approach the school, there is a familiar feeling of sadness and hatred that grows stronger with every step you take."
    "Fortunately, you were late, which means you won't have to be in the school for as long."
    bestfriendname"I really hate coming here. Hey, do you wanna ditch today, %(playername)s?"
    p"Probably not a good idea. I wouldn't be able to hang out after school."
    bestfriendname"Whatever man."
    "Even as you enter the school, you continue sprinting to get to class as soon as possible."
    if bestfriendgender == 1:
        "%(bestfriendname)s doesn't have the same class as you though, so you'll be seeing him later during snack time."
    if bestfriendgender == 2:
        "%(bestfriendname)s doesn't have the same class as you though, so you'll be seeing her later during snack time."
    "You run into class, feeling the sweat pour down your face from running so much."
    "As you make your way into the room, you try to catch your breath."
    teacher"You're late, [playername], how many more times until I have to send you to the office again? I'm getting sick and tired of dealing with you all the time."
    p"I'm sorry, Mr. Sharp."
    p"(I seriously hate this guy)"
    "You make your way to the front of the class, where your seat is located. Around you are your friends, Josh and Ericka."
    
    

label malechapter1toschool:
    scene bg road
    with fade
    "As you sprint towards your school, you run into a familiar face. %(bestfriendname)s, who you've known since you were born."
    if bestfriendgender == 1:
        "Just like always, he starts running along with you, to get to school as fast as possible."
    if bestfriendgender == 2:
        "Just like always, she starts running along with you, to get to school as fast as possible."
        
    bestfriendname"Yo, we're hanging out at MoonBucks after school today right? I've really been wanting to try their Blueberry Sour Latte."
    playername"Yeah, of course we are. We planned this out over the last few days remember? It was hard for me to convince my parents to let me go though."
    bestfriendname"They don't even know, do they?"
    playername"Nope. They think I have extracurricular activities after school."
    bestfriendname"You lying son of a bitch."
    bestfriendname"By the way, did you hear what those people on the news were saying about the nuke?"
    playername"Yeah, my dad was just telling me about it before I left."
    bestfriendname"Seems like a bunch of bullshit, don't you think?"
    playername"After what my dad said, yep. No way they're gonna nuke us."
    scene bg school at truecenter with fade:
       # linear 5 zoom 1.3
       ease 0.5 zoom 1.3
    
    "As you both approach the school, there is a familiar feeling of sadness and hatred that grows stronger with every step you take."
    "Fortunately, you were late, which means you won't have to be in the school for as long."