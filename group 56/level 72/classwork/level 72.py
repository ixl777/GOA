def accum(st):
    result = []
    for i, char in enumerate(st):
        transformed_char = char.upper() + (char.lower() * i)
        result.append(transformed_char)
    return "-".join(result)