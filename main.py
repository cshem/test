import os
import pygame
pygame.init()

def main():
    menu()


def menu():

    path = r'C:\Users\Ben\Desktop\test' # !
    lib = os.listdir(path)
    track_name = []

    print(f'{len(lib)} files found in ({path})')
    for i in range(len(lib)):
        print(f'{i + 1} | {lib[i]}')

    track_idx = int(input('select a track id to play: ')) - 1
    track = pygame.mixer.Sound(path + "//" + lib[track_idx])
    print(f'{lib[i]} selected')
    playing(track)


def playing(track, track):

    playing = False

    while True:
        i = input("input: ")
        if i == 'menu':
            menu()
        if i == 'start' and playing == False:
            track.play()
            playing = True
        if i == 'stop':
            track.stop()
            playing = False


main()