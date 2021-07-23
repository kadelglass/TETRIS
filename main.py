# imports
import pygame


# main game function:
def main():
    # init:
    pygame.init()

    # init display
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Pygame Tetris")

    # offset
    offset = 2

    # level init
    level = 1

    # run loop bool
    carryOn = True

    # main game loop:
    while carryOn:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # draw:

        # background
        screen.fill((0, 0, 0))

        # render grid

        # grid grid
        for i in range(0, 10):
            # vertical line
            pygame.draw.line(screen, (50, 50, 50), (i * 50, 0), (i * 50, screen.get_height()), 5)
        for j in range(0, 12):
            # horizontal line
            pygame.draw.line(screen, (50, 50, 50), (0, j * 50), (500, j * 50), 5)

        # outline
        # top line
        pygame.draw.line(screen, (255, 255, 255), (0, offset), (screen.get_width(), offset), 5)
        # left line
        pygame.draw.line(screen, (255, 255, 255), (offset, 0), (offset, screen.get_height()), 5)
        # right line
        pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, screen.get_height()), 5)
        # far right line
        pygame.draw.line(screen, (255, 255, 255), (screen.get_width() - offset, 0),
                         (screen.get_width() - offset, screen.get_height()), 5)
        # bottom line
        pygame.draw.line(screen, (255, 255, 255), (0, screen.get_height() - offset),
                         (screen.get_width(), screen.get_height() - offset), 5)

        # draw menu text

        # level text
        font = pygame.font.SysFont("Showcard Gothic", 32)
        levelText = font.render("Level " + str(level), False, (255, 255, 255))
        screen.blit(levelText, (500 + offset + 5, 5 + offset))
        # level line
        pygame.draw.line(screen, (255, 255, 255), (500 - offset, 5 + offset + 5 + levelText.get_height()),
                         (screen.get_width(), 5 + offset + 5 + levelText.get_height()), 5)

        # refresh display
        pygame.display.flip()


# run game function
if __name__ == "__main__":
    main()
