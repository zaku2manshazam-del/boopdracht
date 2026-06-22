define g = Character('Gabriel', color="#3c3e5c")
define h = Character('Heathcliff', color="#3c5c3d")
define b = Character('Beelzebub', color="#886412")

image heathcliff neutralspeaking = Transform("heathcliff neutralspeaking.png", xysize=(500, 800))
image heathcliff discomfort = Transform("heathcliff discomfort.png", xysize=(400, 700))
image heathcliff discomfortspeaking = Transform("heathcliff discomfortspeaking.png", xysize=(500, 800))
image heathcliff angry = Transform("heathcliff angry.png", xysize=(400, 700))
image heathcliff angryspeaking = Transform("heathcliff angryspeaking.png", xysize=(500, 800))
image heathcliff concerned = Transform("heathcliff concerned.png", xysize=(400, 700))

image beelzebub neutral = Transform("beelzebub neutral.png", xysize=(800, 900))
image beelzebub neutralspeaking = Transform("beelzebub neutralspeaking.png", xysize=(900, 1000))
image beelzebub smiling = Transform("beelzebub smiling.png", xysize=(800, 900))
image beelzebub angry = Transform("beelzebub angry.png", xysize=(800, 900))
image beelzebub angry2 = Transform("beelzebub angry.png", xysize=(1100, 1200))

image gabriel test1= Transform("gabriel angry1.png")
image gabriel test2= Transform("gabriel angry2.png")

transform centerright:
    xalign 0.9

label start:
    with fade
    scene bg throneroom full

    "This visual novel is a work in progress. Things may be changed."

    "Heathcliff entered a large realm with a reddish atmosphere, it reeked like rotten food and there were all kinds of insects roaming all over. Not dissimilar to a beehive, he noticed the walls had hexagonal holes."
    "And at the center, a tall woman with a large rimmed hat and strange hair that looked almost like wings."

    h "She must be the one behind this mess.. She *has* to know where Gabriel is."

    show heathcliff discomfort at left
    show beelzebub neutral at right
    show heathcliff neutralspeaking at left

    h "Hey, lady. My brother is lost in this hellhole, you happen to see him somewhere?"

    show heathcliff discomfort at left

    show beelzebub neutralspeaking at right

    b "You sure have a lot of nerve to show your face after what you let you brother go through."

    show beelzebub neutral at right

    show heathcliff angryspeaking at left

    h "What's that supposed to mean, huh??"

    show heathcliff angry at left

    show beelzebub neutralspeaking at right

    b "Tiny Gabriel. So scarred. My five disciples had carried his fragile self all the way to my care..."

    hide heathcliff angry at left
    hide beelzebub neutralspeaking at right

    "Heathcliff didn't like the woman's tone.. She seemed quite strange."

    show beelzebub neutral at right
    show heathcliff angryspeaking at left

    h "Excuse me?! Where the hell is he?!"

    show heathcliff concerned at left
    show beelzebub neutral at centerright
    show gabriel test1 at right

    "The woman stepped aside, revealing Gabriel. He refused to look Heathcliff in the eyes."

    show gabriel test2 at right

    g "Heathcliff, please stop."

    show gabriel test1 at right
    show heathcliff angryspeaking at left

    h "Gabriel? What the hell's wrong with you?! You think this is good for you, huh? What's gotten into you?!"

    hide gabriel test1
    hide beelzebub neutral
    hide heathcliff angryspeaking

    "Gabriel couldn't look Heathcliff in the eyes, like the coward he was."

    show gabriel test1 at right
    show beelzebub neutral at centerright
    show heathcliff angryspeaking at left

    h  "Gabriel, you think this is going to fix your mental shit, huh? Those people talked you into some paranormal bullshit, and now you think you found the answer?" 

    h  "And you---You're her, right? Those freaks that pushed me in here. You're their God, arent you?!" 

    show beelzebub neutral at centerright
    show heathcliff angry at left

    "Heathcliff shouted, his anger overboiling, but the woman didn't seem phased at all.."

    show beelzebub neutralspeaking at centerright

    b "One has little control over measly activities some mortals had convinced my new disciple of. 
    Even so, they did him a favor. The world is a terrible and uncomfortable nest of parasites drilling on the turf."
    b "No matter what you think of it, you're either a measly sheep following a crowd, slurping and sucking Earths energy, 
    or you stay in the shadow of your superior, leech off of their confidence so you can rise up yourself. "  

    show beelzebub neutral at centerright
    show heathcliff angryspeaking at left

    h "That's pathetic. Gabriel, you don't actually believe in this bullshit, do you?"

    show heathcliff angry at left

    "But Gabriel didn't bat an eye. He just looked like a toddler who just got caught lying. Heathcliff couldn't let himself just give up."

    show gabriel test2 at right

    g "Heathcliff, stop trying to care."

    show gabriel test1 at right
    show heathcliff angryspeaking at left

    h ".. What?" 

    show gabriel test2 at right
    show heathcliff discomfort at left

    g "Stop trying to convince yourself you care about me. The only thing you want is credit for whatever job you do. You drag me around like an obstacle."  

    show gabriel test1 at right
    show heathcliff discomfortspeaking at left

    h "Oh don't you dare. I've done nothing but cover for your lazy ass every time. And who seemed to be getting more praise?! *You*." 

    "Not that Heathcliff cared about that. Gabriel was pulling out every excuse in the book to stay with this freak."

    h "Gabriel, you know damn well that mom and dad aren't in our lives anymore. Why are you still lingering on the past?"

    "Heathcliff got closer, wanting to grab Gabriel's hand, but Gabriel just stepped away."



    menu:
        "How will Heathcliff convince Gabriel? Use force or use words?"

        "Force.":
            "Forceful."
            jump forceful

        "Words.":
            "Peaceful."
            jump peaceful


label forceful:
    with dissolve
    scene bg throneroom full

    "Heathcliff stepped forward to Gabriel once more, grabbing his arm and pulling him closer and swinging him behind his back."

    show gabriel test1 at right
    show heathcliff discomfortspeaking at left
    show beelzebub neutral at centerright

    h "Gabriel. I'll make sure you get the help you need." 

    hide gabriel test1
    hide heathcliff discomfortspeaking
    show beelzebub angry2 at center

    "But Beelzebub didn't take this very well, lunging a spike at the brothers."

    hide beelzebub angry

    "Gabriel strugged in Heathcliff's grip as his brother dragged him along and ran.
    There had to be a better way out of this place, Heathcliff thought, but he went back the same way he went in, fighting off the deciples of Beelzebub on the way."  

    g "Heathcliff you don't understand!! Let me go!" 

    g "Why are you always contradicting me you asshole?!" 

    g "I wont make it out of here Heathcliff.." 


    "Until he just.. accepted it. Heathcliff wasn't letting go, not until Gabriel was safe. And in a way, he felt peace. 
    Even with Beelzebub's wrathful army of insects following them, they were rapidly approaching the light at the end of the hellish staircase."

    "When they stepped into the light, they couldn't believe what they saw. The cult they'd visited was so phased by Heathcliff killing the disciples that they had all slit their own throats in a twisted ritualistic circle."


    h "Ya still want to be a freaky cultist now?" 


    "Heathcliff joked, putting Gabriel down. He didn't want to look at Heathcliff at first, but he shook his head. No, he didn't."

    return

