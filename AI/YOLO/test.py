from collections import OrderedDict

data = {
    "as":12222,
    "b":12,
    "aa":1212
}
sorted_values = [value for key, value in sorted(data.items())]
print(sorted_values)