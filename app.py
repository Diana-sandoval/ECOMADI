import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ecomadi 🌱 - Prototipo")

# Colores
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)

# Fuente
FONT = pygame.font.SysFont("arial", 28)

# Estado inicial
energia = 100
agua = 100
residuos = 0

def draw_stats():
    energia_text = FONT.render(f"🌞 Energía: {energia}", True, BLACK)
    agua_text = FONT.render(f"💧 Agua: {agua}", True, BLACK)
    residuos_text = FONT.render(f"🗑️ Residuos: {residuos}", True, BLACK)

    WIN.blit(energia_text, (50, 20))
    WIN.blit(agua_text, (50, 60))
    WIN.blit(residuos_text, (50, 100))

def draw_buttons():
    pygame.draw.rect(WIN, BLUE, (100, 200, 250, 60))
    pygame.draw.rect(WIN, BLUE, (100, 300, 250, 60))
    text1 = FONT.render("Construir panel solar", True, WHITE)
    text2 = FONT.render("Talar árboles", True, WHITE)
    WIN.blit(text1, (110, 215))
    WIN.blit(text2, (110, 315))

def main():
    global energia, agua, residuos
    clock = pygame.time.Clock()
    running = True

    while running:
        WIN.fill(WHITE)
        draw_stats()
        draw_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Botón 1
                if 100 <= x <= 350 and 200 <= y <= 260:
                    energia += 10
                    residuos += 2
                # Botón 2
                elif 100 <= x <= 350 and 300 <= y <= 360:
                    agua -= 15
                    residuos += 10

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
