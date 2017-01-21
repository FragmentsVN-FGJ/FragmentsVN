# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chris")

define o = Character("Old man")

define a = Character("Amy")

define b = Character("Beatrice")

define B = Character("Beautiful woman")

define bq = Character("Beatrice ???")

define p = Character("Priest")

define d = Character("Dealer")

define f = Character("Flying sine wave")

define cos = Character("Flying cosine wave from the Fifth Dimension")

define sin = Character("Flying sine wave from the Fifth Dimension")

define g = Character("Guard")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene radio

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    c "Where's my mic? You've got one job, right!?"

    o "Sorry, sir, I was busy. Here it is."

    c "Why is every morning like this?"

    c "How much time left?" 
    
    "The balding man before me is speed-reading the paper containing his lines."

    o"Fifteen seconds."

    c "Aah, damnit! I'm getting too old for this."

    o "Three... two... one... go!"

    c "Good morning, listeners! It's 8.00 am, April 26th, and according to the weather report it's going to be sunny with a pleasant breeze. Get those surfing boards ready! "
    "Before we get to the daily selection, it's time for some local news..."
    "I watch the statistics on the array of screens in front of me. It's my job to make everything run smoothly, not that anyone can see that." 
    "You only know the value of something once it's gone, I guess."

    "Well, this is still an improvement on my last job."

    "A rather boring day of looking at music lists and carrying errands culminates at 4pm, when I'm solemnly released from duty."

    "Finally. Thank god it's Friday."

label bar:
    scene bar

    "After a hard day's work, I decide to hit the bar before going back home. Ever since the new bartender was hired a few weeks ago, I've been coming here daily. You know, it's nothing dirty or anything, she just knows how to fix a drink!"
    
    a "How may I serve, sir?"
    
    "Amy asks the question with a playful smile. She's not exactly the servile type, I know that already. It's probably just a company lineshe's forced to say, but somehow she's managed to turn it into her own little in-joke."

    c "I'll take a Snow White."

    a "You sure you don't want something more manly? Here, I'll make you a Jagerbomb!"

    c "Well, it is Friday, I guess. Hit me up with that."

    "Amy's pretty young, in her early twenties, I think. With her looks and positive attitude, it's no surprise she got hired." 
    "Still, she seems like the type of girl who wants to do something with her life. You know, instead of toiling her life away at some random bar in a small seaside village."

    "Suddenly, someone walks in and takes one of the seats at the desk. I can tell she's not one of the usual patrons." 
    "She's wearing an elaborate dress that seems suitable neither for this climate nor for this bar."
    " But damn is she beautiful. She has a long curly hair, and the scent of flowers hangs around her."

    menu:
        "Welcome the newcomer":

            c "Hey, I haven't seen you here before! New in town?"

            "She looks at me a bit incredulously. Did my sudden advance make her uncomfortable? I sigh in relief inwardly as she breaks out a smile."

            B "No, I'm actually a regular. I recently inherited a flower shop around here. Here's my card."

            "I glance at the name in the business card."

            c "Beatrice? Wow, your name sounds so refined!"

            b "Thank you. Come and visit later, won't you? I really want to keep the store, but there aren't that many customers. Just a few older ladies."

            "Finishing her Snow White, she stands up."

            b "It was a pleasure talking to you."

        "Better not disturb her":

            "The woman orders a Snow White, not really talking to anyone. There's an aura of contemplative sadness around her, and it seems to push away any potential suitors. She finishes her drink and leaves."

            a "Beato is unhappy as always, huh?"

            c "Beato?"

            "Amy smiles."

            a "That's her name. Beatrice."

            "A beautiful name for a beautiful woman, I see."

            a "She's got a flower store in town, but I hear it's doing pretty badly. She's kind of a loner."

            c "You seem to know her pretty well."

            "Amy rejects my hypothesis, looking a bit uncomfortable."

            a "I mean, she comes here often. But I don't really get her. I would never want to spend the rest of my life alone in some shop totally off the map!"

            "I guessed as much. She gradually grows more excited as Beatrice's influence wanes."

            a "Yeah! I wanna see the world, you know, travel and get to know new people, get new experiences, that sorta stuff! Once I've got enough savings, I'll try to get a degree in journalism, or..."

            "I pretend to pay attention, but get lost in thoughts, staring at her lips."

label cliff:
    scene cliff

    "A pleasant breeze blows towards me as I cycle up and down the hills. The sun is about to set, but I still feel warm, perhaps due to the workout." 
    "Cycling home through the countryside has been one of the few remaining passions in my life ever since I moved to this island."
    "I'm approaching a familiar cliff with an amazing view of the ocean. Sometimes I come here in the evenings to watch the blazing sun sink under those peaceful waves."
    "I stop my bike at the cliff. From this angle, the cliff is hidden from view by the vegetation."
    "I jump over the guard rails and walk down a well-trodden path of trampled grass, arriving at the cliff."

    "The view is beautiful as usual. In front of me, the sky is red with the descending sun."
    " However, this time something is different. There is an intruder in my sanctuary. "
    " A woman in a flowing white dress is standing right at the edge of the cliff with her back turned towards me, gazing wistfully at the ever-rolling waves."
    " Suddenly I recognize her. It's Beatrice." 
    "What is she doing here? And how did she find her way here?"

    menu:
        "Wave and try to catch her attention":
            c "Hey, Beatrice! Over here!"
            
            "I try to catch her attention, but she appears to be too deep in her thoughts to hear me. I slowly approach her from behind."
            "I'm right behind her now. I can smell the floral perfume emanating from her curly hair."

            c "Beautiful view, eh?"

            "She is startled by my sudden whisper, and before I can react in any way, her foot slips -- "
            "-- and she falls, falls, falls! I try to grasp her, but my movements are too slow."
            "In a split second, screaming, she disappears under the black waves." 
            "And in the silent air, long after she is gone, I can still hear her scream."

        "Observe her passively":

            "Maybe it's better not to disturb her. I stay in the shadows of the trees, trying to keep quiet." 
            "She keeps staring at the waves, but her eyes are glazed over and empty. Just what is she thinking of...?"

            "Then, one moment, and she disappears into thin air--" 
            "That's my first impression, until I realize what has happened." 
            "I can barely catch a glimpse of her wavy hair vanishing under the cliff. One step, and she is gone." 
            "I stay there, sitting under the trees, and all I can see is that one curl of hair."

label grave:
    scene grave
    
    "I was invited to her funeral, maybe because I was the only one of the locals who had gotten close to her. "
    "Still, I feel like an outsider here, among the grieving faces of her family, all of them strangers."

    "It's raining. To me, the drops seem like soft tears falling from a darkened heaven. It certainly doesn't make me feel any better."
    "After all, I am the reason she died. It was all. My. Fault."

    "As the priest is giving the funeral speech -- I can barely hear his voice as background noise to the welter of my thoughts" 
    "My gaze flits unconsciously from attendee to attendee. And slowly, slowly I realize that my eyes have fixated on someone."
    "I'm looking at someone from behind. It's a woman wearing a flowing white dress."
    "Perhaps that is what caught my attention, everyone else is wearing something suitably depressed."
    "But no, I'm looking at her long, curly hair." 
    "There's a faint voice within me, trying to tell me something, but at first I'm too lost in depression to hear."

    menu:
        "You know her":
            "Wait. I know her. It can't be!" 
            "Explanations race through my mind: a twin sister, mother, it was all a nightmare, this is all a nightmare, clones, aliens..."
            "Beatrice!"

    menu:
        "Run to interrogate her!":

            "I run to her, disturbing the procession. Everyone is looking at me now, faces mixed with shock and apprehension, but I couldn't care less."

            "And as I see her face, as I look into those cerulean eyes, wide with surprise or with terror, my suspicions are confirmed. It *is* her!"

            c "Beatrice! How can you be alive? I saw you, I saw you fall..."

            bq "... Do I know you, sir?"

            c "What do you mean? Of course you do..."

            "The inital shock of the crowd around me is slowly turning to annoyance, to anger, and I can feel the pressure from their silent stares."

            "The priest is slowly trying to continue his speech, unsure of what to do."

            "If Beatrice is here, at her own funeral, then who is in the coffin?"

            "I walk over to the coffin. Nobody stops me."

            "And I look at the corpse, lying quietly on the red cushions."

            "No..."

            "Beatrice slowly walks behind me, and whispers in my ear."

            b "This is not my funeral. It's yours."

        "Just keep watching...":

            "It's better not to cause a ruckus. I keep my gaze fixed on the strange apparition before me." 
            "I'm beginning to doubt my sanity. It cannot be her. This is her funeral!"

            "But then, for just a moment, she turns her head so I can see those cerulean eyes. And then I am certain. It is her."

            "All my sorrow has vanished, replaced by total confusion." 
            "It is as if the world around me was collapsing around me, crushing me under my crumbling sense of reality. What is going on?"

            "I sit and stare, unable to do anything but. The priest's words envelope me subconsciously, even though I can't pay attention to them anymore."
            "But suddenly, something he says piques my interest. It takes me a while to realize what he said." 
            "My name."

            p "Though he had only recently moved here, he was liked by all..."

            "The realization slowly dawns on me."
            " This is not Beatrice's funeral."
            " It is mine."

label beach:
    scene beach
    
    "Woohoo! I shift my weight forward, causing the board to swerve left. "
    "The sun is really hot today, but I've been falling into the water all day, so it's bearable. Splash! There I go again." 
    "Speaking of hot, I can see Amy surfing some really big waves in the distance."
    "Unlike me, she hasn't fallen once the entire day. Her style is breathtaking."

    "If only she didn't laugh every time I fall."
    "Not that I mind making her laugh. Better than being boring."
    "Amy paddles closer to me on her board, laughing at my misery as usual. Come on girl, don't be so mean!"
    "I can't stay angry at that figure, though! Especially not with that bikini..."

    a "Hahaha, you fell again!? Hope it didn't hurt!"

    c "Eh, I can handle it."

    "Why am I pretending to be so macho, anyway?"

    a "Wanna try something harder? I can teach you my super-secret board jump move! It's really cool!"

    c "Erm, I don't know if I'm ready, oh master..."

    "Still, a strange sense of bravery is starting to well up within me. I do kinda want to try something harder already."

    menu:
        "Do the super-secret board jump move":
            "The idea makes my heart pump, but all my fears are being drowned by crazy courage. I'll show her!"

            "She guides me deeper into the ocean, into an area with colossal, periodic waves."

            a "Okay, just wait for a reaaallly big one! Here it comes!"

            "As the wave comes, I go through the usual motions: first on my knees, then..." 
            "Stand! It feels difficult, but somehow, I manage to surf the wave."

            a "Just remember my instructions! Now!"

            "With a shift of weight, I flip the board under me and jump into the air! I'm doing it!" 
            "I'm, uh, falling into the water as usual." 
            "Damn. So much for that."

            "Except the waves are really huge out here. I'm starting to wonder if this was the brightest idea."

            "Gulp. Gasp! I can't... air..."

            "The sounds of the gushing waves and Amy's shouting seem to be coming from somewhere far away as I keep sinking beneath."


        "Maybe I'll just practice a bit closer to the shore":

            "Common sense overcomes me. No way I'm ready for that."

            a "Oh, you're no fun!"

            "Amy's disappointment makes me blush and reconsider, but to be perfectly honest, I'm kinda terrified of those waves."
            "Amy paddles back into the deeps, ready to surf again."

            "Well, I guess there's nothing to do but practice. I relax for a while in the waters nearer to the shore." 
            "The sand and rocks caress the soles of my feet. It feels quite pleasant, up until I feel a strange sting." 
            "As I direct my gaze downwards, the first thing I see is this beautiful, red haze floating in the water."

            "It's my blood."

            "I panic as I look at the thing that has sunk it's teeth into my foot. A snake?... No, a moray!" 
            "I try to shake it off, but that just makes the pain worse. It's not letting go!"

            "I'm really starting to lose a lot of blood here. I desperately make my way towards the shore, but everything is getting darker around me."
            "I fall face down into the water..."


label concert:
    scene concert

    "To be honest, the band is not too inspiring, but you can't expect the best of the best at a faraway place like this." 
    "At least the music is passable."

    "Right now the music is the least of my concerns, though."

    c "Drugs?"

    a "Aren't you kinda curious? People are changed by trips, you know."

    c "I'm fine just the way I am, thanks. If you're so interested, why don't you try it yourself?"

    "Amy flashes an annoying smile at me."

    a "I have to see that it's safe first, right?"

    d "Look, you gonna choose now? I don't got all day."

    "Looking at this shady dealer, I get the feeling I'm going to be beaten to death by some gang if I don't comply." 
    "And it's not like I want to get embarassed in front of Amy, either."

    "Here goes nothing."

    menu:
        "Take the shrooms and try them":

            "So I taste the shrooms." 
            "At first, I don't notice any real effect. Then there's this odd multicolored noise covering my field of vision."
            "I think I need to lie down a bit."
            "For some reason, I have ten fingers in one hand. Huh."

            "I'm on the top of mountain somewhere in the Himalayas. I can see Kathmandu from here."

            "Oh yeah, and a flying saucer. It's quite nice, hovering over me and all."

            "And now it's pulling me in. I don't see any grayheaded aliens with bulging black eyes, though."

            "At first I see no-one at all. Then my vision changes, and the whole saucer is filled with strange, pulsating beings of many colors."

            f "Attention, human! We are aliens from the fifth dimension, and we have come to enlighten you in our ways."

            "Suddenly I am not in the saucer. I am watching a thread of light going up and down, up and down like a makeshift rollercoaster."

            sin  "Attention, human! This is your lifeline."

            "Of course. I already knew that."

            sin "From your limited four-dimensional perspective, time exists and your life is full of possibilities."
            sin "But here in the fifth dimension, you can see the thread of fate as it's truly spun."

            "Everything this lovable sine wave tells me makes perfect sense. It's great! Why didn't I ever realize how great it is before?"

            cos "From an inexhaustible beginning to an incomprehensible end, your butterfly-life goes up and down."
            cos "It is only your resistance that creates suffering. Feel your purpose, and step fearlessly onwards!"

            sin "Attention, human! The experience has ended. Thank you for flying with us, and please remember that we appreciate all feedback."
            sin "Collect frequent tripper points for extra enlightenment!"   

        "Buy them, but refuse to use them":

            "I buy the shrooms, and the dealer leaves us alone. Thank god for that."

            a "Well? You gonna try them now?"

            c "No way." 
            "This is going way too far. How am I gonna get rid of these now?"

            "Maybe I can just discreetly dump them into a trash bin somewhere?"

            "I realize that Amy has disappeared into the crowd. I wonder w-"

            "My thinking freezes as I feel a burly hand descend on my shoulders."

            g "Excuse me, sir? You're coming with me."

label radio2:
    scene radio

    "Just a normal day at the radio station. I stare at the hands of the clock on the wall, tapping a pen on my desk. Half an hour to go."
    "I glance at the calendar. April 25th. I'm going to a concert with Amy this evening." 
    "I brought some clothes with me in the morning, so I don't have to cycle back home or anything."

    "The old guy's left already. I might as well get going. With that, I start turning the machines on auto-mode."

    # This ends the game.

return