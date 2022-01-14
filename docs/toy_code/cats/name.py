from enum import Enum

class CornerAnchorMode:
    TOP_LEFT = "tl"
    TOP_RIGHT = "tr"
    BOTTOM_LEFT = 'bl'
    BOTTOM_RIGHT = 'br'


class RotateMode(Enum):
    KEEP_BLACK = 0
    CROP_BLACK = 1
    SAVE_ORIGINAL_SIZE = 2
