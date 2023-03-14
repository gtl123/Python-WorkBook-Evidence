from Class import *
p = Player()
e = Enemy("Hitman", 100, 10, 100)
gamestate = "engaged"
while gamestate == "engaged":
    out = p.process(
        e.name,
        e.HP,
        e.Strength,
        e.Emotional_Attachment
        )
    gamestate = out["status"]
    if gamestate == "dead":
        print(out)
        break
    elif gamestate == "Declared Truce":
        print(out)
        break
    elif gamestate == "escaped":
        print(out)
        break
    elif gamestate == "engaged":
        p.HP = out["HP"]
    out = e.process(player_HP=p.HP)
    gamestate = out["status"]
    if gamestate == "dead":
        print(out)
        break
    elif gamestate == "engaged":
        e.HP = out["HP"]
    gamestate = out["status"]
    if gamestate == "dead":
        print("You lost")
        print(out)
        break
