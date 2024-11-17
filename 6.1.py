class UserAccount:
    
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.__password = password

  def set_password(self, new_password):
    self.__password = new_password

  def check_password(self, check_password):
    if(check_password == self.__password):
      return True
    else:
      return False

# создаём аккаунт 
name = str(input("username: "))
mail = str(input("email: "))
psswrd = str(input("password: "))
Account = UserAccount(name, mail, psswrd)
# проверяем пароль
check1 = str(input("check_password: "))
print(Account.check_password(check1))


# новый пароль
nw_psswrd = str(input("new_password: "))
Account.set_password(nw_psswrd)
# проверяем новый пароль
check2 = str(input("check_password: "))
print(Account.check_password(check2))
