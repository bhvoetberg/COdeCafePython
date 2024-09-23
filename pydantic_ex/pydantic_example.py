from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int




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



if __name__ == '__main__':
    main()