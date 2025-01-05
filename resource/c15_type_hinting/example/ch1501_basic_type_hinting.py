id: int = 1
name: str = "John Doe"
subjects: list[str] = ["Physics", "Chemistry", "Biology"]
data: dict[str, int] = {
    "roll": 1,
    "age": 10,
    "grade": 5,
}


def add(x: int, y: int) -> int:
    return x + y
