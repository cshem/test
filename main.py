import os
import pygame
pygame.init()

path = 'x' # !
lib = os.listdir(path)

def main():

    print(f'{len(lib)} files found in ({path})')
    for i in range(len(lib)):
        print(f'{i + 1} | {lib[i]}')

    track_idx = int(input('hahahahaha ')) - 1
    track = pygame.mixer.Sound(path + "//" + lib[track_idx])

    track.play()


main()
