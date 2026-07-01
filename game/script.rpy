define g = Character('Gabriel', color="#3c3e5c")
define h = Character('Heathcliff', color="#3c5c3d")
define b = Character('Beelzebub', color="#886412")

image heathcliff neutralspeaking = Transform("heathcliff neutralspeaking.png", xysize=(450, 800))
image heathcliff discomfort = Transform("heathcliff discomfort.png", xysize=(400, 700))
image heathcliff discomfortspeaking = Transform("heathcliff discomfortspeaking.png", xysize=(450, 800))
image heathcliff angry = Transform("heathcliff angry.png", xysize=(400, 700))
image heathcliff angryspeaking = Transform("heathcliff angryspeaking.png", xysize=(450, 800))
image heathcliff concerned = Transform("heathcliff concerned.png", xysize=(400, 700))
image heathcliff concernedspeaking = Transform("heathcliff concernedspeaking.png", xysize=(450, 800))
image heathcliff death = Transform("heathcliff death.png", xysize=(400, 700))

image beelzebub neutral = Transform("beelzebub neutral.png", xysize=(800, 900))
image beelzebub closeup = Transform("beelzebub smiling.png", xysize=(1200, 1300))
image beelzebub neutralspeaking = Transform("beelzebub neutralspeaking.png", xysize=(850, 950))
image beelzebub smiling = Transform("beelzebub smiling.png", xysize=(800, 900))
image beelzebub smilingspeaking = Transform("beelzebub smilingspeaking.png", xysize=(850, 950))
image beelzebub angry = Transform("beelzebub angry.png", xysize=(800, 900))
image beelzebub angry2 = Transform("beelzebub angry.png", xysize=(1100, 1200))
image beelzebub creepy = Transform("beelzebub creepy.png", xysize=(800, 900))

image gabriel neutral = Transform("gabriel neutral.png", xysize=(500, 800))
image gabriel neutralspeaking = Transform("gabriel neutralspeaking.png", xysize=(500, 800))
image gabriel trauma = Transform("gabriel trauma.png", xysize=(50, 800))
image gabriel traumaspeaking = Transform("gabriel traumaspeaking.png", xysize=(500, 800))

transform centerright:
    xalign 0.9
    yalign 1.0

transform gabrielpos:
    xalign 0.99
    yalign 1.0
    xzoom -1.0

transform gabrielspeakpos:
    xalign 0.99
    yalign 1.0
    xzoom -1.0

label start:
    with fade
    scene bg black

    "This visual novel is a work in progress. Things may be changed."

    "{color=#6E6E6E}Heathcliff entered a large realm with a reddish atmosphere, it reeked like rotten food and there were all kinds of insects roaming all over. 
    Not dissimilar to a beehive, he noticed the walls had hexagonal holes.{/color}"

    scene bg throneroom closeup
    show beelzebub closeup at center
    
    "{color=#6E6E6E}And at the center, a tall woman with a large rimmed hat and strange hair that looked almost like wings.{/color}"

    h "{color=#4C7063}{i}She must be the one behind this mess.. She has to know where Gabriel is.{/i}{/color}"

    scene bg throneroom full
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

    "{color=#6E6E6E}Heathcliff didn't like the woman's tone.. She seemed quite strange.{/color}"

    show beelzebub neutral at right
    show heathcliff angryspeaking at left

    h "Excuse me?! Where the hell is he?!"

    show heathcliff concerned at left
    show beelzebub neutral at centerright
    show gabriel neutral at gabrielpos

    "{color=#6E6E6E}The woman stepped aside, revealing Gabriel. He refused to look Heathcliff in the eyes.{/color}"

    show gabriel neutralspeaking at gabrielspeakpos

    g "Heathcliff, please stop."

    show gabriel neutral at gabrielpos
    show heathcliff angryspeaking at left

    h "Gabriel? What the hell's wrong with you?! You think this is good for you, huh? What's gotten into you?!"

    hide gabriel neutral
    hide beelzebub neutral
    hide heathcliff angryspeaking

    "{color=#6E6E6E}Gabriel couldn't look Heathcliff in the eyes, like the coward he was.{/color}"

    show gabriel neutral at gabrielpos
    show beelzebub neutral at centerright
    show heathcliff angryspeaking at left

    h  "Gabriel, you think this is going to fix your mental shit, huh? Those people talked you into some paranormal bullshit, and now you think you found the answer?" 

    h  "And you—You're her, right? Those freaks that pushed me in here. You're their God, arent you?!" 

    show beelzebub neutral at centerright
    show heathcliff angry at left

    "{color=#6E6E6E}Heathcliff shouted, his anger overboiling, but the woman didn't seem phased at all..{/color}"

    show beelzebub neutralspeaking at centerright

    b "One has little control over measly activities some mortals had convinced my new disciple of. 
    Even so, they did him a favor. The world is a terrible and uncomfortable nest of parasites drilling on the turf."
    b "No matter what you think of it, you're either a measly sheep following a crowd, slurping and sucking Earths energy, 
    or you stay in the shadow of your superior, leech off of their confidence so you can rise up yourself. "  

    show beelzebub neutral at centerright
    show heathcliff angryspeaking at left

    h "That's pathetic. Gabriel, you don't actually believe in this bullshit, do you?"

    show heathcliff angry at left

    "{color=#6E6E6E}But Gabriel didn't bat an eye. He just looked like a toddler who just got caught lying. Heathcliff couldn't let himself just give up.{/color}"

    show gabriel neutralspeaking at gabrielpos

    g "Heathcliff, stop trying to care."

    show gabriel neutral at gabrielpos
    show heathcliff angryspeaking at left

    h ".. What?" 

    show gabriel neutralspeaking at gabrielpos
    show heathcliff discomfort at left

    g "Stop trying to convince yourself you care about me. The only thing you want is credit for whatever job you do. You drag me around like an obstacle."  

    show gabriel neutral at gabrielpos
    show heathcliff discomfortspeaking at left

    h "Oh don't you dare. I've done nothing but cover for your lazy ass every time. And who seemed to be getting more praise?! {i}You{/i}." 

    show heathcliff discomfort at left

    "{color=#6E6E6E}Not that Heathcliff cared about that. Gabriel was pulling out every excuse in the book to stay with this freak.{/color}"

    show heathcliff discomfortspeaking at left

    h "Gabriel, you know damn well that mom and dad aren't in our lives anymore. Why are you still lingering on the past?"

    "{color=#6E6E6E}Heathcliff got closer, wanting to grab Gabriel's hand, but Gabriel just stepped away.{/color}"

    hide gabriel neutral
    hide heathcliff discomfortspeaking
    hide beelzebub neutral

    menu:
        "{color=#6E6E6E}How will Heathcliff convince Gabriel? Use force or use words?{/color}"

        "Force.":
            " "
            jump forceful

        "Words.":
            " "
            jump peaceful


label forceful:
    with dissolve
    scene bg throneroom full

    "{color=#6E6E6E}Heathcliff stepped forward to Gabriel once more, grabbing his arm and pulling him closer and swinging him behind his back.{/color}"

    h "Gabriel. I'll make sure you get the help you need." 

    show beelzebub angry2 at center

    "{color=#6E6E6E}But as Heathcliff could've predicted, Beelzebub didn't take this very well, lunging a spike at the brothers.{/color}"

    hide beelzebub angry

    "{color=#6E6E6E}Gabriel strugged in Heathcliff's grip as his brother dragged him along and ran.
    There had to be a better way out of this place, Heathcliff thought, but he went back the same way he went in, fighting off the deciples of Beelzebub on the way.{/color}"  

    g "Heathcliff you don't understand!! Let me go!" 

    g "Why are you always contradicting me you asshole?!" 

    g "I wont make it out of here Heathcliff.." 

    "{color=#6E6E6E}Until he just.. accepted it. Heathcliff wasn't letting go, not until Gabriel was safe. And in a way, he felt peace. 
    Even with Beelzebub's wrathful army of insects following them, they were rapidly approaching the light at the end of the hellish staircase.{/color}"

    "{color=#6E6E6E}When they stepped into the light, they couldn't believe what they saw. 
    The cult they'd visited was so phased by Heathcliff killing the disciples that they had all slit their own throats in a twisted ritualistic circle.{/color}"

    h "Ya still want to be a freaky cultist now?" 

    "{color=#6E6E6E}Heathcliff joked, putting Gabriel down. He didn't want to look at Heathcliff at first, but he shook his head. No, he didn't.{/color}"

    scene bg endinggood
    scene black with fade
    pause 10.0
    return

label peaceful:
    with dissolve
    scene bg throneroom full

    "{color=#6E6E6E}Heathcliff stepped forward to Gabriel once more, hands shaking lightly.{/color}"

    show gabriel neutral at gabrielpos
    show heathcliff concernedspeaking at left
    show beelzebub neutral at centerright

    h "Gabriel, please. Just come with me. You know this isn't right."

    show gabriel neutralspeaking at right
    show heathcliff concerned at left
    show beelzebub smiling at centerright
    g "Heathcliff, you just don't understand. It's for the best if I stay."
    
    show gabriel neutral at right
    show heathcliff concernedspeaking at left

    h "Gabriel—{i}Please{/i} brother. You can't stay here!"

    show heathcliff concerned at left
    show beelzebub smilingspeaking at centerright

    b "Your brother has spoken. I believe it is time for you to make your way out, Heathcliff.. We would not want to make him upset, now would we?"

    show heathcliff discomfortspeaking at left
    show beelzebub smiling at centerright

    h "You're not seriously listening to this freak, are you? Gabriel—"

    show heathcliff discomfort at left
    show gabriel neutralspeaking at right

    g "Heathcliff. I've made my choice."

    show heathcliff angryspeaking at left
    show gabriel neutral at right

    h "{i}Gabriel{/i}, don't be like this. We can just go home! You want me to care less about credit on our jobs? {i}Fine{/i}, 
    I'll stop whining about the credit so much, but damnit just come with me!"

    show heathcliff angry at left
    show beelzebub creepy at centerright

    b "Oh.. Oops.. It seems my powers {color=#690909}slipped.{/color}"

    show heathcliff death at left
    show gabriel trauma at right
    with dissolve

    "{color=#6E6E6E}Heathcliff's gaze went down to where blood was rapidly staining his own shirt, the piercing pain from his back making his breath hitch.{/color}"

    show gabriel traumaspeaking at right

    g "... Heathcliff? HEATHCLIFF?!"

    show gabriel trauma at right

    "{color=#6E6E6E}But as Heathcliff could see Gabriel finally run over, he sunk through his knees, vision going dark. He couldn't form words anymore, but his last thought was that he was sorry to leave his brother behind.{/color}"

    scene bg endingbad with fade
    pause 10.0
    return