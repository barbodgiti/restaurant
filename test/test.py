from model.entity.user import User
from model.da.user_da import UserDa

ali = User(1,"barbod", "ghazaie", "barbari23", "bari8713tth", "09123223469")
dish = User(2,"diana",'ghazaie',"diana456","diana9013","0902")
print(dish)

user_da = UserDa()
user_da.save(ali)
