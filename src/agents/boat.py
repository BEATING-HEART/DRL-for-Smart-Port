from collections import deque
from queue import Queue
from typing import List


class Boat:

    capacity = 0

    @classmethod
    def set_capacity(cls, capacity):
        cls.capacity = capacity

    def __init__(self, init_pos: int = -1) -> None:
        self.pos = init_pos

        self.goodlist = deque()  # save good value in the goodlist
        """goods on the boat (len = current goods number, sum = goods value on the boat)"""
        # self.score = 0

        self.status = 0
        """
        `0`: moving \n
        `1` at the berth or discharging port (virtual point) \n
        `2` waiting outside the berth (in berth waiting list)
        """

        self.waiting_list = deque()
        """berth waiting list (if needed)"""

        self.target = -1
        """target: berth to arrive"""
        self.reach_time = -1

    def sample_action(self):
        """output all actions of boat include ship and go"""
        pass

    def safe_load(self, goods: List[float]) -> int:
        """load goods from list

        Args:
            goods (List[float]): goods value list

        Returns:
            int: number of goods loaded
        """
        spare_space = Boat.capacity - self.cnt
        insert = min(spare_space, len(goods))
        self.goodlist.extend(goods[:insert])
        return insert

    def unload(self) -> float:
        """unload all goods on the boat

        Returns:
            float: sum of goods value
        """
        value = self.val
        self.goodlist.clear()
        return value

    @property
    def cnt(self):
        """count the number of goods on the boat"""
        return len(self.goodlist)

    @property
    def val(self):
        """sum the value of goods on the boat"""
        return sum(self.goodlist)
