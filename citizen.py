class Citizen:
    '''It returns full name of citizens'''
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        self.full_name = self.first_name+' '+self.last_name    
        return self.full_name
    greeting = 'For the glory of Python!'    