import sys
import pygame
from pydub import AudioSegment

finalTrack = []

resolution_x = 480
resolution_y = 480
screen = pygame.display.set_mode((resolution_x, resolution_y))
pygame.init()
pygame.mixer.init()

music1 = pygame.mixer.Sound('bassDrum.mp3')
music2 = pygame.mixer.Sound('cymbal.mp3')
music3 = pygame.mixer.Sound('hiHat.mp3')
music4 = pygame.mixer.Sound('snare.mp3')
music5 = pygame.mixer.Sound('tomDrum.mp3')
music6 = pygame.mixer.Sound('tomDrum2.mp3')
music7 = pygame.mixer.Sound('tomDrum3.mp3')
screen.fill((200, 200, 0))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print('bass')
                music1.play()
                finalTrack.append(AudioSegment.from_mp3('bassDrum.mp3'))
            elif event.key == pygame.K_2:
                print('cymbal')
                music2.play()
                finalTrack.append(AudioSegment.from_mp3('cymbal.mp3'))
            elif event.key == pygame.K_3:
                print('hiHat')
                music3.play()
                finalTrack.append(AudioSegment.from_mp3('hiHat.mp3'))
            elif event.key == pygame.K_4:
                print('snare')
                music4.play()
                finalTrack.append(AudioSegment.from_mp3('snare.mp3'))
            elif event.key == pygame.K_5:
                print('tomDrum')
                music5.play()
                finalTrack.append(AudioSegment.from_mp3('tomDrum.mp3'))
            elif event.key == pygame.K_6:
                print('tomDrum2')
                music6.play()
                finalTrack.append(AudioSegment.from_mp3('tomDrum2.mp3'))
            elif event.key == pygame.K_7:
                print('tomDrum3')
                music7.play()
                finalTrack.append(AudioSegment.from_mp3('tomDrum3.mp3'))
            elif event.key == pygame.K_ESCAPE:
                # Concatenate the audio segments in finalTrack
                finalAudioOutput = sum(finalTrack)
                # Export the final audio output as an mp3 file
                finalAudioOutput.export("/home/csl/Downloads/drumOutput.mp3", format="mp3")
                pygame.quit()
                sys.exit()

    clock.tick(120)