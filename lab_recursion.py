#lab recursion

def characters(text:str):
    if text == "":
        return 0
    
    char = "aeiou"

    if text[0].lower() in char:
        return 1 + characters(text[1:])
    else:
        return characters(text[1:])

print(characters("I love python"))