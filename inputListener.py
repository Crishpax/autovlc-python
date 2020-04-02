from msvcrt import getch


def inputListener(player):

    while True:
        k = getch()
        if k in [b' ', '']:
            print('pause')
            player.pause()
        elif k in [b'\x1b', '\x1b']:
            print('stop')
            player.stop()
        elif k.isdigit():
            player.set_position(float('0.'+str(k)))
