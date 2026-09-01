class InvalidExpenceDataError(Exception):
    '''This Error occurs when user inputs wrong type of data'''
    pass

class ExpenceNotFoundError(Exception):
    '''This error occurs when user selects id of Expence that doesnot exist'''
    pass