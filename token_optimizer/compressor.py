def compress(text):

    words=text.split()

    if len(words)>40:
        return " ".join(words[:40])

    return text
