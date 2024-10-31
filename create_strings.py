from parse_toml import Config_data

data = Config_data()

def email_list():
    res = ''
    for subj in data.get_subjets():
        if subj['email'] != '-':
            res += f"*{subj['subject']}*\n{subj['lehrer']}: `{subj['email']}`\n"
    return res

def subject_dict():
    res = dict()
    for subj in data.get_subjects_list():
        res[data.get_subject(subj)['subject']] = {'callback_data': subj}
    return res

def subject_list():
    res = list()
    for subj in data.get_subjects_list():
        res.append(subj)
    return res

def subject_info(subj):
    res = ''
    try:
        subject = data.get_subject(subj)
        res += f"*Subject:* {subject['subject']}\n" \
               f"*Teacher:* {subject['lehrer']}\n" \
               f"*Email:* {subject['email']}\n" \
               f"*Task:* {subject['task']}\n" \
               f"*Deadline:* {subject['deadline']}\n" \
               f"*Useful links:*\n"
        for link in subject['links']:
            res += f"[{link}]({subject['links'][link]})\n"
    except IndexError:
        print("Wrong config")
    res = res.replace('.', r'\.').replace('-', r'\-')
    return res

if __name__ == '__main__':
    print(email_list())
    print(subject_dict())
