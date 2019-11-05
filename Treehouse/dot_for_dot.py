class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for itm in self.pattern:
            if itm == '.':
                morse.append("dot")
            elif itm == '_':
                morse.append("underscore")
        return '-'.join(morse)     

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

l = Letter(['.', '.', '.'])
print(l.__str__())