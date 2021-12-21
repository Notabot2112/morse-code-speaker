input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    music.playMelody("A - A - A - - - ", 300)
    for (let index = 0; index < 3; index++) {
        basic.pause(200)
        music.playTone(440, music.beat(BeatFraction.Double))
    }
    basic.pause(500)
    music.playMelody("A - A - A - - - ", 300)
})
input.onButtonPressed(Button.A, function () {
    music.playTone(440, music.beat(BeatFraction.Quarter))
})
input.onPinPressed(TouchPin.P2, function () {
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.ForeverInBackground)
})
input.onButtonPressed(Button.B, function () {
    music.playTone(440, music.beat(BeatFraction.Whole))
})
input.onPinPressed(TouchPin.P1, function () {
    music.setVolume(60)
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.OnceInBackground)
    basic.showString("MB | NTB")
    music.setVolume(127)
})
input.onGesture(Gesture.Shake, function () {
    music.stopAllSounds()
})
basic.showString("Morse")
