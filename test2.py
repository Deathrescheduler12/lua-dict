from lua_dict import lua_dict
x = lua_dict(hello = "hi", who = lua_dict(asked = lua_dict(me = "not me", not_me = lua_dict(ans = "me"))))
print(x.who.asked.not_me.ans)

