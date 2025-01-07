class Pawn:
    def __init__(self, color):
        """
        Piyon sınıfı.
        color: 'white' veya 'black'
        """
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        Hareket geçerli mi? (Detaylı mantık eklenecek)
        """
        # Örnek: Piyon sadece bir kare ileri gidebilir.
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        direction = 1 if self.color == 'white' else -1

        if start_x == end_x and end_y == start_y + direction:
            return True
        
        return False