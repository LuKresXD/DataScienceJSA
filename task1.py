class AutoListDict(dict):
    def __getitem__(self, key):
        if key not in self:
            self[key] = []
        return super().__getitem__(key)


d = AutoListDict()
d['test'].append(1)
print(d['test'])
