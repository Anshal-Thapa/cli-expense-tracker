class AppError(Exception):
    pass

class InvalidExpenseDataError(AppError):
    '''This Error occurs when user inputs wrong type of data'''
    pass

class ExpenseNotFoundError(AppError):
    '''This error occurs when user selects id of Expence that doesnot exist'''
    pass

class FutureDateExpenseDateError(AppError):
    '''This error occurs when date is of a future date'''
    pass