import pygame
import sys


def check_win(mas: list, sign: str) -> str:
    fillness_check = 0
    for row in mas:
        fillness_check += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if fillness_check == 0:
        return 'p'
    return False


pygame.init()
block_size = 100
margin = 15
width = heigth = block_size * 3 + margin * 4

window_size = (width, heigth)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tic-tac-toe')

black = (0, 0, 0)
grey = (105, 105, 105)
orange = (255, 165, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
count = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            x_col = x_mouse // (block_size + margin)
            y_row = y_mouse // (block_size + margin)
            if mas[y_row][x_col] == 0:
                if count % 2 == 0:
                    mas[y_row][x_col] = 'x'
                else:
                    mas[y_row][x_col] = 'o'
                count += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            count = 0
            window.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = orange
                elif mas[row][col] == 'o':
                    color = teal
                else:
                    color = white
                x = col * block_size + (col + 1) * margin
                y = row * block_size + (row + 1) * margin
                pygame.draw.rect(window, color, (x, y, block_size, block_size))
                if color == orange:
                    pygame.draw.line(window, white, (x + 5, y + 5), (x + block_size - 5, y + block_size - 5), 5)
                    pygame.draw.line(window, white, (x + block_size - 5, y + 5), (x + 5, y + block_size - 5), 5)
                elif color == teal:
                    pygame.draw.circle(window, white, (x + block_size // 2, y + block_size // 2), block_size // 2 - 5, 5)
    if (count - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        window.fill(grey)
        font = pygame.font.SysFont('Arial', 13)
        if game_over == 'x':
            text = font.render('Game over. First player win. Press "Space" to play again', True, white)
        elif game_over == 'o':
            text = font.render('Game over. Second player win. Press "Space" to play again', True, white)
        elif game_over == 'p':
            text = font.render('Game over. Peace. Press "Space" to play again', True, white)
        text_rect = text.get_rect()
        text_x = window.get_width() / 2 - text_rect.width / 2
        text_y = window.get_height() / 2 - text_rect.height / 2
        window.blit(text, [text_x, text_y])
    pygame.display.update()
