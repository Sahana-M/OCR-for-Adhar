import re


#will help us to preprocess the text
def formatting_text(text):
    text = text.split('\n')
    list1 = []
    list1 = text
    list2 = []
    for word in list1:
        res1 = " ".join(re.findall("[a-zA-Z0-9/-]+", word))
        res1 = str(res1)
        if len(res1)>0:
            list2.append(res1.upper())
    return list2