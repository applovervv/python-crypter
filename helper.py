import base64

asciiChars = "+/0123456789=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
emojiStart = 127800

def ko(text):#encode
    encoded = ""
    for char in text:
        if not asciiChars.find(char) == -1:
            encoded = encoded + chr(emojiStart + asciiChars.find(char))
    return encoded

def pa(text):#decode
    decoded = ""
    for char in text:
        decimal = ord(char)
        decoded = decoded + asciiChars[decimal - emojiStart]
    return decoded


def loc(s):#base64encode
    sample_string_bytes = s.encode("ascii", 'ignore')
    base64_bytes = base64.b64encode(sample_string_bytes)
    encoded = base64_bytes.decode("ascii")
    return encoded

def j(s):#base64decode
    base64_bytes = s.encode("ascii", 'ignore')
    sample_string_bytes = base64.b64decode(base64_bytes)
    decoded = sample_string_bytes.decode("ascii")
    return decoded

