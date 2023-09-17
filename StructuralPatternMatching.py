from dataclasses import dataclass
from typing import List
import shlex


def run_command(command: str) -> None:
    match command:
        case "quit":
            print("Quitting the program")
            quit()


def run_command2(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename]:
            print(f"Saving file: {filename}")
        case ["quit" | "exit" | "bye", *rest]:
            if "--force" in rest or "-f" in rest:
                print("Sending SIGTERM to all processes and quitting the program")
            else:
                print(f"Quitting the program")
            quit()


def run_command3(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename]:
            print(f"Saving file: {filename}")
        case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print("Sending SIGTERM to all processes and quitting the program")
            quit()
        case ["quit" | "exit" | "bye"]:
            print(f"Quitting the program")
            quit()


@dataclass
class Command:
    command: str
    arguments: List[str]


def run_command4(command: Command) -> None:
    match command:
        case Command(command="load", arguments=[filename]):
            print(f"Loading file: {filename}")
        case Command(command="save", arguments=[filename]):
            print(f"Saving file: {filename}")
        case Command(command="quit" | "exit" | "bye", arguments=["--force" | "-f", *rest]):
            print("Sending SIGTERM to all processes and quitting the program")
            print(rest)
            quit()
        case Command(command="quit" | "exit" | "bye"):
            print(f"Quitting the program")
            quit()


def main() -> None:
    """Main function"""

    while True:
        # command = input("$ ")
        command, *arguments = shlex.split(input("$ "))
        # run_command3(command)
        run_command4(Command(command, arguments))
        print(command, arguments)


if __name__ == "__main__":
    main()
