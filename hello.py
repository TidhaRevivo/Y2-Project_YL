import pygame
WIDTH, HEIGHT= 1600, 900
WIN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ya Yeet")

WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
RED= (255, 0, 0)
YELLOW=(255, 255, 0)

FPS= 60
BULLETS_VEL=7
VEL =10
MAX_BULLETS= 10
BORDER= pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 100,60
YELLOW_SPACESHIP_IMAGE= pygame.image.load('Assets/spaceship_yellow.png') 
YELLOW_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE= pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

YELLOW_HIT= pygame.USEREVENT + 1
RED_HIT= pygame.USEREVENT + 2

def yellow_handle_momvment(keys_pressed, yellow):
	if keys_pressed[pygame.K_a] and yellow.x- VEL>0: #left
			yellow.x -= VEL
	if keys_pressed[pygame.K_d] and yellow.x+VEL + yellow.width <BORDER.x+40: #right
		yellow.x += VEL
	if keys_pressed[pygame.K_w] and yellow.y-VEL>0: #up
		yellow.y -= VEL
	if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height+ 20< HEIGHT: #down
		yellow.y += VEL
	
def red_handle_momvment(keys_pressed, red):
	if keys_pressed[pygame.K_LEFT] and red.x- VEL>BORDER.x + BORDER.width: #left
			red.x -= VEL
	if keys_pressed[pygame.K_RIGHT] and red.x + VEL<WIDTH - red.width+ 40 : #right
		red.x += VEL
	if keys_pressed[pygame.K_UP] and red.y-VEL>0: #up
		red.y -= VEL
	if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height+ 20< HEIGHT: #down
		red.y += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
	for bullet in yellow_bullets:
		bullet.x+= BULLETS_VEL
		if yellow.colliderect(bullet):
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_bullets.remove(bullet)
	for bullet in red_bullets:
		bullet.x-= BULLETS_VEL
		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_bullets.remove(bullet)


def draw_window(red, yellow, red_bullets, yellow_bullets):
	WIN.fill(WHITE)
	pygame.draw.rect(WIN, BLACK, BORDER)
	WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))
	for bullet in red_bullets:
		pygame.draw.rect(WIN, RED, bullet)
	for bullet in yellow_bullets:
		pygame.draw.rect(WIN, YELLOW, bullet)
	pygame.display.update()
def main():
	red = pygame.Rect(1100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	clock= pygame.time.Clock()
	run= True
	yellow_bullets= []
	red_bullets= []
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run= False
			if event.type == pygame.KEYDOWN:
				
				if event.key== pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
					bullet= pygame.Rect(yellow.x + yellow.width, yellow.y +yellow.height//2- 2, 10 ,5)
					yellow_bullets.append(bullet)
				if event.key== pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
					bullet= pygame.Rect(red.x, red.y +red.height//2- 2, 10 ,5)
					red_bullets.append(bullet)
		keys_pressed = pygame.key.get_pressed()
		yellow_handle_momvment(keys_pressed, yellow)
		red_handle_momvment(keys_pressed, red)
		handle_bullets(yellow_bullets, red_bullets, yellow, red)
		draw_window(red, yellow, red_bullets, yellow_bullets)
		
		
	pygame.quit()

if __name__=="__main__":
	main()
