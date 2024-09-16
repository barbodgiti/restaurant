from model.entity.user import User
from model.da.user_da import user_da

ali = User("kjhsk", "ikadshvk", "bafgsdgds", "qwe1234", "burger", "coke", "jackti", "true")
print(ali)

oogh = user_da()

oogh.save(ali)
