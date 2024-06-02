from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


def do_something(user: User) -> None:
    user.age += 1
    print(user)


def main() -> None:
    user = User("John", 30)
    print(user)

    do_something(user)


if __name__ == "__main__":
    main()
