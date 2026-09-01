from dataclasses import dataclass, asdict

@dataclass
class Expense:
    id: int
    amount: float
    category: str
    date: str
    description: str=""
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls,data:dict)->"Expense":
        return cls(
            id= data["id"],
            amount= data["amount"],
            category= data["category"],
            date= data["date"],
            description= data.get("description",""),
        )

