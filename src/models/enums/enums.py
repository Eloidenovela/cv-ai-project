import enum

class RoleEnum(enum.Enum):
    user = "user"
    admin = "admin"

    def get_value(self):
        return self.value