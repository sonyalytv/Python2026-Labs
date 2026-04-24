from typing import Protocol

class Serializable(Protocol):
    def serialize(self) -> str:
        ...
    
def export(obj: Serializable) -> None:
    print(obj.serialize())