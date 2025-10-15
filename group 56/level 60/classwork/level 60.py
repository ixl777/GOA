def capitalize_word(word: str) -> str:
    if not word:  
        return ''
    return word[0].upper() + word[1:]