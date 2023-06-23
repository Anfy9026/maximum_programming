def check_string(string):
    string = string.lower()
    string = string.replace(' ', '')
    if len(string) % 2 == 0:
        string_length = int(len(string) / 2)
        if string[:string_length] == string[string_length:][::-1]:
            return True
        else:
            return False
    else:
        return False

print(check_string('Лепс спел'))
