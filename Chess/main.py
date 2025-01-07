import pygame
from board import draw_board, draw_pieces, load_piece_images

pygame.init()

# Tahta boyutları ve renkler
BOARD_SIZE = 8  # 8x8lik bir tahta
SQUARE_SIZE = 60  # Karelerin piksel boyutu
WHITE = (255, 255, 255)  # Beyaz
BLACK = (0, 0, 0)  # Siyah
LIGHT_GRAY = (220, 220, 220)  # Açık gri
DARK_GRAY = (100, 100, 100)  # Koyu gri

# Pencerenin Boyutu
WIDTH = HEIGHT = BOARD_SIZE * SQUARE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Oyun döngüsü
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