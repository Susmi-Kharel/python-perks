"""
Builder Design Pattern
-----------------------

A builder design pattern is a creation design pattern that separates the object
construction process in different scenarios.

You can think a builder pattern as a regular PC builder in which different
components are attached when required. For different user, same brand PC might
have different specifications.
"""

from typing import Any, Literal


class PC:
    def __init__(self) -> None:
        self.processor: str | None = None
        self.memory = 0
        self.storage = 0

    def __str__(self) -> str:
        return f"PC with {self.processor} processor ({self.memory}GB RAM, {self.storage}GB HDD)"


class PCBuilder:
    def __init__(self) -> None:
        self.pc = PC()

    def set_processor(self, processor: Literal["amd", "intel", "arm"]):
        self.pc.processor = processor
        return self

    def set_memory(self, value: int):
        self.pc.memory = value
        return self

    def set_storage(self, value: int):
        self.pc.storage = value
        return self

    def build(self):
        return self.pc


if __name__ == "__main__":
    builder = PCBuilder()

    gaming_pc = (
        builder.set_processor("amd")  # set AMD processor
        .set_memory(32)
        .set_storage(1024)
        .build()
    )

    print("Gaming PC: ", gaming_pc)  # PC with amd processor (32GB RAM, 1024GB HDD)

    mobile_pc = (
        builder.set_processor("arm")  # set ARM processor
        .set_memory(value=8)
        .set_storage(256)
        .build()
    )
    print("Mobile PC: ", mobile_pc)  # PC with arm processor (8GB RAM, 256GB HDD)
