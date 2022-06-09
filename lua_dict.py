class lua_dict:
    def __init__(self, **info):
        self.parent = []
        for x in info.items():
            if isinstance(x[1], str):
                exec(f"self.{x[0]} = '{x[1]}'")
            else:
                exec(f"self.{x[0]} = func", {"func" : x[1], "self" : lua_dict})


