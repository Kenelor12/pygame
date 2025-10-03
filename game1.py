import pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Score Quest")

# Colors and fonts
WHITE = (255, 255, 255)
font = pygame.font.SysFont("Arial", 36)

# Game loop
running = True
score = 0

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (50, 50))

    pygame.display.update()

pygame.quit()
