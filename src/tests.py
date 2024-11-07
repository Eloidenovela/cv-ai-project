# from models.models import get_storage

# get_storage()

from services.user import UserService
from models.models import engine

user_service = UserService(engine)

print(user_service.get_all())

# print(user_service.create({
#     "username": "eloide-novela",
#     "password": "10134456",
#     "role": "admin"
# }))