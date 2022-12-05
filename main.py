from board_class import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('The Life')

    screen = pygame.display.set_mode(DIMENSIONS)

    board = Board(DIMENSIONS, screen)

    board.draw_map()

    TURN = pygame.USEREVENT + 1
    pygame.time.set_timer(TURN, 100)

    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == TURN and board.start:
                board.turn()
                pygame.display.flip()
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and (not board.start):
                if event.button == 1:
                    bird_pos = event.pos
                    board.add_cell([bird_pos[0] // CELL_SIZE, bird_pos[1] // CELL_SIZE])
                    board.draw_cell([bird_pos[0] // CELL_SIZE, bird_pos[1] // CELL_SIZE])
                    pygame.display.flip()
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if board.start:
                        board.start = False
                    else:
                        board.start = True
                if event.key == pygame.K_r and (not board.start):
                    board.random()
                    pygame.display.flip()
                    pygame.display.update()
                if event.key == pygame.K_c and (not board.start):
                    board.clear()
                    pygame.display.flip()
                    pygame.display.update()
