import keyboard as k
from time import sleep


# Скиллы
def chaos_meteor():
    k.send("e")
    k.send("e")
    k.send("e")
    k.send("w")
    k.send("r")

def tornado():
    k.send("w")
    k.send("w")
    k.send("q")
    k.send("r")

def emp():
    k.send("w")
    k.send("w")
    k.send("w")
    k.send("w")
    k.send("r")

def sound_wave():
    k.send("q")
    k.send("w")
    k.send("e")
    k.send("r")

def ice_wall():
    k.send("q")
    k.send("q")
    k.send("e")
    k.send("r")

def sunstrike():
    k.send("e")
    k.send("e")
    k.send("e")
    k.send("r")

def ghost_walk():
    k.send("q")
    k.send("q")
    k.send("w")
    k.send("r")
    sleep(0.4)
    k.send("f")

def forge_spirits():
    k.send("e")
    k.send("e")
    k.send("q")
    k.send("r")

def cold_snap():
    k.send("q")
    k.send("q")
    k.send("q")
    k.send("r")

def alacrity():
    k.send("w")
    k.send("w")
    k.send("e")
    k.send("r")



# Прокасты
def classic():
    tornado()
    sleep(0.4)
    k.send("f")

    sleep(1.4)
    
    chaos_meteor()
    sleep(0.4)
    k.send("f")

    sound_wave()
    sleep(0.6)
    k.send("f")


def suppress_exit():
    ice_wall()
    sleep(0.4)
    k.send("f")

    forge_spirits()
    sleep(0.4)
    k.send("f")

    emp()
    sleep(0.4)
    k.send("f")

    sleep(0.4)
    ghost_walk()


def arm_damage():
    forge_spirits()
    sleep(0.4)
    k.send("f")

    cold_snap()
    sleep(0.4)
    k.send("f")

    alacrity()
    sleep(0.4)
    k.send("f") 


# Бинд скиллов
k.add_hotkey("q", chaos_meteor)
k.add_hotkey("w", sound_wave)
k.add_hotkey("e", emp)
k.add_hotkey("d", tornado)
k.add_hotkey("s", ice_wall)
k.add_hotkey("a", sunstrike)
k.add_hotkey("z", forge_spirits)
k.add_hotkey("x", ghost_walk)


# Бинд прокастов
k.add_hotkey("1", classic)
k.add_hotkey("2", suppress_exit)
k.add_hotkey("3", arm_damage)


    
    