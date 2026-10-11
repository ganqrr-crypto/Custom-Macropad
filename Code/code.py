

#Imports... // i come from c++ so writing in python without semicolons is so wierd
import board


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()


keyboard.matrix = KeysScanner(


    pins = [

        board.D0,

        board.D4,
        
        board.D10,

        board.D5,

        board.D9,


        board.D1,

        board.D3,

        board.D2,

        board.D8,

    ],
    
    value_when_pressed = False,

    
)

keyboard.keymap = [
    [KC.N1,
      KC.N2,
        KC.N3,
     
      KC.N4,
        KC.N5,
          KC.N6,

        KC.N7,
          KC.N8,
            KC.N9]
]



if __name__ == '__main__':
    keyboard.go()


