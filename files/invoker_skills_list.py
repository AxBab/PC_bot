from auto_invoker_skills import cold_snap, ghost_walk, ice_wall, emp, tornado, alacrity, sound_wave, sunstrike, forge_spirits, chaos_meteor

def check_list(text):
    if text == "инвиз":
        ghost_walk()
    elif text == "торнадо":
        tornado()
    elif text == "метеор":
        chaos_meteor()
    elif text == "волна":
        sound_wave()
    elif text == "sun strike":
        sunstrike()
    elif text == "стена":
        ice_wall()
    elif text == "стремление":
        alacrity()
    elif text == "cold snap":
        cold_snap()
    elif text == "духи":
        forge_spirits()
    elif text == "емп":
        emp()