from mycroft import MycroftSkill, intent_file_handler


class Tuxi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tuxi.intent')
    def handle_tuxi(self, message):
        self.speak_dialog('tuxi')


def create_skill():
    return Tuxi()

