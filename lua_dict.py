class lua_dict:
    def __init__(self, **info):
        self.info = info
        self.change()
    def __setitem__(self, name, value):
        self.info[name] = value
        self.change()
    def __getitem__(self, name):
        return self.info[name]
    def change(self):
         for x, y in self.info.items():
            if isinstance(y, str):
                exec(f"self.{x} = '{y}'")
            else:
                exec(f"self.{x} = func", {"func" : y, "self" : lua_dict})


