
define e = Character("Me")
define d = Character("Mister Detective")
define r = Character("Reporter")

label start:
    scene tv room
    with fade

    "Another dead body was found at the lake earlier this morning." 
    
    "Like the previous cases, the body was found with its mouth filled with newspapers."

    "Police says that they are doing their best to solve this case."

    e "WHAT. THE. HELL. It's exactly like how my favorite book goes."

    e "Is the killer reading the same book as me and they're trying to reenact each of the murder case in the book?"

    e "If I remember right, the next would be in the riverside. I'll check it out nothing bad will happen right?"

    scene book room
    with fade

    r "Following the eerie similarities of the recent killings, the police have started to look for clues surrounding you."

    r "What do you have to say to the people throwing allegations at you?"

    d "If they're able to imitate my book to this point, they're probably a super fan."

    d "It's kinda fun actually, to think they like me this much."

    scene mountain
    with fade 

    "Strolling through the riverside, you came across the infamous author."

    e "Huh? Thats's the author of my favorite book!"

    e "I'll go say hi."

    e "Hi mister! I just want to say I'm a super fan of your works."

    e "I love how each story is detailed and doesn't miss anything!"

    d "Oh, thank you. What's your favorite one?"

    e "That's hard but if I had to choose, I guess probably the one that similar to the killings right now."

    e "Oh! Don't worry, I know you're not the suspect."

    d "Thanks, kid. Everyones been accusing me of stuff I didn't do."

    e "No problem!, is it fine to ask for some advice? I'm trying to write a story like yours!"

    

    menu :
        d "Yeah sure, let's take a walk at the riverside while talking."
        "Thanks, let's go!":
            jump riverside
        "Oh, I actually have somewhere to be.":
            jump go home
        