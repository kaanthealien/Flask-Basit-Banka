
class User():
  def __init__(self, name):
    self.name = name

  def show_details(self):
    x = 'Kişi Detayı'
    y = 'Isim: ' + self.name
    z = 'Hesabındaki tutar' +str(self.balance)
    result = [x,y,z]
    return result



class Bank(User):
  def __init__(self, name):
    super().__init__(name)
    self.balance = 0

  def deposit(self, amount):
    self.amount = int(amount)
    self.balance = self.balance +self.amount
    return 'Hesabındaki tutar' +str(self.balance)

  def withdraw(self, amount):
    self.amount = int(amount)
    if self.amount>self.balance:
      return "Yetersiz bakiye" +str(self.balance)
    else:
      self.balance = self.balance-self.amount
      return 'Hesabındaki tutar' +str(self.amount)
    
  def view_money(self):
    return str(self.balance)

