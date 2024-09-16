from model.entity.user import User
from model.da.user_da import UserDa

ali = User(1,"diana", "ghazaie", "diana23", "diana9013", "09023373936")
print(ali)

user_da = UserDa()
user_da.save(ali)
