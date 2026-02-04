def camelCase(s):
    result = ""
    for i, char in enumerate(s):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result