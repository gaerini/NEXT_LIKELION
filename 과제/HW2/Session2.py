class Bank:
    def __init__(self, total_amount, limit_for_loan, limit_for_withdrawal):
        self.total_amount = total_amount
        self.limit_for_loan = limit_for_loan
        self.limit_for_withdrawal = limit_for_withdrawal
        
    def repeat_withdrawing_money(self, amount):
        count = amount // self.limit_for_withdrawal
        rest = amount % self.limit_for_withdrawal

        for i in range(count):
            print(f'This is your money - {self.limit_for_withdrawal}')

            if i == (count - 1):
                print(f'This is your money - {rest}')

    
    def show_me_the_money(self, amount):

        if amount <= self.total_amount:
            self.repeat_withdrawing_money(amount)

        elif amount <= (self.total_amount + self.limit_for_loan):
            print('Wait!')

        else:
            print('your money is not enough')


hana_bank = Bank(1000, 200, 100)
hana_bank.show_me_the_money(450)

sinhan_bank = Bank(500, 50, 50)
sinhan_bank.show_me_the_money(250)
