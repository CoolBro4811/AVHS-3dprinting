from typing import Optional

class User():
    def __init__(self, name : Optional[str], email : Optional[str], totalVolume : Optional[float], totalWeight : Optional[float], totalCost : Optional[float]) -> None:
        self.name = name
        self.email = email
        self.totalVolume = totalVolume if totalVolume else 0.0
        self.totalWeight = totalWeight if totalWeight else 0.0
        self.totalCost = totalCost if totalCost else 0.0

    def addWeight(self, weight : float):
        self.totalWeight += weight
        return self

    def addVolume(self, volume : float):
        self.totalVolume += volume
        return self
    
    def addCost(self, cost : float):
        self.totalCost += cost
        return self
    
    def __str__(self) -> str:
        return f"{self.name}, {self.email}, {self.totalCost}, {self.totalVolume}, {self.totalWeight}"