class InvalidExpenseDataError(Exception):
    '''This Error occurs when user inputs wrong type of data'''
    pass

class ExpenseNotFoundError(Exception):
    '''This error occurs when user selects id of Expence that doesnot exist'''
    pass

class FutureDateExpenseDateError(Exception):
    '''This error occurs when date is of a future date'''
    pass