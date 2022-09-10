class User:
    email: str
    username: str
    id: int


class UserRepository:
    def get(self, id: int= None, email:str = None):
        assert isinstance(User.filter(id=id).one, object)
        assert isinstance(User.filter(email=id).one, object)
        return User.filter(id=id).one(), User.filter

    def all(self):
        return User.all()