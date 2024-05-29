label prlgue:

    scene bg city

    show tarina thinking

    u1 "Ta...na...rina... {b}{size=+10}Tarina!{/b}{/size}"
    # This can be either alerted or surprised.
    show tarina surprised with dissolve 
    # Just add in a delay here.
    show tarina neutral at left with dissolve and easeinright

    show friendA concerned with dissolve
    # Add another delay here later.
    show friendA concerned at right with dissolve and easeinleft

    u1 "Are you okay?"

    t "I'm... fine... just... thinking is all."
    
    show friendA concerned with dissolve

    u1 "You know we're friends right? You can talk to me if you're having a hard time trying to look for an internship."

    u1 "I know some people who would let you work for them if I asked them for a favour."

    show tarina grateful with dissolve

    t "I appreciate it, FriendA, really... I do."

    t "I know that we've always had each other's backs since our first year in the Academy."

    t "But there are times where we need to do things on our own."

    t "This is one of them."

    show tarina confident with dissolve

    t "Besides, I can't let my bestie owe someone else because of me."

    show tarina bigsmile with dissolve

    t "Watch, I'll get the best job in there is."

    t "Else, I won't be called Tarina the Stubborn at the Academy for nothing"

    show friendA sigh with dissolve

    f "You do realise that it's an insult right?"

    show friendA smile with dissolve

    f "Anyways this is me. Good luck with your job hunt."

    f "And remember..."

    show tarina annoyed with dissolve

    t "If I need help I should call you... Sure Mom!"

    scene bg secludedspot

    show tarina sigh with dissolve
    # Remind me to make this italics later.
    t "I say all of that to FriendA and here I am still jobless."
    
    t "Am I really that hopeless?"
    # She hits a pole here.
    "Bonk"

    show tarina hurt with dissolve
    
    t "Owwww... I should've been paying attention to where I was walking."

    t "Another lucky day for our heroine Tarina I guess..."

    "As she finally snaps out of her thoughts Tarina notices something weird."

    show tarina surprised with dissolve

    t "Why is it all quiet all of a sudden?"

    t "It's not even 3pm, yet I don't hear any sounds that are usually there in this city."

    scene bg alley

    "As she falls silent she is suddenly drawn to a nearby alleyway."
    # Play ominous music/sound here
    menu:
        "Should you follow your instinct and follow where the allyway goes to?"

        "Ignore it and go home":
            "You went home..."
            jump end1

        "Walk through the alleyway":
            "You followed went through the alleyway hoping for it to lead you somewhere."

    scene oldBuilding

    play music "oztheme.mp3"

    "As you walked through the alleyway you eventually come across a really old looking building."

    show tarina neutral at left with dissolve

    t "{i}Well this looks creepy... What's this creepy old building doing in a city known for innovation?{/i}"

    show oz silhouette with dissolve

    ou "The owner of that creepy old building is right here you know."

    show tarina surprised with dissolve

    t "{b}{size=+10}Gyaaaaaaaaah!!!{b}{/size}"

    show oz mischief with dissolve
    
    "A mysterious man shows up"

    show oz mischief at left with easeinleft

    ou "Hohohoo... what an interesting young lady."

    ou "Not only is she lively but she was easilly able to get passed the barriers that I have setup all over the place."

    show tarina breath with dissolve

    show tarina neutral with dissolve

    t "{i}That scared me... who's this old man? He said that he owned this building... What even is it?{/i}"

    ou "Oh my, do forgive me for my manners young lady. But you can call me Dr. Oz, a humble old wizard that owns this library."

    t "{i}Oz? Where have I heard of that name before? Wait a minute... Is he reading my mind?!?{/i}"

    o "Hohohoo! I wonder about that young lady. I shall let you think what you will."

    show tarina scream with dissolve

    t "{b}{size=+10}So he is reading my mind!!!{/b}{/size}"

    o "Fufuu... Well would you come inside? We can talk more about you needing that internship."

    show tarina guarded with dissolve

    t "Wait... How did you know that I needed one? I have never"

    o "Never mentioned anything and haven't even thought of it the moment you came close to my library?"

    show tarina surprised with dissolve

    o "Let's just say a dusty old crow told me."
    
    o "But let's not focus on that, I've been needing an assistant lately."

    o "And your timely arrival makes this the perfect opportunity for both you and me."

    o "I get an assistant that can liven up the library and you get my signature so that you can graduate"

    show tarina thinking with dissolve

    t "{i}He is making a good point. This can be an easy job for me to do so I can finally graduate.{/i}"

    t "{i}Urghhhh... It's annoying how this is literally something that I can't really ignore.{/i}"

    o "So, your response?"

    t "Alright alright! I'll at least hear you out."

    o "Splendid! Now follow me inside the library."

    scene bg libraryInside

    show tarina amazed at left with dissolve

    t "{i}This place is way too different on how it looks like outside{/i}"

    o "Welcome to my Grand Library. Breathtaking isn't it?"

    t "This is amazing how many books are even in this library?"

    show oz proud at right with dissolve

    o "Well I do believe that I have every book under the sun."

    o "The magic I used alone to expand this library to fit all of them took me copius amounts of time."

    t "Wait you're Dr. Oz of the Tea Party!!!"

    show oz amused with dissolve

    o "Well yes I do believe that is indeed one of the groups that I was part with."

    t "What are you even doing here? You're one of the greatest space and time wizards of all time!"

    t "You even created the space expansion magic used in magical bags and rooms used today!"

    o "I do believe I did study that on a whim because I wanted a library like this."

    o "Enough about me though... We should talk about your possible internship as my assistant here."

    show tarina determined with dissolve

    t "I accept!!!"

    show oz mischief with dissolve

    o "Fufuuu, while I do quite enjoy your enthusiasm about the job young lady, I really should explain what you are going into young lady."

    show tarina embarrassed with dissolve

    t "Yes! Sorry... Hehe."

    show oz smile with dissolve
    # Add a loud one clap like you're asking for attention.
    o "Onto the explaination then."

    o "But before that I should ask you this question."

    o "Do you hate cliches?"

    t "I... don't? While technically it gets boring the more it happens. But I'm fine with them."

    o "Well I hate them, it makes it predictable. Oh how I wish there is more variety in stories. That is where you as my assistant come in."

    o "As my assistant you will be required to not only help me arrange the books inside my library and study about the complexities and magic of the stories in these books."

    show tarina confused with dissolve
    
    t "Magic? Complexities?"

    o "Ah! Did I forget to mention that everything in this library has it's own unique magic?"

    o "Not only do they have their own magic. Each book is literally a new world of it's own."

    show tarina neutral with dissolve

    o "And your job is to study them by going inside and changing the stories with your presence."

    o "While I have tested the magic of these before we are technically going through uncharted magical territory here."

    o "This is unique magic that you would only be able to experience here."

    o "So, will you join me in this research of mine?"

    show tarina neutral with dissolve

    menu:
        "Will you become Dr. Oz's assistant?"

        "Deny the invitation":
            show tarina sad with dissolve
            t "Sorry Dr. Oz but I don't think I can do it."
            show oz disappointed with dissolve
            o "It's fine, good luck with your endeavours"
            jump end1

        "Accept the invitation":
            show tarina excited with dissolve
            t "It sounds interesting, I accept!"
            show oz mischief with dissolve
            o "Let's get started then."

    o "These are stories that I have read recently."

    o "Take your pick."

    menu:
        "Which world will you head in first?"

        "The Snow Queen":
                t "I'll pick this, this sounds cool, if I do say so myself!"
                show oz worry with dissolve
                o "Oh a quick warning before you head in."
                o "Do be careful when you go inside these worlds."
                o "We still don't have enough information about the magic these books have after all."
                show tarina smile with dissolve
                t "Don't you worry Doc!"
                t "I'll be back faster than you can say {i}'Winter is Coming'{/i}"
                jump snowqueenBook

        "Peter Pan":
                t "This will definitely be an adventure!"
                t "I'll pick this."
                show oz worry with dissolve
                o "Oh a quick warning before you head in."
                o "Do be careful when you go inside these worlds."
                o "We still don't have enough information about the magic these books have after all."
                show tarina smile with dissolve
                t "Have faith Doc!"
                t "I'll be back in a jiffy!"
                jump peterpanBook