class Bank:
    account = 1000
    limit_for_loan = 500
    limit_for_withdraw = 100

    def withdraw_money(self, amount):
        count = amount // self.limit_for_withdraw
        rest = amount % self.limit_for_withdraw
        for i in range(count):
            print(f'This is your money - {self.limit_for_withdraw}')
        print(f'This is your money - {rest}')

    def give_me_money(self, amount):
        if amount <= self.account:
            self.withdraw_money(amount)
        elif amount <= (self.account + self.limit_for_loan):
            print('Wait!')

        else:
            print('not enough money')

hana_bank = Bank()

sinhan_bank =  Bank()

hana_bank.give_me_money(400)