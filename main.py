def on_logo_long_pressed():
    music.play_melody("A - A - A - - - ", 300)
    for index in range(3):
        basic.pause(200)
        music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    basic.pause(500)
    music.play_melody("A - A - A - - - ", 300)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    music.start_melody(music.built_in_melody(Melodies.NYAN),
        MelodyOptions.FOREVER_IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.set_volume(60)
    music.start_melody(music.built_in_melody(Melodies.NYAN),
        MelodyOptions.ONCE_IN_BACKGROUND)
    basic.show_string("MB | NTB")
    music.set_volume(127)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    music.stop_all_sounds()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Morse")