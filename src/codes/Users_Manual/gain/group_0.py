~from pyautd3 import Focus, Group, Null
~x = 1.0
~y = 0.0
~z = 0.0
g = (
    Group(lambda _, tr: "null" if tr.idx <= 100 else "focus")
    .set("null", Null())
    .set("focus", Focus([x, y, z]))
)