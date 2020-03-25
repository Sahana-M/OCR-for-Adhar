import re
import config as cfg
import datetime


#finding out the similarity in sentences
def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    #print("similarity : ", len(intersection)/len(union))
    return len(intersection)/len(union)



#finding aadhar number
def find_adhar_number(text):
    for sentence in text:
        if(re.search(cfg.ADHAR_ID, sentence)):
            sentence = sentence.replace(" ", "")
            sentence = ''.join(d for d in re.findall('\d+', sentence))
            return sentence
        elif(re.search("\d{4}\s\d{8}", sentence)):
            sentence = sentence.replace(" ", "")
            sentence = ''.join(d for d in re.findall('\d+', sentence))
            return sentence
        elif(re.search("\d{8}\s\d{4}", sentence)):
            sentence = sentence.replace(" ", "")
            sentence = ''.join(d for d in re.findall('\d+', sentence))
            return sentence
    return ''


#getting the adhar number from te best of texts obtained from the same image
def get_adhar_number(processed_img_text,raw_image_text):
    sentence = find_adhar_number(processed_img_text)
    if(sentence == ''):
        sentence = find_adhar_number(raw_image_text)
        return sentence
    return sentence


#finding father name
def find_father_name(extracted_text):
    for l in range(len(extracted_text)):
        if(re.search(cfg.FATHER_NAME, extracted_text[l])):     #finding father name from raw text because it had extracted better in most cases
            if(len(extracted_text[l]) > 6):
                father_name = (extracted_text[l])[7:]
                return father_name
            else:
                father_name = extracted_text[l+1]
                return father_name
    return ''


#finding husband name
def find_husband_name(extracted_text):
    for l in range(len(extracted_text)):
        if(re.search(cfg.HUSBAND_NAME, extracted_text[l])):    #finding husband name from raw text as it had better extracted it
            if(len(extracted_text[l]) > 7):
                father_name = (extracted_text[l])[8:]
                return father_name
            else:
                father_name = extracted_text[l+1]
                return father_name
    return ''


#getting name from aadhar card
def find_adhar_name(processed_img_text, raw_image_text):
    
    #Name can be the 2nd string after GOVERNMENT OF INDIA in raw img text(GOI 
    for index in range(len(raw_image_text)):
        if((jaccard_similarity(raw_image_text[index], cfg.ADHAR_FRONT_IDENTIFIER) >= 0.7)
            and (index+2)<len(raw_image_text)):
            name = raw_image_text[index+1]
            return name

    #Name can be the 2nd string after GOVERNMENT OF INDIA in preprocessed img text
    for index in range(len(processed_img_text)):
        if((jaccard_similarity(processed_img_text[index], cfg.ADHAR_FRONT_IDENTIFIER) >= 0.7)
            and (index+2)<len(processed_img_text)):
            name = processed_img_text[index+2]
            return name

    #Name can be 1 string before DOB in raw text
    for index in range(len(raw_image_text)):
        if((re.search(cfg.DOB, raw_image_text[index])
            or re.search(cfg.YOB, raw_image_text[index])
            or re.search(cfg.DOB_SLASH, raw_image_text[index])
            or re.search(cfg.DOB_HIFEN, raw_image_text[index]))
            and (index-1)>=0):
            name = raw_image_text[index-1]
            return name

    #Name can be 1 string before DOB in preprocessed text
    for index in range(len(processed_img_text)):
        if((re.search(cfg.DOB, processed_img_text[index])
            or re.search(cfg.YOB, processed_img_text[index])
            or re.search(cfg.DOB_SLASH, processed_img_text[index])
            or re.search(cfg.DOB_HIFEN, processed_img_text[index]))
            and (index-1)>=0):
            name = processed_img_text[index-1]
            return name
            
    
    return ''


#finding the DOB or year of birth
def find_dob(text):
    for index in range(len(text)):                  
        #Some people have Year of Birth (YOB) in their aadhar card
        if(re.search(cfg.YOB, text[index])):
            yob = re.findall('[1-2][0-9][0-9][0-9]', text[index]) 
            yob = yob[0]   
            if(yob != []):
                now = datetime.datetime.now()
                age = now.year - int(yob)
                return (yob, age)

        #Some people have Date of Birth (DOB) in their aadhar card, in the form DD/MM/YYYY or DD-MM-YYYY
        if(re.search(cfg.DOB, text[index])          
            or re.search(cfg.DOB_SLASH, text[index])
            or re.search(cfg.DOB_HIFEN, text[index])):
            dob = re.findall(cfg.DOB_SLASH, text[index])

            if len(dob) == 0: 
                dob = re.findall(cfg.DOB_HIFEN, text[index])

            if(dob != []):
                dob = dob[0]
                yob = dob[6:]
                now = datetime.datetime.now()
                age = now.year - int(yob)
                return(dob,age)

    return '',''


#finding gender
def find_gender(text):
    for sentence in text:
        if(re.search("FEMALE", sentence)):
            return "FEMALE"
        elif(re.search("MALE", sentence)):
            return "MALE"
        else:
            pass
    return ''



#getting fields from aadhar front
def get_details_adhar_front(processed_img_text, raw_image_text):
    adhar_number = get_adhar_number(processed_img_text, raw_image_text)

    adhar_name = find_adhar_name(processed_img_text, raw_image_text)

    father_name = find_father_name(raw_image_text)
    if father_name == '': father_name = find_father_name(processed_img_text)

    husband_name = find_husband_name(raw_image_text)
    if husband_name == '': husband_name = find_husband_name(processed_img_text)

    gender = find_gender(processed_img_text)
    if gender == '': find_gender(raw_image_text)
    
    dob, age = find_dob(raw_image_text)
    if(dob == '' and age == ''):
        dob, age = find_dob(processed_img_text)

    d = {'fileIdentified' : "document_front.jpg", 'idNumber': adhar_number, 'name': adhar_name,
        'father' : father_name, 'husband' : husband_name, 'dob': dob, 'age' : age, 'gender' : gender}
    return d


#checking if the document is adhar front by the presence of adhar number
def check_adhar_front(processed_img_text, raw_image_text):
    if(find_adhar_number(processed_img_text) != ''):
        return True
    elif(find_adhar_number(raw_image_text) != ''):
        return True
    return False