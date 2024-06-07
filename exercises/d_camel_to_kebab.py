def camel_to_kebab(text):
    result = ''
    for char in text:
        if char.isupper():
            result += '-' + char.lower()
        else:
            result += char
    return result