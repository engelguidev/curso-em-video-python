import pygame


while True:
    quest = str(input('Deseja escutar música boa? [S/N] ')).upper()[0]
    if quest in 'N':
        print('Jesus Amado.. escuta isso ai..')
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('jesusamado.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
    elif quest in 'S':
        print('Aproveite o saudosista, Tião Carreiro!')
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('nove.e.nove.tiao.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
    else:
        print('Somente Sim ou Não, por favor, analfabeto.')


