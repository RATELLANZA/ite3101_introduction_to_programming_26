def censor(text:str,word:str)->str:
    result = []
    for s in text.split():
        if s == word:
            result.append("*" * len(word))
        else:
            result.append(s)
    return " ".join(result)