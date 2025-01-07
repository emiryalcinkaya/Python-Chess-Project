class Rook:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        Kale sadece yatay veya dikey hareket eder.
        """
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        # Yatay veya dikey hareket
        if start_x == end_x or start_y == end_y:
            return True

        return False