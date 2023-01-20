import random

u1_throws_u2_list = [
    "With precision and skill, {u1} effortlessly lifted and threw {u2} over his shoulder, leaving them lying on the mat in defeat.",
    "{u1} expertly hoisted {u2} onto her shoulder and launched them across the mat with a powerful throw.",
    "{u1} gracefully lifted {u2} and effortlessly flung them over his shoulder with a perfectly executed technique.",
    "With a swift and fluid motion, {u1} picked up {u2} and flung them over her shoulder.",
    "Using his cyber strength, {u1} effortlessly lifted {u2} and tossed them over his shoulder in a show of dominance.",
    "In a display of expert technique, {u1} picked up {u2} and flung them over his shoulder with ease.",
]


def u1_throws_u2(u1, u2):
    return random.choice(u1_throws_u2_list).format(u1=u1, u2=u2)
