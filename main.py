import irregular_verbs
import verb_endings
import string

japanese_punction = "、。〜"
unnecessary_endings = "か"

def match_string_end(word, string_end):
    strlen = len(string_end)
    if(word[-strlen:] == string_end):
        return True
    else:
        return False

def check_multiple_endings(word,endings):
    for e in endings:
        if match_string_end(word,e):
            return True

    return False

def is_casual(sen):
    for word in irregular_verbs.CASUAL:
        if match_string_end(sen,word):
            return True
    for word in verb_endings.CASUAL:
        if match_string_end(sen,word):
            return True            

    return False

def is_polite(sen):
    #check irregular verbs
    for word in irregular_verbs.POLITE:
        if word in sen:
            return True
    for word in verb_endings.POLITE:
        if match_string_end(sen,word):
            return True    


    # #check regular verbs
    # if (word[-2:] == "ます" or "です"):
    #     return True
    
    return False

def is_honorific(sen):
    for word in irregular_verbs.HONORIFIC:
        if word in sen:
            return True
    for word in verb_endings.HONORIFIC:
        if match_string_end(sen,word):
            return True    

    """     #check regular verbs
    if (word[-5:] == "になります"):
        return True """

    return False

def is_humble(sen):
    for word in irregular_verbs.HUMBLE:
        if word in sen:
            return True
    for word in verb_endings.HUMBLE:
        if match_string_end(sen,word):
            return True    

    return False

def determine_politeness(sentence):
    if is_honorific(sentence):
        return "honorific / "
    elif is_humble(sentence):
        return "humble / "
    elif is_polite(sentence):
        return "polite / "
    elif is_casual(sentence):
        return "casual / "
    else:
        return "cannot determine"

def convert_past_tense(sen):
    sen = sen.replace("ました", "ます")
    sen = sen.replace("でした", "です")
    return sen

def process_input():
    sen = input("Please enter sentence in Japanese:")
    sen = sen.translate(str.maketrans('', '', string.punctuation + japanese_punction))
    if (sen[-1:] in unnecessary_endings):
        sen = sen[:-1]

    sen = convert_past_tense(sen)
    return sen

def get_output(sentence):
    style = determine_politeness(sentence)
    return style

def main():
    while True:
        sentence = process_input()
        output = get_output(sentence)
        print(output)

main()