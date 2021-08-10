import microbit
from micrpbit import
when True:
    input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    for (let index = 0; index < 4; index++) {
        music.playMelody("C5 B E G F B D A ", 500)
    }
    basic.pause(1000)
    music.playMelody("F - F - F - F - ", 120)
    pins.servoWritePin(AnalogPin.P0, 180)
    basic.pause(300)
    pins.servoWritePin(AnalogPin.P0, 0)
   })
    input.onButtonPressed(Button.B, function () {
    music.playMelody("F E D C - - - - ", 120)
   })
    music.playMelody("C D E F - - - - ", 120)
    basic.forever(function () {
    servos.P0.setPulse(2000)
   })
