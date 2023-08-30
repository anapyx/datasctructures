import numpy as np

from No import No
from LSE import LSE

class LDE(LSE):
    def __init__(self, head):
        self.head = None
        self.tail = None
        self.len = 0

    