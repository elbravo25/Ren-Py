define t = Character('Tarina', color="#a5682a")
define f = Character('Freya', color= "#a5682a")
define n = Character("Narrator")
define ar = Character('Arianna', color= "#fbff04")
define a = Character('Anna', color="#c88333")
define ct = Character("Chief Troll")
define e = Character("Elsa")

image arianna normal:
    "arianna normal.png"
    zoom 0.75

label start:
    play music "audio/bgm_library.mp3"
    scene bg_library
    n "Browsing through an array of books, a certain title piqued Tarina’s eyes -- Frozen. A story of bond between two sisters."
    show tarina normal
    t "This seems like a good choice. A straightforward story should be easy to make more unique, right?"

    scene bg_sleeping
    n "Using book transmigration magic, she was able to possess Freya, a trusted character of the King and Queen of Arendelle."
    n "Of course, mere possession does not allow you to know whatever memories the body did have. As such, Tarina, now acting as Freya, is as fresh as a blank slate. Only knowing the plot of Frozen from her memories of reading its book from long ago."

    menu:
        "Search Drawer":
            jump search_drawer
        "Talk to maids outside":
            n "Freya went outside the room to look for someone who can give her more context on whose body is she in."
            jump talk_to_maids

label search_drawer:
    n "Freya found a book about Arendelle's Court."
    show freya normal at left
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
    show arianna normal at right
    with easeinright
    ar "Good morning, Lady Freya. Didn't expect you to be awake so early."
    show freya normal at left
    with easeinleft
    f "Good morning... Arianna, is it? Please, forgive me, but I seem to be experiencing a slight headache and my memory feels a touch hazy. Perhaps you could refresh my recollection."

    menu:
            "Get tea":
                show freya normal at left
                f "Thank you, dear Arianna, that would be most kind."
                show arianna normal at right
                ar "Got it. I shall send some tea to your room right now. Ah, but please do hurry because His Majesty will be waiting for you for your meeting with the Weseltons later."
                f "I see. So Lady Freya is some kind of a diplomat for the King."
                jump throne_room
            "No":
                show freya normal at left
                f "No thank you, Arianna, I think I just need a refresher."
                f "Now, about my duties... what are some pressing matters that require my attention today? Will you give me a refresher?"
                show arianna normal at right
                ar "Well, there's a meeting with the emissaries from Weselton this afternoon to discuss the upcoming trade agreement. His Majesty values your diplomatic skills in these negotiations."
                f "I see. So Lady Freya is a trusted diplomat for the King. I hope he does not notice the changes."
                f "Weselton, you say? Is there any particular history or tension between our kingdoms that I should be aware of?"
                ar "Oh, not really, Lady Freya. Though, their trade representative, Duke Hans, can be a bit... slippery at times. But I'm sure you can handle him!"
                f "Hans... the villain of Frozen..."
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
    play music "audio/bgm_throne.mp3"
    scene bg_throne

    "Navigating through the large palace is no easy feat. Unlike the Lancaterossa, where magical signage are readily available, the palace of Arendelle is literally a maze. Hundreds of windows, doors, and rooms."

    "Thankfully, I was able to find the meeting room on time."

    "Meeting talks about going to Weselton for trade, as well as looking for a cure for 'extreme cold'."

    "Duke of Weselton suggested going to Antollahan, the mysterious glaciers in the North jokingly, pertaining to a well-known legend in his lands."

    "After the meeting"

    "The King and Queen of Arendelle are considering going there by Fall, as they still have several matters to do in the Kingdom."

    "Freya remembers that those very glaciers are the reason why Elsa and Anna's Parents died. It was due to the severe storm that acted up during the fall."

    menu:
        "Suggest a different date":
            "The King and queen go to the North during the Summer"
            "Killed by bandits along the way"  # Quotes added here
            "The children's mental health were highly affected"  # Quotes added and typo fixed
            jump time_skip
        "Let the story flow as it was written":
            jump time_skip

label time_skip:
    scene bg_thronewithice

    "Anna tries to cheer up the young, gloomy Elsa by playing with her."

    "Anna gets struck by ice to her heart and gets placed into a critical condition."

    "All the kingdom's physician, doctor, nor apothecary could not unfreeze Anna's heart."

    "As a legal guardian of the two, what should you do?"

    menu:
        "Take Anna to the Trolls":  # Quotes added here
            "Anna was taken to the Trolls"
            jump troll_time

label troll_time:
    scene troll_forest

    "Troll’s Forest: Dusk"

    "Trolls. As jolly and fun as they are in the books, is a complete 180 against from what I know from the book."

    "These creatures... they are hiding something else..."

    "The forest is dimly lit, glowing mushrooms providing an eerie luminescence."

    "FREYA stands anxiously beside a large, rocky outcrop where ANNA lies unconscious."

    "A hulking CHIEF TROLL with a single, glowing eye approaches Freya."

    ct "(Booming voice) The magic is a fickle thing, little advisor. It takes time to mend."
    f "(Forced smile) Thank you, Chieftain. I understand. But Anna is still a child.  Wouldn't it be best for her to recover in the castle, surrounded by loved ones?"
    ct "(Chuckles, a sound like rocks grinding together) Love can be a curious illness, advisor. Here, with the mountain's magic, she will heal truly."
    "Freya glances at Anna, worry etched on her face."
    f "But how long will it take?"
    "The Chief Troll leans in close, his single eye gleaming."
    ct "(Voice low) As long as it takes. The mountain's magic works in mysterious ways."
    "Freya steps back, a cold dread pooling in her stomach. Something is wrong here."
    "This isn't the clumsy kindness of the trolls she's read about. This is something else entirely."

    menu:
        "Take Anna away after the initial treatment":
            "Troll’s Forest: Day"
            "Weeks have passed since Anna's injury. The dim cave glows with unnatural light from strange runes etched on the walls.  Anna lies on a stone slab, seemingly peaceful, but pale and fragile."
            "Freya stands vigilantly beside her, a growing suspicion hardening her gaze."
            ct "(Booming voice) Patience, advisor. The mountain's magic works slowly, but surely. Soon, the little princess will be stronger than ever."
            "Freya forces a smile, her eyes lingering on the runes. "
            f "Slowly, you say?"  
            f "It's been weeks. Shouldn't Anna be showing more improvement?"
            ct "The mountain's magic has its own rhythm, advisor. It cannot be rushed."
            "Freya's unease deepens. Something feels off about this 'healing'"
            "Her hand brushes against a hidden pouch at her hip, a small comfort in this unsettling place."
            f "(Voice firm) Perhaps a change of scenery wouldn't hurt. Fresh air, familiar surroundings..."
            ct "(Scoffs) Leaving now would disrupt the delicate balance!  The princess needs the mountain's power."
            "Freya closes her eyes for a fleeting moment, a surge of determination coursing through her. Taking a deep breath, she focuses on the magic residing within her, a gift from Tarina."
            "A soft blue glow emanates from her fingertips. The trolls gasp in surprise. Freya ignites another spark of magic, her voice ringing out."
            f "(Voice firm) Anna is coming with me. The castle healers can complete her recovery."
            "The Chief Troll throws back his head and roars with laughter, a booming sound that echoes through the cavern."
            ct "You, a mere advisor, wield magic?  Foolish! The mountain's power dwarfs yours!"
            "He lunges towards Freya, but she reacts with surprising speed.  Freya extends her hand, the blue glow intensifying."
            "A surge of magical energy erupts from her fingertips, knocking the Chief Troll back and sending smaller trolls scrambling."
            f "(Shouts to Anna) Come on, Anna! We're leaving!"
            "Freya rushes to Anna's side, gently lifting her.  With a determined look in her eyes, Freya weaves another quick spell, creating a shimmering blue bubble around them."
            "This magical shield protects them from any potential attacks as they race towards the cave entrance."
            "Anna receives a mild brainwashing spell"
            jump throne_roomday
        "Let Anna stay with the trolls":
            "Freya stands beside the unconscious Anna, a conflicted expression etched on her face.  The Chief Troll looms nearby, a smug glint in his single, glowing eye."
            f "(Sighs) Very well, Chieftain. I entrust Anna to your care."
            "(Inner thoughts:)  I understand now, perhaps my presence... my interference... has complicated the healing process."
            "Freya's voice carries a hint of self-blame, a subtle way to express her internal struggle."
            "The Chief Troll's smile widens."
            ct "A wise decision, advisor. The mountain will take good care of her."
            "Freya reaches out and gently strokes Anna's hair, a flicker of sadness in her eyes."
            f "(Softly) Get well soon, Anna.  I'll... I'll be back for you."
            "She forces a small smile at the Chief Troll, masking the unease churning in her gut."
            f "When can I expect to see her again?"
            "The Chief Troll's smile turns sly."
            ct "(Vague) The mountain works in its own time, advisor. Patience is a virtue."
            "Freya nods tightly, a knot of worry tightening in her chest.  She casts one last look at the sleeping Anna, then turns and walks resolutely towards the forest entrance."
            f "(To herself) Perhaps the stories haven't gotten it entirely right. But I'll find a way. I have to."
            "Freya exits the forest and the silence of the forest looms over."
            jump backto_palace

label backto_palace:
    scene bgthrone_roomday

    "Sunlight streams through the tall arched windows of the throne room. The moon had long left the sky and the dawn had already set in when Freya arrived back to the throne room of Arrendelle."

    "Across from her stands Elsa, with her expression heavy with worry."

    e "ELSA (Voice trembling) Freya… where is Anna?"

    "Freya takes a deep breath, steeling herself for the difficult conversation."
    
    f "(Softly) Elsa…  I took Anna to the trolls."

    "Elsa's frown deepens, confusion clouding her features."

    e "The trolls? Why?"

    f "(Hesitates) Her injuries… the magic… the trolls possess a unique healing power."

    e "(Standing abruptly) But they said it would only take a few days! It's been weeks, Freya! Weeks!"

    "Decision Point:  Freya must choose a difficult truth."

    menu:
        "Tell the Truth":
            "Freya clenches her fists, bracing herself for the emotional fallout."
            f "The truth is, Elsa... The trolls say the magic… it's… it's taking longer than expected. They… they can't guarantee when Anna will be back."
            "Elsa's face pales, her eyes widening in horror."
            e "(Voice breaking) No… no, this can't be happening. It's my fault… I hurt her!"
            "Elsa stumbles back, tears welling in her eyes. She collapses onto a nearby chair, burying her face in her hands, wracked with sobs."
            "Freya rushes to her side, her heart heavy with guilt and sorrow."
            jump coronation_day
        "Tell a Lie":
            "Freya knows the truth could destroy Elsa.  A desperate plan forms in her mind."
            "(WARNING: This path is emotionally manipulative)"
            f "(Voice with false sympathy) There's… there's something else I need to tell you. She hesitates, then blurts out, Anna… she… she didn't make it."
            "Elsa gasps, a look of pure horror contorting her face.  Freya steels herself for the inevitable breakdown, but instead, a chilling calm descends upon Elsa."
            e "(Voice Icy) Anna… is gone?"
            f "(Nods, tears welling in her own eyes) Yes…"
            e "(Stands slowly, her voice devoid of emotion) Then I have much work to do. Arendelle needs a strong Queen. For Anna."
            "Elsa turns away from Freya, her eyes burning with an unsettling intensity. Freya watches her go, a wave of nausea washing over her."
            "The weight of the lie hangs heavy in the air, a chilling reminder of the price of her deception."
            jump coronation_day

label coronation_day:
    scene bgthrone_roomday

    "Years passed and coronation came, but her sister never did. No consolation nor accomplishment could ease the guilt of Elsa’s heart for killing her parents and leading her sister to death."
    "This, alongside her imminent powers had turned her into a literal ice queen, freezing half the kingdom exactly after being crowned."
    "With her sister gone, she sees no reason to live nor let others live. Arendelle became a kingdom of ice and death."
    "Elsa thanks everone, and especially Freya for being there. On the surface, it seems like she has the power on the kingdom, but the truth is you have the queen under your fingers. You became the shadow queen of Arendelle."

label throne_roomday:
    scene bgthrone_roomday

    "Sunlight streams through the tall windows, illuminating dust motes dancing in the air. Relief washes over ELSA's face as the grand oak doors creak open."
    "Freya enters, supporting a frail ANNA. Anna leans heavily on Freya, her face pale and drawn."
    e "(Rushing forward) Anna!  Thank goodness you're alright!"
    "Elsa engulfs her sister in a tight embrace, tears welling in her eyes.  Anna sways slightly, her voice weak but oddly cheerful."
    a "(Winces) Easy there, Elsa! Still a little sore from all that mountain climbing, wouldn't you say, Freya?"
    "Freya offers a strained smile, her eyes lingering on Anna with concern."
    f "Indeed. The trolls put her through quite the… rigorous recovery process."
    "Anna pulls back from the hug, her gaze flitting around the room with an unsettling intensity."
    a "(Giggles) Rigorous? More like invigorating!  The mountain air, the… challenges… they made me stronger, Elsa! We have to be strong, you know!"
    "Elsa frowns slightly.  Anna's usual vibrancy seems muted, replaced by a forced cheerfulness."
    e "(Gently) Stronger?  That's wonderful, Anna. But you look exhausted.  Come, let's get you to your chambers."
    a "(Waves a dismissive hand) Nonsense! Just a bit winded from that exciting escape, wouldn't you agree, Freya?"
    "Freya forces another smile, her unease growing."
    f "(Carefully) Perhaps a small rest before anything else, Anna?"
    a "(Pouts playfully) Rest? But there's so much to do! We need to be prepared for anything, Elsa!"
    "Anna's voice takes on a new edge, a hint of something unfamiliar lurking beneath the surface. Elsa steps closer, her brow furrowed."
    e "Prepared for what, Anna?  Tell me."
    a "(Eyes gleaming) For anything, Elsa! The mountain taught me that! We can't be weak! We have to be strong!"
    "Anna clenches her fists, a strange intensity radiating from her frail form."
    "Freya shivers involuntarily.  This is not the carefree Anna they remember."
    f "(Clears throat) The mountain… it can be a harsh teacher, Anna. Perhaps some rest will allow you to process everything…"
    a "(Scoffs) Process?  Nonsense!  I'm clear-eyed now, more than ever! We must show our strength, Elsa!  Arendelle needs a strong queen!"
    "Anna's gaze flickers to the throne behind Elsa, a flicker of ambition momentarily replacing the forced cheer."
    "Elsa's eyes narrow, a flicker of suspicion replacing the initial relief."
    e "(Voice firm) Anna, you're not well. You need rest. We'll discuss everything later. Freya, please help Anna get settled."
    a "(Beams) Of course, Elsa!  But don't worry, I won't be out for long! Stronger than ever, ready to face any challenge!"
    "Anna throws Elsa a dazzling smile, a touch too wide and practiced.  Before Elsa can respond, Freya ushers her out of the throne room.  Elsa watches them go, a knot of worry tightening in her stomach."
    "The joyous reunion has been tainted by a disturbing undercurrent."
    




            



                
  