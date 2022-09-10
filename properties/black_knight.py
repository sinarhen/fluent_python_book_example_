class BlackKnight:

    def __init__(self):
        self.members = ["рука", "вторая рука",
                        "нога", "вторая нога"]
        self.phrases = ["Это всего лишь царапина",
                        "Это всего лишь поверхностная рана",
                        "Я неуязвим!",
                        "Ну ладно пусть будет ничья"]

    @property
    def member(self):
        print("Следующий член:")
        return self.members[0]

    @member.deleter
    def member(self):
        text = f"Черный рыцарь утрачена {self.members.pop(0)} \n" \
               f"{self.members.pop(0)}"