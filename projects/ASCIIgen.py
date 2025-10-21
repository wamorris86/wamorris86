"""
This is a work in progress
"""


ascii_art = {
    "A": [
        "    AAA   ",
        "   AA AA  ",
        "  AA   AA ",
        " AAAAAAAAA",
        "AA      AA"
    ],
    "B": [
        "BBBBBBB  ",
        "BB     BB",
        "BBBBBBB  ",
        "BB     BB",
        "BBBBBBB  "
    ],
    "C": [
        " CCCCCCC ",
        "CC       ",
        "CC       ",
        "CC       ",
        " CCCCCCC "
    ],
    "D": [
        "DDDDDDD  ",
        "DD     DD",
        "DD     DD",
        "DD     DD",
        "DDDDDDD  "
    ],
    "E": [
        "EEEEEEEE",
        "EE      ",
        "EEEEEEE ",
        "EE      ",
        "EEEEEEEE"
    ],
    "F": [
        "FFFFFFFF",
        "FF      ",
        "FFFFFF  ",
        "FF      ",
        "FF      "
    ],
    "G": [
        " GGGGGGG ",
        "GG       ",
        "GG   GGGG",
        "GG     GG",
        " GGGGGGG "
    ],
    "H": [
        "HH     HH",
        "HH     HH",
        "HHHHHHHHH",
        "HH     HH",
        "HH     HH"
    ],
    "I": [
        "IIIIIIII",
        "   II   ",
        "   II   ",
        "   II   ",
        "IIIIIIII"
    ],
    "J": [
        "JJJJJJJJ",
        "     JJ ",
        "     JJ ",
        "JJ   JJ ",
        " JJJJ   "
    ],
    "K": [
        "KK    KK",
        "KK   KK ",
        "KKKKK   ",
        "KK   KK ",
        "KK    KK"
    ],
    "L": [
        "LL      ",
        "LL      ",
        "LL      ",
        "LL      ",
        "LLLLLLLL"
    ],
    "M": [
        "MM     MM",
        "MMM   MMM",
        "MM M M MM",
        "MM  M  MM",
        "MM     MM"
    ],
    "N": [
        "NN     NN",
        "NNN    NN",
        "NN N   NN",
        "NN  N  NN",
        "NN   NNN"
    ],
    "O": [
        " OOOOOO ",
        "OO    OO",
        "OO    OO",
        "OO    OO",
        " OOOOOO "
    ],
    "P": [
        "PPPPPPP ",
        "PP    PP",
        "PPPPPPP ",
        "PP      ",
        "PP      "
    ],
    "Q": [
        " QQQQQQ ",
        "QQ    QQ",
        "QQ  Q QQ",
        "QQ   QQ ",
        " QQQQQ Q"
    ],
    "R": [
        "RRRRRRR ",
        "RR    RR",
        "RRRRRRR ",
        "RR  RR  ",
        "RR   RR "
    ],
    "S": [
        " SSSSSS ",
        "SS      ",
        " SSSSSS ",
        "      SS",
        " SSSSSS "
    ],
    "T": [
        "TTTTTTTT",
        "   TT   ",
        "   TT   ",
        "   TT   ",
        "   TT   "
    ],
    "U": [
        "UU    UU",
        "UU    UU",
        "UU    UU",
        "UU    UU",
        " UUUUUU "
    ],
    "V": [
        "VV     VV",
        "VV     VV",
        " VV   VV ",
        "  VV VV  ",
        "   VVV   "
    ],
    "W": [
        "WW     WW",
        "WW     WW",
        "WW  W  WW",
        "WW W W WW",
        " WW   WW "
    ],
    "X": [
        "XX     XX",
        " XX   XX ",
        "  XXXXX  ",
        " XX   XX ",
        "XX     XX"
    ],
    "Y": [
        "YY     YY",
        " YY   YY ",
        "  YYYYY  ",
        "   YYY   ",
        "   YYY   "
    ],
    "Z": [
        "ZZZZZZZZ",
        "     ZZ ",
        "   ZZ   ",
        " ZZ     ",
        "ZZZZZZZZ"
    ],
    " ": [
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    ]
}





text = input("Enter a word: ").upper()

for row in range(5):
    for letter in text:
        if letter in ascii_art:
            print(ascii_art[letter][row], end="  ")
        else:
            print(" " * 8, end="  ")
    print()



