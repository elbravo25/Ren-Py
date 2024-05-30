
image Arianna neutral:
    "Arianna neutral.png"
    zoom 0.75

label snowqueenBook:   
    scene bg FreyaBedroom
    play music "sleepingqtheme.mp3"

    n "Using book transmigration magic, she was able to possess Freya, a trusted character of the King and Queen of Arendelle."
    show freya neutral with dissolve
    n "Of course, mere possession does not allow you to know whatever memories the body did have. As such, Tarina, now acting as Freya, is as fresh as a blank slate. Only knowing the plot of The Snow Queen from her memories of reading its book from long ago."

    menu:
        "Search Drawer":
            jump search_drawer
        "Talk to maids outside":
            n "Freya went outside the room to look for someone who can give her more context on whose body is she in."
            jump talk_to_maids

label search_drawer:
    n "Freya found a book about Arendelle's Court."
    show freya neutral at left
    with easeinleft
    "Freya opens the book."

    "About Freya:
    Freya wasn't born into nobility, 
    but her exceptional intellect and calm 
    demeanor earned her a respected 
    position as an advisor to the King and 
    Queen of Arendelle.  She arrived at the
    castle relatively young, her past 
    shrouded in a veil of mystery.

    Freya possesses a natural talent for 
    diplomacy."  
    
    "She can navigate complex 
    court politics, mediate disagreements 
    between the royal family and foreign 
    dignitaries, and offer insightful counsel 
    on matters of state.  Her calm and collected
    personality allows her to remain composed 
    even in the most stressful situations."

    "Freya: I guess this is the information about this body. I should get going now..."
    jump leave_room

label talk_to_maids:
    scene bg CastleHallway
    show Arianna neutral at right
    with easeinright
    ar "Good morning, Lady Freya. Didn't expect you to be awake so early."
    show freya neutral at left
    with easeinleft
    f "Good morning... Arianna, is it? Please, forgive me, but I seem to be experiencing a slight headache and my memory feels a touch hazy. Perhaps you could refresh my recollection."

    menu:
            "Get tea":
                show freya neutral at left
                f "Thank you, dear Arianna, that would be most kind."
                show Arianna normal at right
                ar "Got it. I shall send some tea to your room right now. Ah, but please do hurry because His Majesty will be waiting for you for your meeting with the Weseltons later."
                f "I see. So Lady Freya is some kind of a diplomat for the King."
                jump throne_room
            "No":
                show freya neutral at left
                f "No thank you, Arianna, I think I just need a refresher."
                f "Now, about my duties... what are some pressing matters that require my attention today? Will you give me a refresher?"
                show Arianna neutral at right
                ar "Well, there's a meeting with the emissaries from Weselton this afternoon to discuss the upcoming trade agreement. His Majesty values your diplomatic skills in these negotiations."
                f "I see. So Lady Freya is a trusted diplomat for the King. I hope he does not notice the changes."
                f "Weselton, you say? Is there any particular history or tension between our kingdoms that I should be aware of?"
                ar "Oh, not really, Lady Freya. Though, their trade representative, Duke Hans, can be a bit... slippery at times. But I'm sure you can handle him!"
                f "Hans... the villain of The Snow Queen..."
                f "Slippery, you say? Very well, I shall approach this meeting with cautious optimism."
                jump ask_more

label ask_more:
    menu:
            "Thank her":
                f "Thanks, Arianna. I really appreciate it!"
                ar "No problem, Lady Freya!"
                jump leave_room
            "Ask her more":
                f "Is there anything else I should be aware of regarding my role here in the castle?"
                ar "Mostly just keeping His Majesty and the Queen on track. Are you truly alright Lady Freya? Should I call the royal physician?"
                f "No! (Panicked, then composes herself). There is no need for that, I am doing just fine. Then, I’ll be going now."
                jump leave_room

label leave_room:
    n "Freya leaves the room."
    jump throne_room

label throne_room:
    play music "throneroom.mp3"
    scene bg ThroneRoom

    "Navigating through the large palace is no easy feat. Unlike the Lancaterossa, where magical signage are readily available, the palace of Arendelle is literally a maze. Hundreds of windows, doors, and rooms."

    "Thankfully, I was able to find the meeting room on time."

    "Meeting talks about going to Weselton for trade, as well as looking for a cure for 'extreme cold'."

    "Duke of Weselton suggested going to Antollahan, the mysterious glaciers in the North jokingly, pertaining to a well-known legend in his lands."

    "After the meeting"

    "The King and Queen of Arendelle are considering going there by Fall, as they still have several matters to do in the Kingdom."

    "Freya remembers that those very glaciers are the reason why Ella and Alma's Parents died. It was due to the severe storm that acted up during the fall."

    menu:
        "Suggest a different date":
            "The King and queen go to the North during the Summer"
            "Killed by bandits along the way"  # Quotes added here
            "The children's mental health were highly affected"  # Quotes added and typo fixed
            jump time_skip
        "Let the story flow as it was written":
            jump time_skip

label time_skip:
    scene bg thronewithice
    play music "throneroom.mp3"

    "Alma tries to cheer up the young, gloomy Ella by playing with her."

    "Alma gets struck by ice to her heart and gets placed into a critical condition."

    "All the kingdom's physician, doctor, nor apothecary could not unfreeze Alma's heart."

    "As a legal guardian of the two, what should you do?"

    menu:
        "Take Alma to the Trolls":  # Quotes added here
            "Alma was taken to the Trolls"
            jump troll_time

label troll_time:
    scene troll_forest

    play music "enchantedforest.mp3"

    "Troll’s Forest: Dusk"

    "Trolls. As jolly and fun as they are in the books, is a complete 180 against from what I know from the book."

    "These creatures... they are hiding something else..."

    "The forest is dimly lit, glowing mushrooms providing an eerie luminescence."

    "FREYA stands anxiously beside a large, rocky outcrop where Alma lies unconscious."

    "A hulking CHIEF TROLL with a single, glowing eye approaches Freya."

    ct "(Booming voice) The magic is a fickle thing, little advisor. It takes time to mend."
    f "(Forced smile) Thank you, Chieftain. I understand. But Alma is still a child.  Wouldn't it be best for her to recover in the castle, surrounded by loved ones?"
    ct "(Chuckles, a sound like rocks grinding together) Love can be a curious illness, advisor. Here, with the mountain's magic, she will heal truly."
    "Freya glances at Alma, worry etched on her face."
    f "But how long will it take?"
    "The Chief Troll leans in close, his single eye gleaming."
    ct "(Voice low) As long as it takes. The mountain's magic works in mysterious ways."
    "Freya steps back, a cold dread pooling in her stomach. Something is wrong here."
    "This isn't the clumsy kindness of the trolls she's read about. This is something else entirely."

    menu:
        "Take Alma away after the initial treatment":
            "Troll’s Forest: Day"
            "Weeks have passed since Alma's injury. The dim cave glows with unnatural light from strange runes etched on the walls.  Alma lies on a stone slab, seemingly peaceful, but pale and fragile."
            "Freya stands vigilantly beside her, a growing suspicion hardening her gaze."
            ct "(Booming voice) Patience, advisor. The mountain's magic works slowly, but surely. Soon, the little princess will be stronger than ever."
            "Freya forces a smile, her eyes lingering on the runes. "
            f "Slowly, you say?"  
            f "It's been weeks. Shouldn't Alma be showing more improvement?"
            ct "The mountain's magic has its own rhythm, advisor. It cannot be rushed."
            "Freya's unease deepens. Something feels off about this 'healing'"
            "Her hand brushes against a hidden pouch at her hip, a small comfort in this unsettling place."
            f "(Voice firm) Perhaps a change of scenery wouldn't hurt. Fresh air, familiar surroundings..."
            ct "(Scoffs) Leaving now would disrupt the delicate balance!  The princess needs the mountain's power."
            "Freya closes her eyes for a fleeting moment, a surge of determination coursing through her. Taking a deep breath, she focuses on the magic residing within her, a gift from Tarina."
            "A soft blue glow emanates from her fingertips. The trolls gasp in surprise. Freya ignites another spark of magic, her voice ringing out."
            f "(Voice firm) Alma is coming with me. The castle healers can complete her recovery."
            "The Chief Troll throws back his head and roars with laughter, a booming sound that echoes through the cavern."
            ct "You, a mere advisor, wield magic?  Foolish! The mountain's power dwarfs yours!"
            "He lunges towards Freya, but she reacts with surprising speed.  Freya extends her hand, the blue glow intensifying."
            "A surge of magical energy erupts from her fingertips, knocking the Chief Troll back and sending smaller trolls scrambling."
            f "(Shouts to Alma) Come on, Alma! We're leaving!"
            "Freya rushes to Alma's side, gently lifting her.  With a determined look in her eyes, Freya weaves another quick spell, creating a shimmering blue bubble around them."
            "This magical shield protects them from any potential attacks as they race towards the cave entrance."
            "Alma receives a mild brainwashing spell"
            jump throne_roomday
        "Let Alma stay with the trolls":
            "Freya stands beside the unconscious Alma, a conflicted expression etched on her face.  The Chief Troll looms nearby, a smug glint in his single, glowing eye."
            f "(Sighs) Very well, Chieftain. I entrust Alma to your care."
            "(Inner thoughts:)  I understand now, perhaps my presence... my interference... has complicated the healing process."
            "Freya's voice carries a hint of self-blame, a subtle way to express her internal struggle."
            "The Chief Troll's smile widens."
            ct "A wise decision, advisor. The mountain will take good care of her."
            "Freya reaches out and gently strokes Alma's hair, a flicker of sadness in her eyes."
            f "(Softly) Get well soon, Alma.  I'll... I'll be back for you."
            "She forces a small smile at the Chief Troll, masking the unease churning in her gut."
            f "When can I expect to see her again?"
            "The Chief Troll's smile turns sly."
            ct "(Vague) The mountain works in its own time, advisor. Patience is a virtue."
            "Freya nods tightly, a knot of worry tightening in her chest.  She casts one last look at the sleeping Alma, then turns and walks resolutely towards the forest entrance."
            f "(To herself) Perhaps the stories haven't gotten it entirely right. But I'll find a way. I have to."
            "Freya exits the forest and the silence of the forest looms over."
            jump backto_palace

label backto_palace:
    scene bgthrone_roomday
    play music "throneroom.mp3"

    "Sunlight streams through the tall arched windows of the throne room. The moon had long left the sky and the dawn had already set in when Freya arrived back to the throne room of Arrendelle."

    "Across from her stands Ella, with her expression heavy with worry."

    e "Ella (Voice trembling) Freya… where is Alma?"

    "Freya takes a deep breath, steeling herself for the difficult conversation."
    
    f "(Softly) Ella…  I took Alma to the trolls."

    "Ella's frown deepens, confusion clouding her features."

    e "The trolls? Why?"

    f "(Hesitates) Her injuries… the magic… the trolls possess a unique healing power."

    e "(Standing abruptly) But they said it would only take a few days! It's been weeks, Freya! Weeks!"

    "Decision Point:  Freya must choose a difficult truth."

    menu:
        "Tell the Truth":
            "Freya clenches her fists, bracing herself for the emotional fallout."
            f "The truth is, Ella... The trolls say the magic… it's… it's taking longer than expected. They… they can't guarantee when Alma will be back."
            "Ella's face pales, her eyes widening in horror."
            e "(Voice breaking) No… no, this can't be happening. It's my fault… I hurt her!"
            "Ella stumbles back, tears welling in her eyes. She collapses onto a nearby chair, burying her face in her hands, wracked with sobs."
            "Freya rushes to her side, her heart heavy with guilt and sorrow."
            jump coronation_day
        "Tell a Lie":
            "Freya knows the truth could destroy Ella.  A desperate plan forms in her mind."
            "(WARNING: This path is emotionally manipulative)"
            f "There's… there's something else I need to tell you. She hesitates, then blurts out, Alma… she… she didn't make it."
            "Ella gasps, a look of pure horror contorting her face.  Freya steels herself for the inevitable breakdown, but instead, a chilling calm descends upon Ella."
            e "(Voice Icy) Alma… is gone?"
            f "(Nods, tears welling in her own eyes) Yes…"
            e "(Stands slowly, her voice devoid of emotion) Then I have much work to do. Arendelle needs a strong Queen. For Alma."
            "Ella turns away from Freya, her eyes burning with an unsettling intensity. Freya watches her go, a wave of nausea washing over her."
            "The weight of the lie hangs heavy in the air, a chilling reminder of the price of her deception."
            jump coronation_day

label coronation_day:
    scene bgthrone_roomday

    "Years passed and coronation came, but her sister never did. No consolation nor accomplishment could ease the guilt of Ella’s heart for killing her parents and leading her sister to death."
    "This, alongside her imminent powers had turned her into a literal ice queen, freezing half the kingdom exactly after being crowned."
    "With her sister gone, she sees no reason to live nor let others live. Arendelle became a kingdom of ice and death."
    "Ella thanks everone, and especially Freya for being there. On the surface, it seems like she has the power on the kingdom, but the truth is you have the queen under your fingers. You became the shadow queen of Arendelle."

label throne_roomday:
    scene bgthrone_roomday
    play music "throneroom.mp3"

    "Sunlight streams through the tall windows, illuminating dust motes dancing in the air. Relief washes over Ella's face as the grand oak doors creak open."
    "Freya enters, supporting a frail Alma. Alma leans heavily on Freya, her face pale and drawn."
    e "(Rushing forward) Alma!  Thank goodness you're alright!"
    "Ella engulfs her sister in a tight embrace, tears welling in her eyes.  Alma sways slightly, her voice weak but oddly cheerful."
    a "(Winces) Easy there, Ella! Still a little sore from all that mountain climbing, wouldn't you say, Freya?"
    "Freya offers a strained smile, her eyes lingering on Alma with concern."
    f "Indeed. The trolls put her through quite the… rigorous recovery process."
    "Alma pulls back from the hug, her gaze flitting around the room with an unsettling intensity."
    a "(Giggles) Rigorous? More like invigorating!  The mountain air, the… challenges… they made me stronger, Ella! We have to be strong, you know!"
    "Ella frowns slightly.  Alma's usual vibrancy seems muted, replaced by a forced cheerfulness."
    e "(Gently) Stronger?  That's wonderful, Alma. But you look exhausted.  Come, let's get you to your chambers."
    a "(Waves a dismissive hand) Nonsense! Just a bit winded from that exciting escape, wouldn't you agree, Freya?"
    "Freya forces another smile, her unease growing."
    f "(Carefully) Perhaps a small rest before anything else, Alma?"
    a "(Pouts playfully) Rest? But there's so much to do! We need to be prepared for anything, Ella!"
    "Alma's voice takes on a new edge, a hint of something unfamiliar lurking beneath the surface. Ella steps closer, her brow furrowed."
    e "Prepared for what, Alma?  Tell me."
    a "(Eyes gleaming) For anything, Ella! The mountain taught me that! We can't be weak! We have to be strong!"
    "Alma clenches her fists, a strange intensity radiating from her frail form."
    "Freya shivers involuntarily.  This is not the carefree Alma they remember."
    f "(Clears throat) The mountain… it can be a harsh teacher, Alma. Perhaps some rest will allow you to process everything…"
    a "(Scoffs) Process?  Nonsense!  I'm clear-eyed now, more than ever! We must show our strength, Ella!  Arendelle needs a strong queen!"
    "Alma's gaze flickers to the throne behind Ella, a flicker of ambition momentarily replacing the forced cheer."
    "Ella's eyes narrow, a flicker of suspicion replacing the initial relief."
    e "(Voice firm) Alma, you're not well. You need rest. We'll discuss everything later. Freya, please help Alma get settled."
    a "(Beams) Of course, Ella!  But don't worry, I won't be out for long! Stronger than ever, ready to face any challenge!"
    "Alma throws Ella a dazzling smile, a touch too wide and practiced.  Before Ella can respond, Freya ushers her out of the throne room.  Ella watches them go, a knot of worry tightening in her stomach."
    "The joyous reunion has been tainted by a disturbing undercurrent."
    "Sunlight streams through stained glass windows, casting colorful patterns on the polished stone floor.  Freya carefully helps Alma walk through the castle hallway, her brow furrowed with concern."
    a "(Huffs slightly) This castle is like a giant ice sculpture! Everything's so… cold."
    f "(Chuckles softly) Perhaps. But it is home, Alma. You just need some time to adjust after… everything."
    "Freya casts a worried glance at Alma.  Although physically weak, a strange energy crackles beneath the surface."
    a "(Stops abruptly, turning to Freya) Adjust? Why should I adjust? I'm stronger now, Freya. The mountain showed me that!"
    f "(Places a gentle hand on Alma's arm) Stronger, yes. But you also look exhausted. Rest is important, Alma."
    a "(Pushes Freya's hand away, a flicker of anger in her eyes) Rest? No time for that! Ella… she needs to understand. We can't be weak anymore, Freya!"
    f "(Concerned) Ella understands that you were injured, Alma. She just wants you to recover."
    a "(Scoffs) Recover? I am recovered! Stronger than ever! But Ella… she's still clinging to her silly weakness! Arendelle needs a strong queen, Freya!"
    "Alma's voice takes on a new edge, a hint of ambition replacing her usual playful demeanor. Freya's concern deepens."

    menu:
        "Dissuade Alma":
            "Freya worries about the growing tension between the sisters. She decides to gently remind Alma of Ella's struggles."
            f "(Sighs) Alma, listen to me. Ella has carried a heavy weight for a long time. She may not always show it, but she cares deeply about you. Perhaps a gentler approach…"
            a "(Crosses her arms, her voice laced with defiance) Gentle? The mountain showed me the dangers of weakness! Ella needs to be strong! Arendelle needs a strong queen!"
            "Alma's eyes gleam with a disturbing intensity that makes Freya shudder."
            f "(Places a hand on Alma's shoulder) Strength comes in many forms, Alma. Ella's strength lies in her love for you, for Arendelle. She's been through her own struggles, her own battles."
            a "(Scoffs) Battles? Playing princess in her ice palace? No, Freya. The mountain showed me real strength, real power! We can't afford Ella's… weakness… any longer."
            "Freya's concern deepens. Alma's words sound harsh, manipulative. There's something wrong here."
            f "(Voice firm) Alma, the mountain's magic can be… unpredictable. Perhaps it's clouded your judgment. Trust me, Ella is strong, in her own way."
            a "(Pulls away from Freya, a flicker of anger flashing in her eyes) Don't patronize me, Freya! I see things clearly now! Ella needs to learn from the mountain's power, just like I did!"
            "Alma throws Freya a challenging look, then continues walking down the hallway, her steps surprisingly steady despite her earlier weakness. Freya watches her go, a knot of worry tightening in her stomach."
            "The 'recovery' at the mountain has left Alma changed, and not for the better. Freya knows she needs to get to the bottom of this, for Alma, for Ella, for Arendelle."
            jump coronation_dayy
        "Be an understanding adult":
            "Freya understands Alma's frustration after her ordeal. She decides to show empathy and offer support."
            f "(Takes a deep breath) I understand your frustration, Alma. You've been through a lot. It's natural to feel… different after such an experience."
            a "(Pouts slightly, her earlier anger replaced by a forced cheer) Different? I wouldn't say different, Freya. More… aware. The mountain opened my eyes."
            f "(Offers a gentle smile) I'm sure it did, Alma. And it's wonderful that you feel stronger. But trust me, Ella wants nothing more than for you to be healthy and happy. Perhaps, when you're feeling better, you two can talk about it."
            a "(Sighs dramatically) Talk, talk, talk. Ella's always so serious, wouldn't you agree, Freya? She needs someone who understands true strength, someone who can face any challenge!"
            "Alma throws Freya a pointed look, a hint of manipulation lurking beneath the surface. Freya hesitates, a flicker of unease crossing her features."
            f "(Carefully) Ella is strong, Alma. In her own way."
            a "(Waves a dismissive hand) Oh, I'm sure she is, in her own… way. But wouldn't it be better if she were strong… like us, Freya? Strong like the mountain made me?"
            "Alma leans in close to Freya, her voice dropping to a conspiratorial whisper."
            a "We can help her, Freya. You and I. We can show her the true meaning of strength. Wouldn't that be wonderful?"
            "A cold dread pooling in your stomach. The innocent, carefree girl she once knew seems to have vanished, replaced by someone… else. Someone who sees Freya as a potential ally, a means to an unsettling end."
            jump coronation_dayy

label coronation_dayy:
    scene Ella_chamber
    # Change later maybe?
    play music "sleepingqtheme.mp3"

    "Weeks have flown by in a flurry of preparations. The once-The Snow Queen kingdom hums with renewed life. It is Ella's coronation day! The windows are open, and so are those doors that never did before."
    "Eight thousand salad plates, halls filled with festivities and ballroom excited for the balls. Finally, the guards have opened up the gates. The sun was looking bright but far beyond the horizons a cold icy storm brews."

    "Sunlight streams through a newly opened window, casting a warm glow on Ella's chambers. The room is bustling with activity. Maids scurry about, arranging flowers and straightening tapestries."
    "Freya carefully adjusts the crown on Ella's head, a worried expression etched on her face"
    f "(Holds the jeweled crown) There. Perfect. You look absolutely regal, Ella."
    "Ella stares at her reflection in the mirror, her face a mask of unease."
    e "(Voice trembling) Regal, maybe. But do I look like a queen?"
    f "(Places a hand on Ella's shoulder) Of course you do! A magnificent one. You were born for this, Ella."
    e "(Turns away, a shiver running down her spine despite the warm sunlight) I don't know, Freya. It all feels… so cold. The crown, the responsibility… even the weather."
    "A gust of wind whistles through the newly opened window, sending chills through the room. Ella closes the window with a sigh."
    f "(Chuckles nervously) Just pre-coronation jitters, Ella. Everyone has them. Even the most seasoned rulers."
    e "(Glances out the window) Maybe. But where is Alma? I haven't seen her all morning amidst the chaos."
    "A shadow of concern flickers across Freya's face. She forces a smile."

    menu:
        "Assure Ella 'Alma is probably just having fun out there' (Downplays the issue): (Choose this option if you want Freya to try and calm Ella's anxieties)":
            f "Alma is probably just having fun out there, Freya assures her. She can't wait to celebrate you becoming Queen."
            jump coronation_time
        "Look for Alma":
            f "I should look for her,"
            "Freya suggests, a flicker of worry in her eyes."
            f "She wouldn't miss this for anything."
            "Oddly enough, Freya was not able to find Alma anywhere in the castle, as well as some of the guards. Where could have they gone to when an event as important as a coronation is happening"
            jump coronation_time

label coronation_time:
    scene  throne_room
    play music "throneroom.mp3"

    "Sunlight streams through stained glass windows, casting colorful patterns on the polished stone floor.  Choir voices soar, filling the air with a joyous melody.  Guests from all over Arendelle, adorned in their finest attire, fill the pews."
    "Anticipation crackles in the air. This is the day Arendelle welcomes their new queen: Ella."
    "Ella stands at the altar, a magnificent crown adorning her head.  Her once pale face is flushed with a mixture of nervousness and determination. Freya stands vigilantly by her side, a worried look etched on her face."
    "Weeks have passed since Alma's strange behavior, and Freya has yet to find an explanation. A nagging suspicion continues to gnaw at her."
    p "(Raises his hands, his voice booming through the chapel): By the power vested in me, I declare you, Ella of Arendelle, Queen of this sovereign nation! May your reign be long and prosperous!"
    "A thunderous applause erupts from the crowd. Ella takes a deep breath, trying to quell the flutter of fear in her heart.  She lifts her chin, a look of resolve hardening her features. This is it. This is her new beginning."
    "Suddenly, the massive oak doors of the chapel burst open. A hush falls over the crowd. All eyes turn towards the entrance, where Alma stands, flanked by several armed guards. Her usual bright smile is replaced by a cold, determined expression."
    a "(Voice ringing out, silencing the choir) Hold your applause! There will be no coronation today!"
    "Ella's heart plummets. Freya's hand tightens around Ella's arm, her eyes widening in alarm. This is not the joyous reunion they had hoped for."
    a "The people of Arendelle deserves a true leader, not a… a monster!"
    "Murmurs of confusion ripple through the crowd. Ella stares at Alma, her mind reeling. What is she doing?"
    a " Ella… my own sister… is a witch! The accusation hangs heavy in the air, a bomb dropped in the middle of the coronation ceremony. Gasps of shock erupt from the crowd. Ella stares at Alma, betrayal and hurt flashing in her eyes."
    a "She has used her dark magic to control us all! But no more! Seize her!"
    "The guards surge forward, their weapons glinting in the sunlight. Chaos erupts in the chapel. Ella stands The Snow Queen, The Snow Queen by a mixture of shock and disbelief. This isn't happening. This can't be happening."

    menu:
            "Calm Ella Down":
                f "(Grasping Ella's arm firmly but gently) Your Majesty, you need to come with me. This isn't safe! We can talk about this later, but right now, we need to get you out of here."
                e "(Having a panic attack)"
                a "I guess this is the side that you are taking, Freya. To aid with the witch."
                f "You are insane."
                a "You are more insane for protecting that murderer. She murdered our parents. Guards, seize them!"
                "As the guards approach, several vassals blocked their paths."
                v "Milady, you must run, we will hold them off."
                

            "Argue with Alma":
                f "(Stepping forward, voice laced with disbelief) Alma! What are you doing? This isn't you! Explain yourself right now!"
                e "Stop..."
                a "I am doing what needs to be done. That person is not my sister."
                f "How could you say that!"
                e "Please, stop..."
                a "She is the reason why I almost died. It is thanks to the mountains why I am alive and kicking, but if not I would have been a The Snow Queen corpse like that witch wants."
                e "(screams) ENOUGH!"
                "Ella froze half of Arendelle due to her rampant emotions."
                jump argue

            "Accuse Ella":
                f "All this time, you were a witch!"
                e "(Confused) What are you saying, Freya? You have always known about my powers."
                f "Liar!"
                a "Hahaha! What an interesting turn of events!"
                e "Stop! Please stop. This is all just a dream. This is all just a dream. Calm down. Conceal. Don’t feel it."
                a "You hear that everyone? Queen Ella is still trying to hide it!"
                pp "Kill the witch! Kill the witch!"
                "Freya sided with Alma and left the losing team. It was a practical choice."

label fight_flee:
    scene throne_room
    # Add suspense filled bgm

    "You were given the choice to Fight or Flee, what will you choose?"

    menu:
            "Fight":
                f "No. I won’t run, when I know I can do something. Watch me young Queen, as magic is not always bad."
                "Freya used her magic to conjure a blast of lightning against the guards incapacitating them. Everyone gasps."
                e "A witch! The adviser is a witch!"
                jump argue_blame
            
            "Flee":
                f "Hurry your majesty! Before they catch you!"
                a "Kill them"
                "Ella receives a throwing knife to her wrists. She cannot conjure ice anymore."
                e "Run, Freya. Just run."
                "Ella sacrifices herself for you"

label argue_blame:
    scene throne_room

    "You have 2 options, to argue or to take the blame. Which one will you choose?"
    menu:
        "Argue":
                "You chose to argue with Alma."
                jump argue

        "Take the blame":
                f "HAHAHA! You are all correct. I am the witch of Arendelle. I killed the king and queen of this country."
                f "I cursed the appointed Queen Ella to be able to conjure Ice in this cold and dark lands. It took you long enough you fools!"
                a "(looks baffled) Ha, you can’t be serious!"
                pp "KIll the witch! Kill the witch!"
                f "“That reaction, I sense brainwashing magic”"
                f "I command thee, spirit of mana, to sever the anomaly manifesting upon this woman."
                "Freya used a high level dispel magic to cure Alma which promptly sent her to sleep. Conversely, Freya is struggling to stay awake."
                g "The witch has taken down the princess. Kill the witch!"
                e "No! Stop! She is not evil!"
                pp "Evil! Evil!"
                jump blame_ending
            
label argue:
    scene throne_room

    f "Magic is not an evil thing, it is just like air that has always been with us."
    e "(Looked at Freya with teary eyes)"
    a "Shut up, both of you are witches! They must have conspired to kill the king and queen! Do not listen to their words!"
    "The guards and people stampeded towards Ella and Freya. Of course, not wanting to hurt the people, both merely defended their own body than to retaliate."
    "Freya and Ella have been executed. Alma lived as the new queen with her new panel of entourage, several boulders appeared to visit my humble abode."

label blame_ending:
    scene throne_room
    "Like a grand sacrifice you took the blame to help Erin or a racing game"








    




            





    




            



                
  