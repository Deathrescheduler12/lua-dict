class lua_dict:
    def __init__(self, **info):
        for x, y in info.items():
            if isinstance(y, str):
                exec(f"self.{x} = '{y}'")
            else:
                exec(f"self.{x} = func", {"func" : y, "self" : lua_dict})


