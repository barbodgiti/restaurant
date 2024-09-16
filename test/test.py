from model.entity.user import User
from model.da.user_da import UserDa

ali = User(1,"barbod", "ghazaie", "barbari23", "bari8713", "09123223469")
print(ali)

user_da = UserDa()
user_da.save(ali)
