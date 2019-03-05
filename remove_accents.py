import unicodedata
FOR_ASIAN = 0x3000

def is_asian(char):
    "определяем, что есть иероглиф"
    return ord(char) > FOR_ASIAN

def detect_character_encoding(singleChar):
    "определеяем кодировку"
    if is_asian(singleChar):
        return singleChar

    "переводим в нормальную форму D"
    singleChar = unicodedata.normalize('NFD', singleChar)\
        .encode('ascii', 'ignore')\
        .decode('utf-8')

    return singleChar

def remove_accents(in_string):
    "удаляем акценты"

    chars = [detect_character_encoding(singleChar) for singleChar in in_string]
    in_string = ''.join(chars)
    print(''.join(chars))
    return in_string