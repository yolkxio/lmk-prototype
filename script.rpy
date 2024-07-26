# The script of the game goes in this file.
# Welcome to the code for Mystic Monkey Makeout Supreme! The prototype for the LEGO Monkie Kid Dating Sim!
# This code was made by yolk (@yolk.xio on insta)... I really don't know why I'm saying this, no one's gonna see this like... ever
    # I'll try to be more descriptive with my comments in the next game, but if you see this and have any questions please reach out!!
init:                   ### INITIALIZING CODE ###
    #characters
    define protag = Character("Y/N", color="#b9ba8a")
    define mk = Character("MK", color="#a14d45")
    define mei = Character("Mei", color="#49a13d")

    #backgrounds
    image protagroom = Image("protag_room.png")
    image rooftop = Image("protag_roof.png")
    image mainstreet = Image("megopolis_streetview.png")
    #image meishall = Image("hall_mei.png")
    image fade2black = Solid("#000000")
    image bad_end = Image("bad_end.png")
    image best_end = Image("best_end.png")
    image golden_end = Image("golden_end.png")
    image weird_end = Image("weird_end.png")

    #variables
    default soda = False
    default gun = False
    default mk_bond = 5
    default mei_bond = 5
    default meta_counter = 0
    default mei_streamies = False

label start:            ### INTRO SCENE ###

    scene fade2black
    "Tucked away somewhere in Megapolis, a young protagonist finishes the first few steps to beginning a new chapter of life..."
    pause 1.0
    scene protagroom with fade
    
    protag "Aaaaaannnd THAT should be the very last box!"
    
    "you feel the folded cardboard between your fingers as you look around at your new room, organized perfectly. You take a second to reflect on the long journey that led you to this exact moment."
    "..."
    "interrupting this tranquil thought, you feel all of the adrenaline that's been keeping you going these past few days finally drain away, your shoulders sag and you exhale."
    
    protag "Wow I feel... so exhausted... I should reward myself and take the evening to do absolutely nothing."
    
    "Luckily, the landlord gives residents rooftop access, that would be the perfect spot to relax and take in the scenery of your new home, Megapolis."

    menu:
        "What will you bring to accompany you on your small trip?"
        "a can of soda":
            jump .soda
        "a gun":
            jump .gun

    label .soda:
        $ soda = True
        play sound "can-opening.mp3"
       
        protag "Nothing like something sweet to refresh myself with while I relax!"
        jump .leaveroom
    
    label .gun:
        play sound "pistol-cock-6014.mp3"
        $ gun = True 

        protag "Nothing like the feeling of a gun in my hand to help me feel safe while I relax!"
        jump .leaveroom

    label .leaveroom:
        "Once you've grabbed your keys, you head out the door and go upstairs."
        scene fade2black with dissolve
        jump rooftop1

label rooftop1:         ### SCENE TWO ### 

    show rooftop with fade
    "When you get up to the rooftop, you discover it peacefully empty. Taking a deep breath, you look around and take in the view around you."
    
    "The sun beginning to set is paired with the buzz of cars and people in the distance, making Megapolis feel like a living and breathing creature."
    
    if soda:
        protag "This is the best feeling ever... But it would be nice to share the moment with someone."
        "You take a sip of your fizzy drink and sigh, sitting down by the edge of the roof."
    if gun:
        protag "This is the best feeling ever... Just me, my GUN, and I... If anyone tries to talk to me right now they won't know what hittem"
        "You cock your gun again and sigh, sitting down by the edge of the roof."

    "Suddenly, as you were just getting comfortable, you hear a loud rumbling sound rapidly approaching you."
    "Before you can even react, a golden burst of light floods your eyes and a loud {b}BAM{/b} rings in your ears!! LOOK OUT!!!"
    protag "WOA- WHAT THE- "
    "As the smoke clears, you see a figure emerge from the pile of rubble"
    show mk default at left
    "???" "Oh sorry! I didn't see you there, are you alright?"
    
    if gun:
        protag "HOLY SHIT WHAT THE FUCK "
        "Suddenly, years of weapon training kick in and you point your weapon right at him"
        show mk o_o
        protag "WHO ARE YOU"
        show mk angy
        "???" "WH- IS THAT A GUN??? ARE YOU SERIOUSLY POINTING A GUN AT ME RIGHT NOW?!?!"
        "the figure in front of you takes out his phone and begins to make a phone call. This action shocks you so much that you don't even react."
        show mk angy_talk
        "???""Hey- Red? Yeah there's a situation- mhm- nono... yeah, with a gun. right... yup, no, not going anywhere... okay"
        "the figure hangs up and turns to look at you"
        show mk angy
        "???""pray to whatever gods you believe in, heathen"
        "Before you can respond, you hear the sound of an engine humming, as you turn towards the sound, you see a large flying vehicle with at least one complex transformation hurtling towards you!!"
        scene bad_end
        play sound "chainsaw.mp3"
        "You got: {b}the bad ending{/b}... death by Red Son"
        return

    if soda:
        protag "Woah crazy!!"
        "You stand up and approach the crater where the figure is."
        protag "Are you alright??"
        "???""Yeah, thanks for asking! and it's great that you didn't do anything crazy like pull out a gun on me! hahaha!"
        protag "Haha thanks.."
        "That sounded really specific, has that happened before? And speaking of really specific events..."
        protag "Also... what.. what just happened? Who are you?"
        show mk morty_face
        "the figure seems slightly taken back by this question, but he still responds"
        show mk default
        mk "I'm MK! Protector of Megapolis!"
        "as he says this he smiles and strikes a little pose"
        protag "Well, something tells me we're all clear over here, no protection needed"
        "he exaggeratedly looks around, running a hand through his hair"
        mk "Ah, it's always good to check, just in case. Wouldn't want anyone to have to fight demons on their own!"
        "It seems surprising that he landed here on purpose, given the nasty landing and... property damage"
        protag "Do you always stick the landing like that?"
        "MK laughs, but his eyes dart away anxiously"
        mk "Well... not always"
        jump .pressure_apply

    label .pressure_apply:
        "You get the feeling that he might not want to talk about this"
        menu:
            "ask anyways":
                $ mk_bond -= 1
                "you try to lighten the mood, but you're still too curious to let it go"
                protag "Are you sure you didn't just get smacked over here by a demon yourself?"
                show mk sad
                "mk lets out a laugh that feels a bit forced"
                show mk default
                mk "nono, it's a bit embarassing but i actually tripped on the way over, i always forget to tie my shoes haha!"
                "you glance down and find that his shoes are, as stated, untied"
                "in fact, his whole outfit looks pretty ratty, like he just rolled through some mud.. or concrete (idk guys work with me here)"
                show mk sad
                protag "Well, maybe you should be a bit more careful next time"
                show mk default
                mk "yeah i will, thanks!"
                protag "so, i guess this is a habit of yours then.. are you some kind of hero with powers then?"
                "MK really does seem surprised by the fact that you keep asking about him"
                jump .mk_intro

            "topic change": 
                $ mk_bond += 1
                "you shift the subject of the conversation to something that might not be too personal"
                protag "Protector of Megapolis, huh? So.. do you have powers then?"
                "he looks grateful for the topic change and smiles, seemingly at ease"
                mk "yeah, I do! Monkey King powers!"
                "he picks up the staff from the rubble (you didn't notice it) and gives it a twirl. You nod, impressed but also a bit lost."
                jump .mk_intro
        
    label .mk_intro:
        show mk confused_talk
        mk "Wow, you really don't know who I am, huh?"
        "you shake your head"
        show mk default
        mk "Well, I am technically the city's sole protector!! I'm uh- I'm kind of a big deal...Usually people have heard of me"
        "he holds up his staff and gestures around a bit"
        show mk morty_face
        protag "Oh well- I mean, I did just move here- like- two days ago. So I'm not too familiar with... local protectors"
        "MK looks a bit embarrassed upon hearing this, but quickly brightens up"
        show mk default
        mk "well- welcome to Megapolis! The best city to live in because I'm here to protect every citizen! promise! "
        "after thinking for a moment, he appears to grow a bit self conscious"
        show mk bashful
        mk "i hope that first impression wasn't too terrible"
        "you laugh"
        show mk default
        protag "it wasn't, don't worry"
        mk "ah- well that's good to hear"
        mk "Anyways, I clear up any demons and ghouls who try to cause trouble, so let me know if you see anything suspicious, evil, or dangerous, alright?"
        "clearing up demons with your powers for an entire city? that sounds..."
         
        menu:
            "that sounds awesome!":
                protag "that's crazy cool man! you must be living the dream out there!"
                show mk bashful
                "mk laughs again and rubs the back of his neck bashfully"
                show mk default
                mk "haha yup! i always liked the Monkey King, and now i get to be just like him!... Pretty uh- pretty epic"
                "you laugh and think about how fun this MK guy is, he seems worth keeping around"
                "you think of some other ways to continue the conversation"
                jump .the_offer

            "that sounds tough!":
                $ mk_bond +=1
                protag "that sounds like a lot of work, you make sure you take care of yourself too, okay?"
                show mk bashful
                "he seems surprised by your words, searching your face for a second before glancing away"
                show mk default
                mk "Ah don't worry about me, I'm the Monkey Kid! I can handle anything!"
                show mk bashful
                mk "I appreciate that though, thanks for looking out for me, man."
                protag "yeah of course"
                show mk default
                "you smile, and there's a moment of comfortable silence"
                pause 0.5
                "MK seems like good company, you think about some way to continue this pleasant feeling."
                jump .the_offer

            "that sounds lame...":
                $ mk_bond -= 1 
                protag "wow, you really just focus on demons all day? sounds... pretty lame, can't lie."
                show mk sad
                "MK looks a bit shocked by this, you see a flicker of hurt before he covers it up with an offended look"
                show mk confused_talk
                mk "well- psh- you go try to fight demons and see how well that goes!"
                "you don't really have a good comeback"
                menu: 
                    "maybe i will!":
                        protag "maybe i will go fight a demon! I'm sure it'll go well"
                        "mk huffs and mutters something"
                        pause 1.0
                        "you don't really have anything else to say... there's a beat of uncomfortable silence"
                    "i bet i'd do better than you":
                        $ mk_bond -= 1
                        protag "i bet i'd do better than you, seeing how you can't even stick a landing"
                        "mk scoffs and crosses his arms, muttering something"
                        pause 1.0
                        "you don't really have anything else to say... there's a beat of uncomfortable silence"
                "you think maybe your comments were uncalled for, you barely even know the guy"
                "you search for some way to resolve the tension"
                jump .the_offer

    label .the_offer:
        show mk default
        mk "wheellpp- it's been nice meeting you, but I'll get out of your hair now-"
        "what- he's leaving so soon?"    
        menu:
            "wait- don't go!":
                jump .obvious_choice
            "ok bye shart":
                hide mk 
                $ meta_counter += 1
                "hey.. wtf are u doing bruv"
                "you know this is a dating sim... and you know you have to like... romance the main characters"
                pause 1.0
                "yeah did you even think about that? what's gonna happen if you just let MK go right now? it'd probably be weeks before you just {i}happen{/i} to bump into each other again"
                "do you know how much work that would be for me?"
                menu:
                    "ask him not to go":
                        "(thank you, jeez..)"
                        jump .obvious_choice
    label .obvious_choice:
        show mk default at left
        protag "wait-"
        "Looking at MK, you recall that he did crash into a thick floor of concrete. Hero or not, that's gotta leave some scrapes."
        "You notice a few spots on his palms that seem pretty scraped up"
        protag "Do you want to come to my apartment for a quick second? We can get you cleaned up a bit and i can get you something to drink?"
        if mk_bond > 6:
            jump .soft
        else:
            jump .okay
        
    label .soft:
        "mk smiles warmly, he seems genuinely touched by this"
        mk "yeah, that'd be great. you're really nice"
        jump .regular

    label .okay:
        "mk smiles, but it seems mostly out of politeness"
        mk "that's very kind of you, I'll just stay for a moment."
        jump .regular

    label .regular:
        "you nod and stand up, waiting for him to follow you down the stairs and back to your place"
        scene fade2black with dissolve
        jump bedroom_two
        
label bedroom_two:      ### SCENE THREE ###
    scene protagroom with fade
    "when you return, you bring mk into the kitchen area"
    protag "wait here, i'll get some bandages and antiseptic"
    show mk default at left
    mk "you got it, boss!"
    if mk_bond > 6:
        $ mk_bond +=1
        "mk hops up on the counter, swinging his feet. he seems to have had no problem getting comfortable"
        "watching this makes you pause for a moment"
        protag "actually... do you want anything to drink before i go?"
        "mk looks over and brightens up"
        mk "yeah! i'll take anything sugary"
        "you look into the fridge, there's a few options..."
        menu:
            "what do you grab?"
            "peach ramune":
                $ mk_bond += 1
                "you reach into the fridge and pull out a bottle of peach ramune, mk seems delighted and is opening the bottle before you even close the fridge"
                mk "thanks man!"
                jump .after_bandages

            "water":
                $ mk_bond += 0 
                "you reach into the fridge and pull out a bottle of water, mk laughs"
                mk "i guess it is important to stay hydrated"
                jump .after_bandages

            "vegetable juice":
                $ mk_bond += 0
                "you reach into the fridge and pull out a bottle of vegetable juice, mk pulls a face and laughs"
                mk "trying to make sure i eat my greens? you're like my dad"
                "you turn away to hide your smile"
                protag "whatever"
                jump .after_bandages

    label .after_bandages:
        "you get some medical equipment from the bathroom, coming back to help mk wipe off his hands"
        "the vibes are good, and soon enough mk's hands are covered in cutesy little band-aids (per his request)"
        protag "aaannd you should be all good now!"
        mk "thanks! i feel totally healed up!"
        pause 0.5
        mk "You know, you've been a great help, I really appreciate it"
        mk "Would you like to hang out with me and a friend tomorrow? We're gonna go to the arcade and play a bunch of cool games and all that. It'll be a blast!"
        mk "What do you say?"
        protag "That sounds fun! You can catch me there for sure"
        "mk lights up at this and exchanges his number with you as he gets ready to leave."
        mk "I really think you'll like my friend, she's great- like you!"
        "You smile"
        protag "I can't wait, see you tomorrow, then"
        "you wave as he walks down the hall and you close the door"
        hide mk
        "you take a second to think about everything that just happened- so much for doing nothing the rest of the night!"
        "mk seems like he could be a really valuable friend. You can't wait to socialize with him tomorrow, maybe he can show you some other parts of Megapolis, or introduce you to even more people!"
        "honestly, that whole interaction wiped away any nerves you had about integrating into your new home, seems like the people here are truly kind!"
        pause 0.5
        "you get ready to settle in for the night, but you still have some time to kill and aren't totally sleepy yet."
        menu:
            "Is there anything in particular you wan't to do?"
            "watch some tv":
                $ mk_bond += 1
                "watching a little bit of tv before bed sounds like a great idea!"
                "you sit down and turn the tv on."
                "before you can begin flipping through channels, you notice something interesting on the news cast before you"
                "the headline reads: The great monkey kid saves the day again omg thats craazyy"
                protag "omg thats craazyyy"
                protag "well, that proves that he wasn't... like a wacko or whatever"
                "you end up staying on that channel, watching a video of MK from earlier today."
                "As he dodges demons from his floating cloud, you are filled with admiration for this guy! You really can't wait to get to know him better"
                pause 1.0
                "After a while, you feel your eyelids grow heavy, so you cut off the tv and go to bed. As you drift to sleep, you think about.. a.. plastic.. yellow dude with uh.. idk... u think ab him wow gay"
                jump .night_night
            "watch a stream":
                $ mei_streamies = True
                "watching a stream or two sounds like a great way to wind down before bed!"
                "you get comfortable in your bed and open your laptop, scrolling through some of the nearby streamers. One of the most popular livestreams at the moment seems to be a product review from \"(insert cool streamer tag for mei here)\". You click on it."
                "You see a girl chatting about some sneakers she's been wearing for a sponsorship, talking about how stylish they made her look while beating up bad guys... maybe she's also a protector of Megapolis? How many heroes are there???"
                "You decide that you really like her bubbly energy, and you stick around for a few hours until you're too tired to watch anymore."
                "Rolling over, you think of.... something gay.. before you sleep... idk... idk what normal ppl use to help them fall asleep or smthn i daydream ocs kissing im built different like that" 
                jump .night_night
            "nah go to bed":
                "Why would I do anything when I can just go to bed. Bed is life"
                "You go to your lovely comfortable bed, getting nice and cozy up under there"
                protag "yeaaahh this is the life"
                "this \nis \nthe \nlife"
                "you promptly fall asleep"
                jump .night_night

    label .night_night:
        "zzz"
        scene fade2black with fade
        "..."
        "END OF DAY ONE"
        "..."
        "(guys i did it holy shit i coded a whole day yippee)"

    jump day_two


label day_two:          ###SCENE ONE DAY TWO###

    return

