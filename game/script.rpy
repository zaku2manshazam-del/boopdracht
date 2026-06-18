define g = Character('Gabriel', color="#3c3e5c")
define h = Character('Heathcliff', color="#3c5c3d")
define b = Character('Beelzebub', color="#886412")

image heathcliff neutralspeaking = Transform("heathcliff neutralspeaking.png", xysize=(500, 800))
image heathcliff discomfort = Transform("heathcliff discomfort.png", xysize=(400, 700))
image heathcliff angry = Transform("heathcliff angry.png", xysize=(400, 700))
image heathcliff angryspeaking = Transform("heathcliff angryspeaking.png", xysize=(500, 800))
image heathcliff concerned = Transform("heathcliff concerned.png", xysize=(400, 700))

image beelzebub neutral = Transform("beelzebub neutral.png", xysize=(800, 900))
image beelzebub neutralspeaking = Transform("beelzebub neutral.png", xysize=(900, 1000))
image beelzebub smiling = Transform("beelzebub smiling.png", xysize=(800, 900))
image beelzebub smilingspeaking = Transform("beelzebub smiling.png", xysize=(900, 1000))

image gabriel test1= Transform("gabriel angry1.png")
image gabriel test2= Transform("gabriel angry2.png")

label start:

    scene bg throneroom full

    "This visual novel is a work in progress. Things may be changed."

    "Heathcliff entered a large realm with a reddish atmosphere, it reeked like rotten food and there were all kinds of insects roaming all over. Not dissimilar to a beehive, he noticed the walls had hexagonal holes. 
    And at the center, a tall woman with a large rimmed hat and strange hair that looked almost like wings."

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
    show beelzebub neutral
    show gabriel test1 at right

    "The woman stepped aside, revealing Gabriel. He refused to look Heathcliff in the eyes."

    show gabriel test2 at right

    g "Heathcliff, please stop."

    show gabriel test1 at right
    show heathcliff angryspeaking at left

    h "Gabriel? What the hell's wrong with you?! You think this is good for you, huh? What's gotten into you?!"

    hide gabriel test1
    hide heathcliff angryspeaking

    "Gabriel couldn't look Heathcliff in the eyes, like the coward he was."