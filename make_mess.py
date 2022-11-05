from tkinter import *
from tkinter.ttk import *

FILL = dict(expand=True, fill=BOTH)
FILLX = dict(expand=True, fill=X)
FILLY = dict(expand=True, fill=Y)
GAP = dict(padx=5, pady=5)


def make_mess(s, reverse=False):
    """
    ‥  … …  ▪ ■ □ ◇ ○ ━ ▒ ▓ ░ ▥ ▨ ⋌ ∷
    """
    try:
        if reverse:
            s1 = s.encode('gbk')
            s2 = s1.decode('utf-8')
            msg = s2
        else:
            s1 = s.encode('utf-8')
            s2 = s1.decode('gbk')
            msg = s2
    except Exception as e:
        msg = str(e)
        pos = msg[msg.find('position') + 9:msg.rfind(':')]
        msg = f'第 {pos} 个字符编码错误：{s[int(pos) // 3]}'
    return msg


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.title('GBK from UTF-8 messy code')
        self.font = ('微软雅黑', 12)

        self.input_text = StringVar()
        self.output_text = StringVar()

        self.input_text_test = StringVar()
        self.output_text_test = StringVar()

    def init_style(self):
        style = Style()
        style.configure('.', font=self.font)

    def init_ui(self):
        # create messy code
        f1 = Frame(self.root)
        f1.pack(**GAP)
        Label(f1, text="Make messy code when decode utf-8 in gbk").pack()
        self.input_e = Entry(f1,
                             width=60,
                             font=self.font,
                             textvariable=self.input_text)
        self.input_e.pack(**GAP)
        self.input_e.focus_set()
        self.input_e.bind('<KeyRelease>', self.on_input)
        # insert special characters
        f11 = Frame(f1)
        f11.pack()
        codes = ['…', '□', '◇', '○', '⋌', '∷']
        # pack all special buttons
        for idx in range(len(codes)):
            b = Button(f11,
                       width=2,
                       text=codes[idx],
                       command=lambda idx=idx: self.handle_btn(codes[idx]))
            b.pack(side=LEFT, **GAP)
        Entry(f1,
              width=60,
              font=self.font,
              textvariable=self.output_text).pack(**GAP)

        # decode messy code
        f2 = Frame(self.root)
        f2.pack(**GAP)
        Label(f2, text="Reverse test").pack()
        input_test = Entry(f2,
                           width=60,
                           font=self.font,
                           textvariable=self.input_text_test)
        input_test.pack(**GAP)
        input_test.bind('<KeyRelease>', self.on_input_test)
        Entry(f2, width=60, font=self.font,
              textvariable=self.output_text_test).pack(**GAP)
        return self

    def handle_btn(self, char):
        self.input_e.insert(INSERT, char)
        self.on_input()

    def on_input(self, *a, **b):
        text = self.input_text.get()
        self.output_text.set(make_mess(text))

    def on_input_test(self, *a, **b):
        text = self.input_text_test.get()
        self.output_text_test.set(make_mess(text, True))

    def run(self):
        self.init_style()
        self.init_ui()
        self.root.mainloop()


if __name__ == '__main__':
    Gui().run()
