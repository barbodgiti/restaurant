from model.entity.user import User
from model.da.user_da import UserDa

ali = User(1,"kjkhjkahsk", "ikadshvk", "bafgsdgds", "qwe1234", "0917")
print(ali)

user_da = UserDa()
user_da.save(ali)
