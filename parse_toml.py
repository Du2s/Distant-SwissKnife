import tomllib

class Config_data():
    def __init__(self) -> None:
            with open(".config.toml", "rb") as f:
                self.data = tomllib.load(f)
    def get_subjets(self):
        for subj in self.data:
            yield self.data[subj]

if __name__ == '__main__':
    data = Config_data()
    for i in data.get_subjets():
        print(f"{i['subject']}: {i['email']}")