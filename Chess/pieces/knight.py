class Knight:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        At 'L' şeklinde hareket eder.
        """
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        dx = abs(start_x - end_x)
        dy = abs(start_y - end_y)

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True

        return False