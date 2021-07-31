#Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?


import json
def code_complex(z):
    if isinstance(z,complex):
        print(type(z))
        return ("real",z.real,"imag",z.imag)
    json.dumps (z,indent=3)
print(code_complex(12+3j))