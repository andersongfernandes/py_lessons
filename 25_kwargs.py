# timecode 2:16:59
# kwargs

def hello(**kargs):
    aux = ""
    for key,value in kargs.items():
        aux = aux + value+ " "
    return aux

final_response = hello(title="Dr", first="Anna")
print(final_response)

final_response = hello(title="Dr", first="Anna", last_name="Fernandes")
print(final_response)