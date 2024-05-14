gondolt_szám = 0

def on_gesture_shake():
    global gondolt_szám
    gondolt_szám = randint(1, 3)
    if gondolt_szám == 1:
        basic.show_icon(IconNames.DIAMOND)
    elif gondolt_szám == 2:
        basic.show_icon(IconNames.SQUARE)
    elif gondolt_szám == 3:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
