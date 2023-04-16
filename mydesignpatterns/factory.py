"""
工厂模式模拟
"""


class Button(object):
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory():
    def create_button(self, typ):
        print(typ)
        targetclass = typ.capitalize()
        print(targetclass)
        return globals()[targetclass]()


button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print(button_obj.create_button(b).get_html())
