import pygame
import snake
import food

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# THE GAME IS MADE SO THAT THE SCREEN SIZE MUST BE DIVISBLE BY THE SNAKE AND FOOD
W = 500
H = 500
SNAKE_SIZE = 20
FOOD_SIZE = 20


BGCOLOR = GREEN

# We set up a few things
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
screen.fill(BGCOLOR)

font = pygame.font.SysFont('calibri', 50)


score = 0
running = True
gameOver = False
bodies = []
foods = []
foods.append(food.Food(FOOD_SIZE, (W,H)))
bodies.append(snake.Snake("head", (0,0), SNAKE_SIZE))

while running:
	screen.fill(BGCOLOR)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and bodies[0].direction != "right":
				bodies[0].direction = "left"    

			if event.key == pygame.K_RIGHT and bodies[0].direction != "left":
				bodies[0].direction = "right"
	            
			if event.key == pygame.K_UP and bodies[0].direction != "down":
				bodies[0].direction = "up"

			if event.key == pygame.K_DOWN and bodies[0].direction != "up":
				bodies[0].direction = "down"

			if event.key == pygame.K_SPACE and gameOver:
				gameOver = False
				bodies = []
				foods = []
				foods.append(food.Food(FOOD_SIZE, (W,H)))
				bodies.append(snake.Snake("head", (0,0), SNAKE_SIZE))
				direction = "right"
				score = 0


	if bodies[0].x > W or bodies[0].x < 0 or bodies[0].y > H or bodies[0].y < 0:
		gameOver = True

	for snakee in bodies:
		if snakee.x == bodies[0].x and snakee.y == bodies[0].y and snakee is not bodies[0]:
			gameOver = True

		if gameOver == False:
			snakee.move(bodies)
		
		snakee.draw(screen, RED)

		temp = foods # So we don't edit the array while we go through it
		for foodd in temp:
			if foodd.x == snakee.x and foodd.y == snakee.y:
				bodies.append(snake.Snake("body", (0,0), SNAKE_SIZE))
				foods.remove(foodd)
				foods.append(food.Food(FOOD_SIZE, (500,500)))
				score += 1

	for foodd in foods:
		foodd.draw(screen, WHITE)


	render = font.render(str(score), True, BLACK)
	screen.blit(render, (20,20))

	pygame.display.flip()
	pygame.time.wait(80)