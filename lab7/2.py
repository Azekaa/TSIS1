import pygame
import datetime
pygame.init()
screen= pygame.display.set_mode((500,400))
clock = pygame.time.Clock()
main = pygame.image.load("C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab7\\mainclock.png")
left = pygame.image.load("C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab7\\leftarm.png")
right = pygame.image.load("C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab7\\rightarm.png")
run = True
main = pygame.transform.scale(main,(500,400))
left = pygame.transform.scale(left,(50,480))
right = pygame.transform.scale(right,(500,450))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    current_time = datetime.datetime.now()
    minut = current_time.minute*6*-1
    second = current_time.second*6*-1

    rotate_left = pygame.transform.rotate(left,second)
    rotate_right = pygame.transform.rotate(right,minut)

    screen.blit(main,main.get_rect(center = screen.get_rect().center))
    screen.blit(rotate_left,rotate_left.get_rect(center = screen.get_rect().center))
    screen.blit(rotate_right,rotate_right.get_rect(center = screen.get_rect().center))
    pygame.display.flip()
    clock.tick(50)
pygame.quit()

