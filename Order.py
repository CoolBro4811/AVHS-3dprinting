from typing import Optional

class Order():
    def __init__(self, volume : Optional[float], weight : Optional[float], cost : Optional[float]) -> None:
        self.volume = volume if volume else 0.0
        self.weight = weight if weight else 0.0
        self.cost = cost if cost else 0.0

        def __str__(self) -> str:
            return f"{self.volume}, {self.weight}, {self.cost}"