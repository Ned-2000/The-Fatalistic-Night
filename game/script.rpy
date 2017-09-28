# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image black = "BLACK.png"
image village = "village_at_night_by_unidcolor-d370xmq.jpg"
image zombies = "zombie_hoard_halloween_prop__76121.1433907499.1280.1280.png"
image forest = "forest1bg.png"
image house = "abandoned_house.jpg"

# Declare characters used by this game.
define e = Character('Everyone', color="#d0d0d0")
define m = Character('Mordecai', color="#1056ce")
define g = Character('Captain Greenwood', color="#219859")

# The game starts here.
label start:
    
    $ player_health = 4
    $ zombies = 3
    
    show black
    
    play music "Eerie Forest Night Ambience Effect.wav"
    
    m "I take in a deep breath while my eyes are closed."
    
    m "I take in another one."
    
    m "Another final breath, listening to ambience of the little town and surrounding nature I'll be slaughtered in."
    
    m "It's not a very comforting breath, and I'm scared to open my eyes, but I do both of them anyways."
    
    hide black
    show village
    with dissolve
    
    m "The decrepit village smells of rotten wood abandoned dozens of years ago, its tiny houses are covered in dust and rust."
    
    m "I look around the forest that envelope the tiny village, and see black silhouettes of the rustling trees and creatures weaving in and out of them, hearing their little chirps and calls."
    
    m "The blue dusk of the sky gives warning that it will soon be dark, and threatens to darken everything in shades of black, letting anyone or anything be able to slip in the shadows."
    
    m "All of the sights, sounds, and smell make me want to take off and never look back, but to do so would betray the Citadel, my teammates, and myself."
    
    m "The Citadel did take me and many others in at a young age, and somehow managed to make something out of me. To prove it, we would have to pass the first test in this squalid village against the other teams."
    
    m "I reminisce the several years of combat training and education within the stone walls of the Citadel. It made me pretty skilled at the rapier, and I'll have to show it by piercing it through the brains of an undead."
    
    
    
    m "I take a look at my teammates, and try to read on how they're dealing with this."
    
    m "A glance at the face of our fighter seems that he would show no mercy towards our undead opponents. His heavy plate armour and the giant longsword he's holding in front of him prove his expression further."
    
    m "The eyes of our half-orc wizard dart side to side as he intensely reads the gigantic leather-bound spellbook in one hand, mimicing hand gestures in other one. No doubt he'll cast a fireball or have a trick up his robe to
       turn the tides of battle to us."
    
    m "Our cleric is kneeling down, trying to heal a small, dead animal on the ground, probably to practice his medical skills once we're all bitten or torn to shreds by the horde. I'll be glad to have him if I somehow turn
       undead."
    
    m "I listen to the telltale hums of the monk which will aid us in battle. She's on the dirt ground with her legs crossed, arms in a convoluted twist, and her eyes shut as she focuses on some chant that I'll never be able to
       learn, or even understand."
    
    m "But I focus on myself the most. Black, leather armour covers my entire body, at the left side of my hip is my rapier in its sheath, ready to come out at a moments notice. My longbow and quiver sit comfortably on
       my back, giving me a sense of ease since I do not have to be face to face with one of those things."
    
    m "I shiver a small amount as the Autumn cold clenches my skin, and I can see small puffs of my breath condensate as I exhale."
    
    stop music
    play sound "Zombie sound effects - moderate moaning.ogg"
    
    e "!"
    
    m "A chilling groan of an undead catches all of us in surprise, and we stare at the source of where it came from."
    
    m "Off in the distance, we see a lone, shambling figure with sloughing flesh meandering towards us, its glowing eyes show its intense desire to consume all of our flesh and blood."
    
    play sound "mega_mob_incoming.wav"
    play music "Chase Pulse.mp3"
    show zombies at Position(xpos = 0.5, xanchor=0.5, ypos=0.8, yanchor=0.5):
        zoom 0.8
    with dissolve
    
    m "It's not just one figure I realise, dozens of the undead start to zero in on our position sprinting at full speed, moans and groans turn into screams of pure terror, their faces are of pure hatred for the living."
    
    m "Everyone readies up, the fighter holding his sword high over his head, the wizard conjuring a fireball in his hand, our cleric holding holy water in hand, and our monk chanting louder than ever."
    
    menu:
        m "I know what to do."
        
        "Ready my bow and fire!":
            m "I take my longbow off of my back, along with an arrow from my quiver, I line it along the arrow rest and the string, and pull it back, aimed at one of the monstrosities."
            
            $ attack = renpy.random.randint(1, 20)
            
            "DC 13 to hit undead, you rolled [attack]"
            
            if attack >= 13:
                m "The arrow flies straight into the forehead of the unfortunate undead, he groans in an immense amount pain, buckles down to his knees and falls face first, no longer struggling. But now the rest of the undead
                   are even more determined to get me and start to charge, they are now to close to aim another arrow, and I am forced to draw my rapier."
                
                $ zombies -= 1
                
                jump rapier_field_fight
                
            if attack < 13:
               m "The arrow flies well above the forehead of the lucky undead, he now seems angrier, and charges faster, he is too close to pull of another shot, so I prepare to unsheath my rapier, ready to fight face to face."
                
               jump rapier_field_fight
                
        "Unsheath my rapier and charge in!":
            
            jump rapier_field_fight
            
        "Retreat into the nearby house.":
            
            jump house
            
        "Run, and never look back.":
            
            jump retreat
    
    label rapier_field_fight:
        
        m "The moonlight reflects of the thin metal of my rapier as I take it out of my sheath. I give it a firm grip on the handle, and I change into a combat stance as an undead approaches me."
        
        jump rapier_fight_outside
    
    label rapier_fight_outside:
        
        m "The zombie twitches every few seconds, his jaws open and close with blood drooling out, eyes dilating and pulsating, his banshee screams make me want to aim for his throat."
        
        m "My current health is [player_health]."
        
        menu:
            m "I make my decision."
            
            "Thrust the rapier into him.":
                m "I aim for the torso, and thrust my rapier."
                
                $ attack = renpy.random.randint(1, 20)
                
                "DC 11 to pierce zombie, you rolled [attack]"
                
                if attack >= 11:
                    
                    m "My well placed thrust cleanly goes through the throat, instantly stopping his screams. Blood begins to leak from the puncture, and as I pull the rapier out the blood flows out faster. He slowly grabs his
                       throat and falls onto his back, dead."
                    
                    $ zombies -= 1
                    
                    if zombies <= 0:
                        
                        jump win
                        
                if attack < 11:
                    
                    m "The rapier grazes the stomach of the zombie, doing nothing to stop his determination. Instead, he becomes more enraged, his eyes turn to red, his breathing is louder, and a face of pure hatred shows."
                    
            "Yell for the help of the cleric":
                
                m "I scream for the attention of the cleric to tend to my wounds. Even though he is distracted fighting off another zombie, with the flick of his wrist and unidentifiable chant, my wounds stop bleeding and
                   heal at a rapid pace, and I silently thank him."
                
                $ player_health = 4
                
                jump zombie_attack
                
            "Run.":
                
                jump retreat
    
    label zombie_attack:
        
        m "One of the undead lets out a howl of malevolence, and swings his arm across my torse, hand stretched out and sharp claws on his fingers."
        
        $ attack = renpy.random.randint(1, 20)
        
        "DC 15 for undead to hit Mordercai, undead rolled [attack]."
        
        if attack >= 15:
            
            $ player_health -= renpy.random.randint(1, 3)
            
            if player_health > 0:
                
                m "The undead slashes his claws along my chest, leaving four streaks of exposed flesh, and blood starts to pour out of them. I try not to focus on it, readying my rapier to exact my revenge."
            
                jump rapier_fight_outside
                
            if player_health <= 0:
                
                jump zombie_death
            
        if attack < 15:
            
            m "His claws barely touch my armour, to close of a call for comfort. The adrenaline really starts to flow in my body, I seethe anger, aiming my rapier to get back at him."
            
            jump rapier_fight_outside
            
    label house:
        
        m "I definitely can't fight the undead here out in the open, I'll be exposed on all sides and be surrounded."
        
        m "I make a mad dash towards the nearest building, the ruins of a tiny wooden house, ignoring the confused looks on my teammates."
        
        hide village
        hide zombies
        show house
        with dissolve
        
        m "I bash into the ancient wooden door, it easily gives way, into the remains of the once lively house, the smell of rotten wood invades my sense of smell, but there is no time to take in my surroundings."
        
        menu:
            
            m "I decide what to do in this wretched house."
            
            "Ambush the undead when they come in.":
                
                m "I hide beside the doorway, listening for any telltale signs of a zombie, slowly taking out my rapier."
                
                play sound "Zombie sound effects - moderate moaning.ogg"
                
                m "I turn to the doorway, and spot a zombie right there, I drive my rapier into his eye socket before he could notice me. I hear the sickening crack of his skull, as the end of my rapier goes out the other end
                   of his skull, he collapses and stays down."
                
                show zombies at Position(xpos = 0.5, xanchor=0.5, ypos=0.8, yanchor=0.5):
                    zoom 0.8
                with dissolve
                
                m "My rapier was thoroughly stuck and it took a while to pull it out. When I managed to pull it out, a few others were already shambling towards the doorway, and I had no choice but to do the same to the others."
                
                $ zombies -= 1 
                
                jump rapier_fight_outside
                
            "Hide.":
                
                m "I quickly spot a small dining table and squeeze myself down into there. its very cramped, but it'll do."
                
                play sound "Zombie sound effects - moderate moaning.ogg"
                
                m "I tense up, hearing the moans of an undead close by, I peek and see one has passed through the doorway. I continue to stay in my hiding spot to avoid confrontaion."
                
                $ attack = renpy.random.randint(1, 20)
                
                "DC 12 for zombie to spot Mordecai, zombie rolled [attack]."
                
                if attack >= 12:
                    
                    m "The zombie suddenly swings his claw under the table, scratching the side of my right arm, causing it to bleed."
                    
                    $ player_health = 3
                    
                    m "The pain and panic make me stand up, striking my head against the table and flipping it onto its side, I quickly pull out my rapier to fight off the undead, and curse myself for hiding in such a stupid spot."
                    
                    show zombies at Position(xpos = 0.5, xanchor=0.5, ypos=0.8, yanchor=0.5):
                        zoom 0.8
                    with dissolve
                    
                    jump rapier_fight_outside
                    
                if attack < 12:
                    
                    m "The zombie sniffs around for a few moments, and slowly shuffles away outside. I thank the gods"
                    
                    m "I don't know how long I've been hiding under the table, its been quite a while, but I'll stay under, just in case."
                    
                    stop music fadeout 1.0
                    stop sound fadeout 1.0
                    
                    m "I no longer hear the horde of undead, in fact, I no longer hear anything, not even the chit chat of my comrades, but I'll stay under, just in case."
                    
                    m "As I was about to fall asleep, I hear a booming voice."
                    
                    hide house
                    show black
                    with dissolve
                    
                    g "YOU COWARD, YOU HID WHILE YOUR COMRADES WERE BEING SLAUGHTERED."
                    
                    return
                 
                
            
            
    
    label zombie_death:
        
        hide village
        hide zombies
        show black
        with dissolve
        
        m "The wounds overpower my will to continue fighting, and I try to clutch them and close my eyes to ease the pain, but to no avail."
        
        m "They start to surround me, pushing me down on to the ground as I change into the fetal position, and start to greedily dig in."
        
        m "I feel parts of me being forcibly removed, like an amatuer surgeon was trying to amputate every part of me, my blood flows freely from all of my wounds, and all I can think is pain."
        
        m "The pain is unbearable, I must scream, but I have no throat after it was torn out."
        
        m "Before I pass out however, I hear a booming voice."
        
        g "DISAPPOINTMENT, I EXPECTED BETTER."
        
        return
            
    label retreat:
        
        m "Why am I even doing this? Such a ridiculous situation, being forced to fight the undead with a bunch of other mediocre teammates."
        
        m "I turn my heels toward the horde, and start sprinting away from it all."
        
        m "The screams of my comrades as they plead for me to come back almost make me want to, but I keep on running, further and further from the village, towards the forest."
        
        hide village
        show forest
        with dissolve
        stop music fadeout 1.0
        play music "Eerie Forest Night Ambience Effect.wav"
        
        m "My breathing gets more and more ragged and I stop, leaning on a tree, was it the right thing to do? Abandoning everything? I think frantically trying to justify running away, but then I hear a booming voice."
        
        hide forest
        show black
        stop music
        
        g "YOU ARE DISQUALIFIED, COWARD."
        
        m "I am instantly knocked out, for being such a coward."
        
        return
        
    label win:
        
        hide zombies
        with dissolve
        
        stop music
        play music "The Last of Us Soundtrack 29 - The Path (A New Beginning).mp3"
        
        m "After the zombie fell down from my finishing blow, I realise there are no more moans or groans coming from the throats of the undead."
        
        m "In fact, I don't see anymore living zombies at all, only the corpses of them. Some have been cleaved in half, others are charred or burning, turned to dust from holy water, or simply been punched to death."
        
        m "We somehow actually managed to do it, we did the test! I start to cheer, and soon the others start to join me too."
        
        m "I highly doubted we would be able to do such a thing, fight an entire horde of zombies, save for surviving."
        
        m "As we hug and praise each other, we all hear a booming, yet gentle voice."
        
        g "I am pleased with the results, congratulations!"
        
        hide village
        hide house
        show black with dissolve
        
        "I, Wathaned Ean, thank you very much for taking your time to play this game, and I hope you had a good time!"
        
        return
        
    
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
