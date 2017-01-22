# The script of the game goes in this file.

init python:

    #Credits
    credits = ('Story', 'Full team'), ('Script', 'Jami Valorinta'), ('Music/SFX', 'Mikael Korpela'), ('Music/SFX', 'Ricardo Falcon Perez'), ('Music/SFX', 'Zhicun Xu'), ('Sprites and CG', 'Roope Herpiö'), ('Background images', 'Snehadri Sinha'), ('Background images', 'All images are under Creative Commons'), ('Programming', 'Jami Valorinta'), ('Programming', 'Mikael Korpela'), ('Programming', 'Roope Herpiö'), ('Programming', 'Snehadri Sinha')
    credits_s = "{size=80}Credits\n\n"
    e1 = ''
    for e in credits:
        if not e1==e[0]:
            credits_s += "\n{size=40}" + e[0] + "\n"
        credits_s += "{size=60}" + e[1] + "\n"
        e1=e[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.12.2"


    def amy_normal_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.normal.wav", channel='sound')
        #elif event == "slow_done" or event == "end":
        #    renpy.music.stop(channel="sound")
    def amy_excited_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.excited.wav", channel='sound')
    def amy_happy_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.happy.wav", channel='sound')
    def amy_question_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.question.wav", channel='sound')
    def amy_angry_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.angry.wav", channel='sound')
    def amy_sad_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Amy/amy.sad.wav", channel='sound')

    def beato_normal_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Beatrice/beatrice.normal.wav", channel='sound')
    def beato_sad_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Beatrice/beatrice.sad.wav", channel='sound')
    def beato_angry_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Beatrice/beatrice.angry.wav", channel='sound')
    def beato_question_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Beatrice/beatrice.question.wav", channel='sound')
    def beato_excited_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Beatrice/beatrice.excited.wav", channel='sound')

    def male1_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Other/male1.wav", channel='sound')
    def male2_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Other/male2.wav", channel='sound')
    def priest_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Other/priest.wav", channel='sound')
    def alien_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("va/Other/alien.wav", channel='sound')


# Declare characters used by this game. The color argument colorizes the
# name of the character.

image amy normal2 = "lr/amy_normal_2.png"

image amy normal = "lr/amy_normal.png"

image amy gossip = "lr/amy_gossip.png"

image amy disappoint = "lr/amy_disappoint.png"

image amy laugh = "lr/amy_laugh.png"

image amy provocative = "lr/amy_provocative.png"


image beato normal2 = "lr/beato_normal.png"

image beato sad = "lr/beato_sad.png"

image beato back = "lr/beato_back.png"

image beato courtesy = "lr/beato_courtesy.png"

image beato confused = "lr/beato_confused.png"

image beato turn = "lr/beato_turning.png"


image guard = "lr/guard.png"

image dealer = "lr/dealer.png"

image priest = "lr/priest.png"


image sineFD:
    "sprites/sine_0.png"
    pause 0.1
    "sprites/sine_1.png"
    pause 0.1
    "sprites/sine_2.png"
    pause 0.1
    "sprites/sine_3.png"
    pause 0.1
    repeat

image cosFD:
    "sprites/cosine2_0.png"
    pause 0.1
    "sprites/cosine2_1.png"
    pause 0.1
    "sprites/cosine2_2.png"
    pause 0.1
    "sprites/cosine2_3.png"
    pause 0.1
    repeat

image sine:
    "sprites/cosine_0.png"
    pause 0.1
    "sprites/cosine_1.png"
    pause 0.1
    "sprites/cosine_2.png"
    pause 0.1
    "sprites/cosine_3.png"
    pause 0.1
    repeat

image moray = "cgs/moray.png"
image drown = "cgs/watery.png"

define c = Character("Chris")

define o = Character("Old man")

define a = Character("Amy", callback=amy_normal_beep)

define b = Character("Beatrice", callback=beato_normal_beep)

define B = Character("Beautiful woman", callback=beato_normal_beep)

define bq = Character("Beatrice ???", callback=beato_question_beep)

define p = Character("Priest", callback=priest_beep)

define d = Character("Dealer")

define f = Character("Flying sine wave")

define cos = Character("Flying cosine wave from the Fifth Dimension")

define sin = Character("Flying sine wave from the Fifth Dimension")

define g = Character("Guard")

# MY OWN CHARACTERS

define b_sad = Character("Beatrice", callback=beato_sad_beep)

define a_happy = Character("Amy", callback=amy_happy_beep)

define a_excited = Character("Amy", callback=amy_excited_beep)

define a_angry = Character("Amy", callback=amy_angry_beep)

define a_sad = Character("Amy", callback=amy_sad_beep)

define a_ask = Character("Amy", callback=amy_question_beep)

define b_excited = Character("", callback=beato_excited_beep)

define b_angry = Character("Beatrice", callback=beato_angry_beep)


init:
    # image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image fgj17 = Text("{size=80}Finnish Game Jam 2017 Otaniemi", text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image frag = Text("{size=80}Fragments", text_align=0.5)
    image thanks = Text("{size=40}Thanks to Samuli Pentti for the concert background image", text_align=0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ fragment_queue = []
    $ a_points = 0
    $ b_points = 0

    scene radio

    play music "bgm/Foley - ElecNoise16.wav"

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
    scene bar with dissolve

    play music "bgm/AmbientBGM.mp3"

    "After a hard day's work, I decide to hit the bar before going back home. Ever since the new bartender was hired a few weeks ago, I've been coming here daily."
    "You know, it's nothing dirty or anything, she just knows how to fix a drink!"

    show amy normal2

    a_ask "How may I serve, sir?"

    "Amy asks the question with a playful smile. She's not exactly the servile type, I know that already."
    "It's probably just a company line she's forced to say, but somehow she's managed to turn it into her own little in-joke."

    c "I'll take a Snow White."

    show amy provocative

    a_excited "You sure you don't want something more manly? Here, I'll make you a Jagerbomb!"

    c "Well, it is Friday, I guess. Hit me up with that."

    "Amy's pretty young, in her early twenties, I think. With her looks and positive attitude, it's no surprise she got hired."
    "Still, she seems like the type of girl who wants to do something with her life. You know, instead of toiling her life away at some random bar in a small seaside village."

    "Suddenly, someone walks in and takes one of the seats at the desk. I can tell she's not one of the usual patrons."

    hide amy provocative
    show beato normal2

    "She's wearing an elaborate dress that seems suitable neither for this climate nor for this bar."
    "But damn is she beautiful. She has a long curly hair, and the scent of flowers hangs around her."

    menu:
        "Welcome the newcomer":


            $ fragment_queue.append("MEL/B1.wav")
            $ b_points += 1
            $ bar_choice = True

            c "Hey, I haven't seen you here before! New in town?"

            "She looks at me a bit incredulously. Did my sudden advance make her uncomfortable? I sigh in relief inwardly as she breaks out a smile."

            B "No, I'm actually a regular. I recently inherited a flower shop around here. Here's my card."

            "I glance at the name in the business card."

            c "Beatrice? Wow, your name sounds so refined!"

            show beato courtesy

            b "Thank you. Come and visit later, won't you? I really want to keep the store, but there aren't that many customers. Just a few older ladies."

            "Finishing her Snow White, she stands up."

            b "It was a pleasure talking to you."

        "Better not disturb her":

            $ fragment_queue.append("MEL/A1.wav")
            $ a_points += 1
            $ bar_choice = False

            show beato sad

            "The woman orders a Snow White, not really talking to anyone. There's an aura of contemplative sadness around her, and it seems to push away any potential suitors. She finishes her drink and leaves."

            hide beato sad
            show amy normal2

            a_sad "Beato is unhappy as always, huh?"

            c "Beato?"

            "Amy smiles."

            a "That's her name. Beatrice."

            "A beautiful name for a beautiful woman, I see."

            show amy gossip

            a "She's got a flower store in town, but I hear it's doing pretty badly. She's kind of a loner."

            c "You seem to know her pretty well."

            "Amy rejects my hypothesis, looking a bit uncomfortable."

            show amy normal

            a_angry "I mean, she comes here often. But I don't really get her. I would never want to spend the rest of my life alone in some shop totally off the map!"

            "I guessed as much. She gradually grows more excited as Beatrice's influence wanes."

            show amy laugh

            a_excited "Yeah! I wanna see the world, you know, travel and get to know new people, get new experiences, that sorta stuff! Once I've got enough savings, I'll try to get a degree in journalism, or..."

            "I pretend to pay attention, but get lost in thoughts, staring at her lips."

label cliff:
    scene cliff with dissolve

    play music "bgm/Foley - Wind16.wav"

    "A pleasant breeze blows towards me as I cycle up and down the hills. The sun is about to set, but I still feel warm, perhaps due to the workout."
    "Cycling home through the countryside has been one of the few remaining passions in my life ever since I moved to this island."
    "I'm approaching a familiar cliff with an amazing view of the ocean. Sometimes I come here in the evenings to watch the blazing sun sink under those peaceful waves."
    "I stop my bike at the cliff. From this angle, the cliff is hidden from view by the vegetation."
    "I jump over the guard rails and walk down a well-trodden path of trampled grass, arriving at the cliff."

    "The view is beautiful as usual. In front of me, the sky is red with the descending sun."
    "However, this time something is different. There is an intruder in my sanctuary."

    show beato back

    "A woman in a flowing white dress is standing right at the edge of the cliff with her back turned towards me, gazing wistfully at the ever-rolling waves."
    "Suddenly I recognize her. It's Beatrice."
    "What is she doing here? And how did she find her way here?"

    menu:
        "Wave and try to catch her attention":

            $ fragment_queue.append("MEL/B2.wav")
            $ b_points += 1
            $ cliff_choice = True

            c "Hey, Beatrice! Over here!"

            "I try to catch her attention, but she appears to be too deep in her thoughts to hear me. I slowly approach her from behind."
            "I'm right behind her now. I can smell the floral perfume emanating from her curly hair."

            c "Beautiful view, eh?"

            "She is startled by my sudden whisper, and before I can react in any way, her foot slips -- "

            hide beato back with moveoutbottom

            play music "bgm/Conflict_V1.mp3"

            "-- and she falls, falls, falls! I try to grasp her, but my movements are too slow."
            b_excited "In a split second, screaming, she disappears under the black waves."
            "And in the silent air, long after she is gone, I can still hear her scream."

        "Observe her passively":

            $ fragment_queue.append("MEL/A2.wav")
            $ a_points += 1
            $ cliff_choice = False

            "Maybe it's better not to disturb her. I stay in the shadows of the trees, trying to keep quiet."

            show beato sad

            "She keeps staring at the waves, but her eyes are glazed over and empty. Just what is she thinking of...?"

            hide beato sad

            "Then, one moment, and she disappears into thin air--"
            play music "bgm/Conflict_V1.mp3"
            "That's my first impression, until I realize what has happened."
            "I can barely catch a glimpse of her wavy hair vanishing under the cliff. One step, and she is gone."
            "I stay there, sitting under the trees, and all I can see is that one curl of hair."

label grave:
    scene grave with dissolve

    play music "bgm/Foley - Rain16.wav"

    "I was invited to her funeral, maybe because I was the only one of the locals who had gotten close to her. "
    "Still, I feel like an outsider here, among the grieving faces of her family, all of them strangers."

    "It's raining."
    "To me, the drops seem like soft tears falling from a darkened heaven."
    "It certainly doesn't make me feel any better."
    "After all, I am the reason she died."
    "It was all. My. Fault."

    "As the priest is giving the funeral speech, I can barely hear his voice as background noise to the welter of my thoughts."
    "My gaze flits unconsciously from attendee to attendee. And slowly, slowly I realize that my eyes have fixated on someone."
    "I'm looking at someone from behind."
    show beato back
    "It's a woman wearing a flowing white dress."
    "Perhaps that is what caught my attention, everyone else is wearing something suitably depressed."
    "But no, I'm looking at her long, curly hair."
    "There's a faint voice within me, trying to tell me something, but at first I'm too lost in depression to hear."

    menu:
        "You know her":
            "Wait."
            play music "bgm/Action_V1.mp3"
            "I know her. It can't be!"
            "Explanations race through my mind: a twin sister, mother, it was all a nightmare, this is all a nightmare, clones, aliens..."
            "Beatrice!"

    menu:
        "Run to interrogate her!":

            $ fragment_queue.append("MEL/A3.wav")
            $ a_points += 1
            $ graveyard_choice = True

            "I run to her, disturbing the procession. Everyone is looking at me now, faces mixed with shock and apprehension, but I couldn't care less."

            "And as I see her face, as I look into those cerulean eyes, wide with surprise or with terror, my suspicions are confirmed. It *is* her!"

            c "Beatrice! How can you be alive? I saw you, I saw you fall..."

            show beato confused

            bq "... Do I know you, sir?"

            c "What do you mean? Of course you do..."

            "The inital shock of the crowd around me is slowly turning to annoyance, to anger, and I can feel the pressure from their silent stares."

            "The priest is slowly trying to continue his speech, unsure of what to do."

            "If Beatrice is here, at her own funeral, then who is in the coffin?"

            hide beato confused

            play music "bgm/Foley - Rain16.wav"

            "I walk over to the coffin. Nobody stops me."

            "And I look at the corpse, lying quietly on the red cushions."

            "No..."

            "Beatrice slowly walks behind me, and whispers in my ear."

            b_sad "This is not my funeral. It's yours."

        "Just keep watching...":

            $ fragment_queue.append("MEL/B3.wav")
            $ b_points += 1
            $ graveyard_choice = False

            play music "bgm/Foley - Rain16.wav"

            "It's better not to cause a ruckus. I keep my gaze fixed on the strange apparition before me."
            "I'm beginning to doubt my sanity. It cannot be her. This is her funeral!"

            show beato turn
            "But then, for just a moment, she turns her head so I can see those cerulean eyes."
            "And then I am certain. It is her."

            "All my sorrow has vanished, replaced by total confusion."
            "It is as if the world around me was collapsing around me, crushing me under my crumbling sense of reality. What is going on?"

            "I sit and stare, unable to do anything but."
            hide beato turn
            show priest
            "The priest's words envelope me subconsciously, even though I can't pay attention to them anymore."
            "But suddenly, something he says piques my interest. It takes me a while to realize what he said."
            "My name."

            p "Though he had only recently moved here, he was liked by all..."

            "The realization slowly dawns on me."
            "This is not Beatrice's funeral."
            "It is mine."

label beach:
    scene black with dissolve
    pause 0.5
    scene beach with dissolve

    play music "bgm/Foley - Beach16.wav"

    "Woohoo! I shift my weight forward, causing the board to swerve left. "
    "The sun is really hot today, but I've been falling into the water all day, so it's bearable. Splash! There I go again."
    "Speaking of hot, I can see Amy surfing some really big waves in the distance."
    "Unlike me, she hasn't fallen once the entire day. Her style is breathtaking."

    "If only she didn't laugh every time I fall."
    "Not that I mind making her laugh. Better than being boring."
    "Amy paddles closer to me on her board, laughing at my misery as usual. Come on girl, don't be so mean!"
    "I can't stay angry at that figure, though! Especially not with that bikini..."

    show amy laugh

    a_happy "Hahaha, you fell again!? Hope it didn't hurt!"

    c "Eh, I can handle it."

    "Why am I pretending to be so macho, anyway?"

    show amy provocative

    a_ask "Wanna try something harder? I can teach you my super-secret board jump move! It's really cool!"

    c "Erm, I don't know if I'm ready, oh master..."

    "Still, a strange sense of bravery is starting to well up within me. I do kinda want to try something harder already."

    play music "bgm/Action_V1.mp3"

    menu:
        "Do the super-secret board jump move":

            $ fragment_queue.append("MEL/A4.wav")
            $ a_points += 1
            $ beach_choice = True

            hide amy
            "The idea makes my heart pump, but all my fears are being drowned by crazy courage. I'll show her!"

            "She guides me deeper into the ocean, into an area with colossal, periodic waves."

            show amy laugh

            a_excited "Okay, just wait for a reaaallly big one! Here it comes!"

            hide amy laugh

            "As the wave comes, I go through the usual motions: first on my knees, then..."
            "Stand! It feels difficult, but somehow, I manage to surf the wave."

            show amy laugh

            a_excited "Just remember my instructions! Now!"

            hide amy laugh

            "With a shift of weight, I flip the board under me and jump into the air! I'm doing it!"
            "I'm, uh, falling into the water as usual."
            "Damn. So much for that."

            "Except the waves are really huge out here. I'm starting to wonder if this was the brightest idea."

            scene drown

            "Gulp. Gasp! I can't... air..."

            "The sounds of the gushing waves and Amy's shouting seem to be coming from somewhere far away as I keep sinking beneath."

            pause 0.5


        "Maybe I'll just practice a bit closer to the shore":

            $ fragment_queue.append("MEL/B4.wav")
            $ b_points += 1
            $ beach_choice = False

            play music "bgm/Foley - Beach16.wav"

            "Common sense overcomes me. No way I'm ready for that."

            show amy disappoint

            a_sad "Oh, you're no fun!"

            "Amy's disappointment makes me blush and reconsider, but to be perfectly honest, I'm kinda terrified of those waves."

            hide amy disappoint

            "Amy paddles back into the deeps, ready to surf again."

            "Well, I guess there's nothing to do but practice. I relax for a while in the waters nearer to the shore."
            "The sand and rocks caress the soles of my feet. It feels quite pleasant, up until I feel a strange sting."
            "As I direct my gaze downwards, the first thing I see is this beautiful, red haze floating in the water."

            play music "bgm/Conflict_V1.mp3"

            "It's my blood."

            scene moray

            "I panic as I look at the thing that has sunk it's teeth into my foot. A snake?... No, a moray!"
            "I try to shake it off, but that just makes the pain worse. It's not letting go!"

            "I'm really starting to lose a lot of blood here. I desperately make my way towards the shore, but everything is getting darker around me."
            "I fall face down into the water..."

            pause 0.5


label concert:
    scene concert with dissolve

    play music "bgm/Action_V1.mp3"

    "To be honest, the band is not too inspiring, but you can't expect the best of the best at a faraway place like this."
    "At least the music is passable."

    "Right now the music is the least of my concerns, though."

    c "Drugs?"

    show amy normal

    a "Aren't you kinda curious? People are changed by trips, you know."

    c "I'm fine just the way I am, thanks. If you're so interested, why don't you try it yourself?"

    "Amy flashes an annoying smile at me."

    show amy disappoint

    a "I have to see that it's safe first, right?"

    show amy normal at left

    show dealer at right
    with moveinright

    d "Look, you gonna choose now? I don't got all day."

    "Looking at this shady dealer, I get the feeling I'm going to be beaten to death by some gang if I don't comply."
    "And it's not like I want to get embarassed in front of Amy, either."

    "Here goes nothing."

    menu:
        "Take the shrooms and try them":

            $ fragment_queue.append("MEL/A5.wav")
            $ a_points += 1
            $ concert_choice = True

            jump ufo

        "Buy them, but refuse to use them":

            $ fragment_queue.append("MEL/B5.wav")
            $ b_points += 1
            $ concert_choice = False

            jump trouble

label ufo:

    hide amy normal
    hide dealer

    "At first, I don't notice any real effect. Then there's this odd multicolored noise covering my field of vision."

    scene trip with dissolve
    pause 1.0

    "I think I need to lie down a bit."
    "For some reason, I have ten fingers in one hand. Huh."

    "I'm on the top of mountain somewhere in the Himalayas. I can see Kathmandu from here."
    scene ufo with dissolve

    "Oh yeah, and a flying saucer. It's quite nice, hovering over me and all."

    "And now it's pulling me in. I don't see any grayheaded aliens with bulging black eyes, though."

    "At first I see no-one at all. Then my vision changes, and the whole saucer is filled with strange, pulsating beings of many colors."

    show sine with dissolve:
        zoom 0.5
        yanchor 0
        xanchor 0.5
        yalign 0
        xalign 0.5

    f "Attention, human! We are aliens from the Fifth Dimension, and we have come to enlighten you in our ways."

    "Suddenly I am not in the saucer. I am watching a thread of light going up and down, up and down like a makeshift rollercoaster."

    show sineFD with dissolve:
        zoom 0.5
        yanchor 0
        xanchor 0
        yalign 0
        xalign 0

    show cosFD with dissolve:
        zoom 0.5
        yanchor 0
        xanchor 1.0
        yalign 0
        xalign 1.2

    sin  "Attention, human! This is your lifeline."

    "Of course. I already knew that."

    sin "From your limited four-dimensional perspective, time exists and your life is full of possibilities."
    sin "But here in the fifth dimension, you can see the thread of fate as it's truly spun."

    "Everything this lovable sine wave tells me makes perfect sense. It's great! Why didn't I ever realize how great it is before?"

    cos "From an inexhaustible beginning to an incomprehensible end, your butterfly-life goes up and down."
    cos "It is only your resistance that creates suffering. Feel your purpose, and step fearlessly onwards!"

    sin "Attention, human! The experience has ended. Thank you for flying with us, and please remember that we appreciate all feedback."
    sin "Collect frequent tripper points for extra enlightenment!"

    hide sine
    hide sineFD
    hide cosFD
    jump radio2

label trouble:

    "I buy the shrooms, and the dealer leaves us alone. Thank god for that."

    hide dealer with moveoutright

    show amy normal:
        yanchor 0
        xanchor 0.5
        yalign 0
        xalign 0.5

    a "Well? You gonna try them now?"

    c "No way."
    "This is going way too far. How am I gonna get rid of these now?"

    "Maybe I can just discreetly dump them into a trash bin somewhere?"

    hide amy normal with dissolve

    "I realize that Amy has disappeared into the crowd. I wonder w-"

    "My thinking freezes as I feel a burly hand descend on my shoulders."

    show guard

    g "Excuse me, sir? You're coming with me."

    hide guard

label radio2:
    scene radio with dissolve

    play music "bgm/Foley - ElecNoise16.wav"

    "Just a normal day at the radio station. I stare at the hands of the clock on the wall, tapping a pen on my desk. Half an hour to go."
    "I glance at the calendar. April 25th. I'm going to a concert with Amy this evening."
    "I brought some clothes with me in the morning, so I don't have to cycle back home or anything."

    "The old guy's left already. I might as well get going. With that, I start turning the machines on auto-mode."


    # plays the fragments
    #play music fragment_queue

    # something changes based on the points?
    #if a_points >= 5:
        # something if  5 a_points gotten?
    #elif b_points >= 5:
        # something if 5 b_points gotten?
    #else:
        # something if neither?

    #if bar_choice:
        # something if talked to beato
    #else:
        # something if did not talk

        #choice variable names:
        # bar_choice cliff_choice graveyard_choice beach_choice concert_choice
    # This ends the game.


label ending:

    play music "bgm/AmbientBGM.mp3"

    scene bar with dissolve

    "I go to pick up Amy at the bar. Her shift's just about to end."

    show amy normal2

    a_happy "How may I serve, sir?"

    "Amy asks the question with a playful smile."
    "It's probably just a company line that she's forced to say, but somehow she's managed to turn it into an in-joke."

    c "Are you seriously going to the concert in those clothes?"

    a_ask "Huh? Concert?"

    "The fact that she's forgotten is kind of frustrating."

    c "The one on the 25th. That's today, right?"

    "Amy's smile shifts between amusement and confusion."

    a "Uh, that was yesterday."
    if concert_choice:
        a_ask "Man, the shrooms really got to you, didn't they?"
    else:
        a_happy "Did you try the shrooms after all? Sorry I ditched you with the security guard there!"

    "Now that you mention it, I do remember that. I feel a bit of vertigo."

    if concert_choice:
        "Really shouldn't have tried those shrooms."
    else:
        "But I'm sure I didn't use anything. What's going on?"

    hide amy
    show beato normal2

    "Suddenly, someone walks in and takes one of the seats at the desk."
    "I can tell she's not one of the usual patrons. She's wearing an elaborate dress that seems suitable neither for this climate nor for this bar."

    "In a flash, I lose all sense of my surroundings."

    play music "bgm/Conflict_V1.mp3"

    scene cliff with dissolve

    if cliff_choice:
        b_excited "She's screaming, falling under the waves."
    else:
        "All I can see is one curl of hair, disappearing beneath the cliff."

    "She's dead. I was at her funeral."

    scene grave with dissolve

    if graveyard_choice:
        b_sad "This is not my funeral. It is yours."
    else:
        p "Though he had only recently moved here, he was liked by all..."

    scene bar with dissolve

    "I'm... dead? But I'm standing right here!"

    if not beach_choice:
        "My heart is beating, blood is flowing in my veins!"
        scene moray
        "I'm really starting to lose a lot of blood here..."
    else:
        "I'm still breathing!"
        scene drown
        "Gasp! I can't... air..."

    scene black with dissolve

    stop music

    "I'm floating in a sea of blackness. There's a small bubble of pulsating light in front of me."

    show beato sad

    "It's Beatrice. She is sitting at a harpsichord, playing a tune with her nimble fingers."

    #Play Melody.

    play music fragment_queue noloop

    show beato normal2

    "Beatrice rises and addresses me, her cerulean eyes looking deeply into mine."

    b_angry "How many times have you died already?"

    "Her voice remains courteous, but there's a hint of... anger?"

    bq "Do you know who I am?"

    "She sounds almost despairing."

    bq "What my surname is?"

    if bar_choice:
        "No..."

        "I feel something in my pocket. A card."

        "Her business card."

        "I look at her name."

        "How did I never notice this before?"

        "Her surname is the same as mine!"

    else:
        c "Sorry."

    if a_points >= 5:
        #AMY ENDING:

        play music fragment_queue loop

        "Beatrice looks at me sorrowfully."

        b "The melody is complete. You have forgotten me, and it is for the better."

        b "Leave this island with Amy before May, and fate shall spare you both."

        "She starts drifting away, the blackness vanishing around me."

        show beato sad

        b_sad "Goodbye, my..."

        scene bar with dissolve

        "I am at the bar."

        a_excited "Chris? Are you all right!?"

    elif b_points >= 5:
        #BEATRICE ENDING:

        play music fragment_queue loop

        "As I say her full name, Beatrice's face lightens."

        b "You remember."

        b "The melody is complete. Your memories have returned from the haze of time."

        "The blackness vanishes."

        "I am at Beatrice's flower shop. She is smiling."

        "Hers is the most beautiful smile in the world."

        show beato sad

        "She hugs me, and cries."

        b_sad "You're alive..."

    else:
        #NORMAL ENDING:

        "Beatrice's voice drips with resentment."

        b_angry "The melody is incomplete. And yet again you and I must return to the has-already-been."

        "Did I fail her somehow?"

        "The blackness vanishes around me."

        scene radio with dissolve

        play music "bgm/Foley - ElecNoise16.wav"

        "I'm sitting at my desk at the radio station."

        "I moved here recently. It's my first day at work."

        "I'm really liking this subtropical climate."

        "I can't believe it's January and still so warm!"

    #Jump to the credits
    call credits
    return

label credits:
    $ credits_speed = 20 #scrolling speed in seconds
    scene black with dissolve #replace this with a fancy background
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 4.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    show fgj17:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide fgj17
    with Pause(1)
    show frag:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide frag
    return


return
