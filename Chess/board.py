import pygame

pygame.init()

# Tahta boyutları ve renkler
BOARD_SIZE = 8  # 8x8lik bir tahta
SQUARE_SIZE = 60  # Her bir karenin piksel boyutları
WHITE = (255, 255, 255)  # Beyaz
BLACK = (0, 0, 0)  # Siyah
LIGHT_GRAY = (220, 220, 220)  # Açık gri
DARK_GRAY = (100, 100, 100)  # Koyu gri

# Pencerenin boyutu
WIDTH = HEIGHT = BOARD_SIZE * SQUARE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Taş resimlerini yükleme
def load_piece_images():
    pieces = {}
    pieces['wp'] = pygame.image.load('images/white_pawn.png')  # Beyaz piyon
    pieces['bp'] = pygame.image.load('images/black_pawn.png')  # Siyah piyon
    pieces['wr'] = pygame.image.load('images/white_rook.png')  # Beyaz kale
    pieces['br'] = pygame.image.load('images/black_rook.png')  # Siyah kale
    pieces['wn'] = pygame.image.load('images/white_knight.png')  # Beyaz at
    pieces['bn'] = pygame.image.load('images/black_knight.png')  # Siyah at
    pieces['wb'] = pygame.image.load('images/white_bishop.png')  # Beyaz fil
    pieces['bb'] = pygame.image.load('images/black_bishop.png')  # Siyah fil
    pieces['wq'] = pygame.image.load('images/white_queen.png')  # Beyaz vezir
    pieces['bq'] = pygame.image.load('images/black_queen.png')  # Siyah vezir
    pieces['wk'] = pygame.image.load('images/white_king.png')  # Beyaz şah
    pieces['bk'] = pygame.image.load('images/black_king.png')  # Siyah şah
    return pieces

# Tahtayı çizme
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = LIGHT_GRAY if (row + col) % 2 == 0 else DARK_GRAY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Taşları tahtaya yerleştirme
def draw_pieces(pieces):
    # Beyaz taşlar
    screen.blit(pieces['wp'], (0 * SQUARE_SIZE, 6 * SQUARE_SIZE))  # Beyaz piyon
    screen.blit(pieces['wr'], (0 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz kale
    screen.blit(pieces['wn'], (1 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz at
    screen.blit(pieces['wb'], (2 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz fil
    screen.blit(pieces['wq'], (3 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz vezir
    screen.blit(pieces['wk'], (4 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz şah
    screen.blit(pieces['wn'], (5 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz at
    screen.blit(pieces['wb'], (6 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz fil
    screen.blit(pieces['wr'], (7 * SQUARE_SIZE, 7 * SQUARE_SIZE))  # Beyaz kale

    # Siyah taşlar
    screen.blit(pieces['bp'], (0 * SQUARE_SIZE, 1 * SQUARE_SIZE))  # Siyah piyon
    screen.blit(pieces['br'], (0 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah kale
    screen.blit(pieces['bn'], (1 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah at
    screen.blit(pieces['bb'], (2 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah fil
    screen.blit(pieces['bq'], (3 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah vezir
    screen.blit(pieces['bk'], (4 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah şah
    screen.blit(pieces['bn'], (5 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah at
    screen.blit(pieces['bb'], (6 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah fil
    screen.blit(pieces['br'], (7 * SQUARE_SIZE, 0 * SQUARE_SIZE))  # Siyah kale

# Ana oyun döngüsü
def main():
    running = True
    pieces = load_piece_images()  # Taşları yükle
    while running:
        screen.fill(WHITE)  # Ekranı temizle
        draw_board()  # Tahtayı çiz
        draw_pieces(pieces)  # Taşları tahtada göster

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()  # Ekranı güncelle

    pygame.quit()

# Oyunu başlat
if __name__ == "__main__":
    main()