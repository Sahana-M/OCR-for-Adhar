import config as cfg
import re


#finding out the similarity in sentences
def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)



#converting list to string
def list_to_string(text, left_index, right_index):
    address =''
    while(left_index<=right_index):
        address = address + ' ' +  text[left_index]
        left_index = left_index+1
    return address


#finding out the address
def get_address(text):
    address = ''
    for index in range(len(text)):
        #either the address has "address"
        if(re.search("^ADDRESS", text[index])):
            index = index + 1
            last_index = len(text)-1
            while(last_index>=index):
                if(re.search("\d{6}", text[last_index])):
                    pincode = re.findall('\d{6}', text[last_index])
                    address = list_to_string(text, index, last_index)
                    return (address, pincode[0])
                    
                last_index = last_index-1
        
        #it can start from "TO" also
        if(re.search("^TO", text[index])):
            while(index<len(text)):
                if(re.search("D/O",text[index]) or re.search("S/O",text[index]) or re.search("W/O",text[index])):
                    last_index = len(text)-1
                    while(last_index>=index):
                        if(re.search("\d{6}", text[last_index])):
                            pincode = re.findall('\d{6}', text[last_index])
                            address = list_to_string(text, index, last_index)
                            return (address, pincode[0])
                            
                        last_index = last_index-1
                index = index + 1
        
        #it can start from "D/O", "S/O", "W/O"
        if(re.search("D/O",text[index]) or re.search("S/O",text[index]) or re.search("W/O",text[index])):
            last_index = len(text)-1
            while(last_index>=index):
                if(re.search("\d{6}", text[last_index])):
                        pincode = re.findall('\d{6}', text[last_index])
                        address = list_to_string(text, index, last_index)
                        return (address, pincode[0])
                            
                last_index = last_index-1
        index = index + 1

    return ('','')


#get fields from adhar back
def get_details_adhar_back(extracted_text):
    address, pincode = get_address(extracted_text)
    if(address == '' and pincode == ''):
        d = cfg.ERROR_MESSAGE
        return d
    d = {'fileIdentified' : "document_back.jpg", 'address':address, 'pincode': pincode}
    return d


#check whether the document is adhar back or not
def check_adhar_back(processed_img_text, raw_image_text):
    for sentence in processed_img_text:
        if((jaccard_similarity(sentence, cfg.ADHAR_BACK_IDENTIFIER)) >= 0.7):
            return True
    for sentence in raw_image_text:
        if((jaccard_similarity(sentence, cfg.ADHAR_BACK_IDENTIFIER)) >= 0.7):
            return True
    return False

