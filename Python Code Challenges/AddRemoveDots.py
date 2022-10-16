def add_dots(word_WithoutD):
    return ".".join(word_WithoutD)

def remove_dots(word_withD):
    return word_withD.replace(".","")

print(remove_dots(add_dots("test")))