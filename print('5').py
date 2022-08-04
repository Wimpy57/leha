import pygame
from gun import Gun
import controls

def run():
    
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Альфа 1')
    bgcolor = (0 , 0 , 0)
    gun = Gun(screen)
    while True:
        controls.events(gun)
        gun.updategun()
        screen.fill(bgcolor)
        gun.output()
        pygame.display.flip()
        """^обновляет дисплей"""
        
run()