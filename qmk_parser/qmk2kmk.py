#!/usr/bin/python
import sys
import json

class Atreus62:
    # A class should be created for each matrix type

    # this layout follows the physical wiring of the matrix.
    # this was a hand wired build for me, so the actual wiring may differ from
    # from other tutorials online

    # there is an extra row to accomodate the thumb keys, this can also  be used
    # for encoder buttons wired into matrix.  This layout gives my drop in 
    # success for converting qmk configurator keymap for atreus62.  It will 
    # require thought, but this should be capable for all other keymaps 
    # provided that you know the wiring of the matrix 
    rows = 6
    cols = 12
    matrix = [
        0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11,
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 
        48, 49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 61,
        -1, -1, -1, -1, -1, 54, 55 , -1,-1, -1, -1, -1
    ]

class Dactyl4x6:
    rows = 4
    cols = 12
    matrix = [
        0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  11,
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
        -2, -2, -2, 36, 37, 38, 39, 40, 41, -2, -2, -2
    ]

class Translator:
    
    debug = False
    keymap = []  
    keyslot = 12
    tab = '    '
    # this was a quick and dirty lookup dict that fit my purpouse for the
    # atreus62.  Please expand for your needs
    key_lookup = {
        'KC_1'    : 'KC.N1',
        'KC_2'    : 'KC.N2',
        'KC_3'    : 'KC.N3',
        'KC_4'    : 'KC.N4',
        'KC_5'    : 'KC.N5',
        'KC_6'    : 'KC.N6',
        'KC_7'    : 'KC.N7',
        'KC_8'    : 'KC.N8',
        'KC_9'    : 'KC.N9',
        'KC_0'    : 'KC.N0',
        'KC_P1'   : 'KC.P1',
        'KC_P2'   : 'KC.P2',
        'KC_P3'   : 'KC.P3',
        'KC_P4'   : 'KC.P4',
        'KC_P5'   : 'KC.P5',
        'KC_P6'   : 'KC.P6',
        'KC_P7'   : 'KC.P7',
        'KC_P8'   : 'KC.P8',
        'KC_P9'   : 'KC.P9',
        'KC_P0'   : 'KC.P0',
        'KC_A'    : 'KC.A',
        'KC_B'    : 'KC.B',
        'KC_C'    : 'KC.C',
        'KC_D'    : 'KC.D',
        'KC_E'    : 'KC.E',
        'KC_F'    : 'KC.F',
        'KC_G'    : 'KC.G',
        'KC_H'    : 'KC.H',
        'KC_I'    : 'KC.I',
        'KC_J'    : 'KC.J',
        'KC_K'    : 'KC.K',
        'KC_L'    : 'KC.L',
        'KC_M'    : 'KC.M',
        'KC_N'    : 'KC.N',
        'KC_O'    : 'KC.O',
        'KC_P'    : 'KC.P',
        'KC_Q'    : 'KC.Q',
        'KC_R'    : 'KC.R',
        'KC_S'    : 'KC.S',
        'KC_T'    : 'KC.T',
        'KC_U'    : 'KC.U',
        'KC_V'    : 'KC.V',
        'KC_W'    : 'KC.W',
        'KC_X'    : 'KC.X',
        'KC_Y'    : 'KC.Y',
        'KC_Z'    : 'KC.Z',
        'KC_NO'   : 'KC.NO',
        'KC_TRNS' : 'KC.TRNS',
        'KC_TILD' : 'KC.TILD',
        'KC_COMM' : 'KC.COMM',
        'KC_DOT'  : 'KC.DOT',
        'KC_SLSH' : 'KC.SLSH',
        'KC_LBRC' : 'KC.LBRC',
        'KC_LCTL' : 'KC.LCTL',
        'KC_LGUI' : 'KC.LGUI',
        'KC_LALT' : 'KC.LALT',
        'KC_LSFT' : 'KC.LSFT',
        'KC_RBRC' : 'KC.RBRC',
        'KC_RCTL' : 'KC.RCTL',
        'KC_RGUI' : 'KC.RGUI',
        'KC_RALT' : 'KC.RALT',
        'KC_RSFT' : 'KC.RSFT',
        'KC_GRV'  : 'KC.GRV',
        'KC_BSPC' : 'KC.BSPC',
        'KC_DEL'  : 'KC.DEL',
        'KC_ENT'  : 'KC.ENT',
        'KC_SPC'  : 'KC.SPC',
        'KC_EQL'  : 'KC.EQL',
        'KC_MINS' : 'KC.MINS',
        'KC_QUOT' : 'KC.QUOT',
        'KC_RGUI' : 'KC.RGUI',
        'KC_LPRN' : 'KC.LPRN',
        'KC_RPRN' : 'KC.RPRN',
        'KC_LCBR' : 'KC.LCBR',
        'KC_RCBR' : 'KC.RCBR',
        'KC_TAB'  : 'KC.TAB',
        'KC_UP'   : 'KC.UP',
        'KC_DOWN' : 'KC.DOWN',
        'KC_LEFT' : 'KC.LEFT',
        'KC_RIGHT': 'KC.RIGHT',
        'KC_UNDS' : 'KC.UNDS',
        'KC_PSLS' : 'KC.PSLS',
        'KC_PAST' : 'KC.PAST',
        'KC_PPLS' : 'KC.PPLS',
        'KC_EQUAL': 'KC.EQUAL',
        'KC_ESC'  : 'KC.ESC',
        'KC_BSLS' : 'KC.BSLS',
        'KC_SCLN' : 'KC.SCLN',
        'KC_RGHT' : 'KC.RGHT',
        'KC_PGDN' : 'KC.PGDN',
        'KC_F1'   : 'KC.F1',
        'KC_F2'   : 'KC.F2',
        'KC_F3'   : 'KC.F3',
        'KC_F4'   : 'KC.F4',
        'KC_F5'   : 'KC.F5',
        'KC_F6'   : 'KC.F6',
        'KC_F7'   : 'KC.F7',
        'KC_F8'   : 'KC.F8',
        'KC_F9'   : 'KC.F9',
        'KC_F10'  : 'KC.F10',
        'KC_F11'  : 'KC.F11',
        'KC_F12'  : 'KC.F12',
        'KC_F13'  : 'KC.F13',
        'RESET'   : 'KC.RESET',
        'KC_CAPS' : 'KC.CAPS',
        'KC_HASH' : 'KC.HASH',
        'KC_AT'   : 'KC.AT',
        'KC_DLR'  : 'KC.DLR',
        'KC_PERC' : 'KC.PERC',
        'KC_EXLM' : 'KC.EXLM',
        'KC_CIRC' : 'KC.CIRC',
        'KC_AMPR' : 'KC.AMP',
        'KC_ASTR' : 'KC.AST',
        'KC_PLUS' : 'KC.PLUS',
        'KC_PIPE' : 'KC.PIPE',
        'RGB_TOG' : 'KC.RGB_TOG',
        'RGB_HUI' : 'KC.RGB_HUI',
        'RGB_SAI' : 'KC.RGB_SAI',
        'RGB_VAI' : 'KC.RGB_VAI',
        'RGB_MOD' : 'KC.RGB_MODE_PLAIN',
        'RGB_HUD' : 'KC.RGB_HUD',
        'RGB_SAD' : 'KC.RGB_SAD',
        'RGB_VAD' : 'KC.RGB_VAD',

    }

    def __init__(self, qmk_file, keyboard, debug=False):
        self.qmk_file = qmk_file
        self.keyboard = keyboard
        self.debug = debug

    def parse_anykey(self, key):
        newkey = key.split('(')
        newkey = newkey[1].split(')')[0]
        return newkey

    def parse_mo(self, key):
        return f'KC.MO({self.split_key(key)})'

    def parse_to(self, key):
        return f'KC.TO({self.split_key(key)})'

    def parse_tt(self, key):
        return f'KC.TT({self.split_key(key)})'

    def parse_tg(self, key):
        return f'KC.TG({self.split_key(key)})'

    def parse_df(self, key):
        return f'KC.DF({self.split_key(key)})'
    
    def split_key(self, key):
        newkey = key.split('(')
        newkey = newkey[1].split(')')[0]
        return newkey

    def parse(self):
        # read in info.json form qmk configurator download
        with open(self.qmk_file,'r') as f:
            # store json info in a dict
            data = json.load(f)
            # iterate through keymap layers
            for layer in range(len(data['layers'])):
                layer_list = []
                 # for each layer, convert the key from qmk to kmk
                for idx,key in enumerate(self.keyboard.matrix):
                    if key == -1:
                        # this lets us fill in our matrix if it is larger than 
                        # the map read in from qmk, fills holes with KC.NO
                        layer_list.append('XXXXXXX')
                    elif key == -2:
                        layer_list.append('_______')
                    else:
                        # where ther is a valid index in the json, put it in the
                        # correct place in the kmk keymap
                        if 'ANY' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_anykey(data['layers'][layer][key])
                                )
                        elif 'MO(' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_mo(data['layers'][layer][key])
                                )
                        elif 'TO(' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_to(data['layers'][layer][key])
                                )
                        elif 'TT(' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_tt(data['layers'][layer][key])
                                )
                        elif 'TG(' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_tg(data['layers'][layer][key])
                                )
                        elif 'DF(' in data['layers'][layer][key]:
                            layer_list.append(
                                self.parse_tf(data['layers'][layer][key])
                                )
                        else:
                            layer_list.append(
                                self.key_lookup[data['layers'][layer][key]]
                                )
                # add the layer to our new list of layers
                self.keymap.append(layer_list)
        # produce a kmk keymap that can be pasted into our main.py
        self.translate()
        if self.debug:
            print(self.keymap)

    # this just prints out the new keymap in a format that can be pasted into 
    # our main.py.  the final product isnt pretty yet, but usable
    def translate(self):
        line = ''
        count = 0
        print('keyboard.keymap = [')
        for layer in self.keymap:
            self.keyslot = len(max(layer, key=len))+3
            print(f'{self.tab}[')
            for idx,key in enumerate(layer):
                if count <= self.keyboard.cols - 1:
                    line += f'{key}, '
                    for s in range(self.keyslot-len(key)):
                        line += ' '
                    count += 1
                if count > self.keyboard.cols - 1:
                    print(f'{self.tab*2}{line}')
                    line = ''
                    count = 0
            print(f'{self.tab}],')
        print(']')

# usage - path to json file as the only argument
if __name__ == '__main__':
    #translator = Translator(sys.argv[1], Atreus62()).parse()
    translator = Translator(sys.argv[1], Dactyl4x6()).parse()
