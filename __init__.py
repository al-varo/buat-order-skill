from mycroft import MycroftSkill, intent_file_handler


class BuatOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.buat.intent')
    def handle_order_buat(self, message):
        self.speak_dialog('order.buat')


def create_skill():
    return BuatOrder()

