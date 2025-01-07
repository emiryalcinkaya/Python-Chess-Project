class Bishop:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        Fil sadece çapraz hareket eder.
        """
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        if abs(start_x - end_x) == abs(start_y - end_y):
            return True

        return False