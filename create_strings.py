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

if __name__ == '__main__':
    print(email_list())
    print(subject_dict())