from mycroft import MycroftSkill, intent_file_handler


class MkAutomation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('automation.mk.intent')
    def handle_automation_mk(self, message):
        self.speak_dialog('automation.mk')


def create_skill():
    return MkAutomation()

