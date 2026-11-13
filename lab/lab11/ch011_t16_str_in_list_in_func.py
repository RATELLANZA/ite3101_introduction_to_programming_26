from typing import List


n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words: List[str])-> str:
    result = ""
    for word in words:
        result = result + word
    return result

print(join_strings(n))
