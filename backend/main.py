import random
from typing import List

class Randomizer:
    def get_random_num(self, max: int) -> int:
        return random.randint(0, max)

    def get_random_name(self, names: List[str]) -> str:
        return names[self.get_random_num(len(names)) - 1]

    def get_list_names(self, names: List[str]) -> List[str]:
        random.shuffle(names)
        return names;