let gondolt_szám = 0
input.onGesture(Gesture.Shake, function () {
    gondolt_szám = randint(1, 3)
    if (gondolt_szám == 1) {
        basic.showIcon(IconNames.Diamond)
    } else if (gondolt_szám == 2) {
        basic.showIcon(IconNames.Square)
    } else if (gondolt_szám == 3) {
        basic.showIcon(IconNames.Scissors)
    }
})
