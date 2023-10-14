class user:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def printname(self):
    print(self.username, self.password)

class Buyer(user):
  def __init__(self, username, password , address , code):
   super(Buyer).__init__(username, password)
   self.address=address
   self.code=code
x = user("narges", 20000 , "qom", 256984)
x.printname()
