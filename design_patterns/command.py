"""
Command Design Pattern
-----------------------

Command Design pattern is a design pattern in which each request is
encapsulated as an object called command. As the command easily capture the
request along with the object and it's method to invoke, we can easily pass
those requests.

Key Components of a command design pattern is as follows:

1. Command Interface: Defines the abstract method `execute` for all concrete commands
2. Concrete Command : A command that implements Command Interface
3. Receiver         : An object that performs the operation
4. Invoker          : An object that stores and executes commands
5. Client           : An object that configures command objects

One of the popular usecase of the command design pattern is game development.
We can encapsulate the behavior of different objects with the single command and
each operations can be invoked using `execute()` method.
"""

from abc import ABC, abstractmethod
from enum import Enum


class Command(ABC):
    """
    This is a Command Interface that defines the blueprint for concrete command.
    """

    @abstractmethod
    def execute(self):
        pass


class Player:
    def run(self):
        print("Player Running")

    def jump(self):
        print("Player Jumping")


class Tank:
    def move(self):
        print("Tank Moving")

    def fire(self):
        print("Tank Firing")


class PlayerRunCommand(Command):
    """
    This is a concrete command that implements the Command Interface.
    """

    def __init__(self, player: Player) -> None:
        self.player = player

    def execute(self):
        self.player.run()


class PlayerJumpCommand(Command):
    def __init__(self, player: Player) -> None:
        self.player = player

    def execute(self):
        self.player.jump()


class TankMoveCommand(Command):
    def __init__(self, tank: Tank) -> None:
        self.tank = tank

    def execute(self):
        self.tank.move()


class TankFireCommand(Command):
    def __init__(self, tank: Tank) -> None:
        self.tank = tank

    def execute(self):
        self.tank.fire()


class Keys(Enum):
    UP = 1
    SPACE = 2


class Controller:
    """
    This is an invoker that stores and executes command on `key_press`
    """

    def __init__(self, commands: dict[Keys, Command]) -> None:
        self.commands = commands

    def key_press(self, key: Keys):
        command = self.commands.get(key)
        """
        The command object here is a receiver that run command
        """
        if command:
            print(f"[ {key:^10s} ]:  ", end="")
            command.execute()


if __name__ == "__main__":
    player = Player()
    tank = Tank()
    """
    Here, player_controller and tank_controller are clients that creates and
    configures command objects
    """

    player_controller = Controller(
        {
            Keys.UP: PlayerRunCommand(player),
            Keys.SPACE: PlayerJumpCommand(player),
        }
    )
    tank_controller = Controller(
        {
            Keys.UP: TankMoveCommand(tank),
            Keys.SPACE: TankFireCommand(tank),
        }
    )

    print("[ Player Active ]".center(40, "="))
    player_controller.key_press(Keys.UP)  # command is invoked
    player_controller.key_press(Keys.SPACE)

    print("[ Tank Active ]".center(40, "="))
    tank_controller.key_press(Keys.UP)
    tank_controller.key_press(Keys.SPACE)

"""
OUTPUT:

===========[ Player Active ]============
[  Keys.UP   ]:  Player Running
[ Keys.SPACE ]:  Player Jumping
============[ Tank Active ]=============
[  Keys.UP   ]:  Tank Moving
[ Keys.SPACE ]:  Tank Firing

"""
