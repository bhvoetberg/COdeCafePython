from pydantic import BaseModel, EmailStr, field_validator


# "pip install pydantic[email]" required to use EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"Account ID must be positive: {value}")
        return value


def main():
    user: User = User(
        name="Rober",
        email="some@there.com",
        account_id=28
    )
    user_data = {
        'name': 'Ben',
        'email': 'here@there.com',
        'account_id': '30'
    }

    user2: User = User(**user_data)
    print(user2)
    print(user2.model_dump_json())
    print(user2.model_dump())

    json_string = {"name":"Ben","email":"here@there.com","account_id":30}



if __name__ == '__main__':
    main()
