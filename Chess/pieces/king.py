class King:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start_pos, end_pos, board):
        """
        Şah sadece bir kare hareket edebilir.
        """
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        if abs(start_x - end_x) <= 1 and abs(start_y - end_y) <= 1:
            return True

        return False