def censor(text:str,word:str)->str:
    result = []
    for s in text.split():
        if s == word:
            result.append()
        else:
            result.append(s)