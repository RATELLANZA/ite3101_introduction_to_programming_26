def reverse(text:str)->str:
    word = ""
    length = len(text) - 1
    while length >=0:
        word = word + text[length]
        length -=1