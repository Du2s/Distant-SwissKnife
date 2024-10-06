from parse_toml import Config_data

data = Config_data()

def email_list():
    res = ''
    for subj in data.get_subjets():
        if subj['email'] != '-':
            res += f"*{subj['subject']}*\n{subj['lehrer']}: `{subj['email']}`\n"
    return res

if __name__ == '__main__':
    print(email_list())