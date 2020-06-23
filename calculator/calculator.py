import numpy as np
from functools import partial
import pkgutil

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock

Config.set("kivy", "window_icon", "logo.ico")


class CalcGridLayout(GridLayout):

    def __init__(self):
        GridLayout.__init__(self)
        self.content = False
        self.error_msg = False
        self.run_on_mult = False
        self.operators = ["*", "+", "-", "/", "(", ")", "^", "."]

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, new_bool):
        self._error_msg = new_bool

    @property
    def run_on_mult(self):
        return self._run_on_mult

    @run_on_mult.setter
    def run_on_mult(self, new_bool):
        self._run_on_mult = new_bool

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_bool):
        self._content = new_bool

    @property
    def operators(self):
        return self._operators

    @operators.setter
    def operators(self, new_operators):
        self._operators = new_operators

    def add_operand(self, operand):
        if self.content and self.display.text[-1] in self.operators:
            self.del_char()

        self.display.text += operand

    def add_euler(self):
        if self.content and self.display.text[-1] == "e":
            return

        else:
            char = "e"

            if self.content:
                self.run_on_mult = True

            self.add_char(char)
            self.run_on_mult = True

    def add_pi(self):
        if self.content and self.display.text[-1] == "\u03C0":
            return
        else:
            char = "\u03C0"

            if self.content:
                self.run_on_mult = True

            self.add_char(char)
            self.run_on_mult = True

    def add_open_bracket(self):
        if self.content:
            self.run_on_mult = True

        self.add_char("(")

    def add_char(self, char, *args):
        self.content = True

        if self.error_msg:
            self.display.text = char
            self.error_msg = False
            return

        if self.run_on_mult:
            if char not in self.operators and self.display.text[-1] not in self.operators:
                char = "*" + char

            self.run_on_mult = False

        self.display.text += char

    def calculate(self, term):
        if term:
            try:
                # change all exponents to the python syntax
                term = term.replace("^", "**")
                # replace the str placeholders for pi and e with the actual numbers
                term = term.replace("\u03C0", str(np.pi))
                term = term.replace("e", str(np.e))

                self.display.text = str(round(eval(term), 8))
                self.run_on_mult = True

            except ZeroDivisionError:
                self.display.text = "Can't divide by 0!"
                self.error_msg = True

            except SyntaxError:
                old_text = self.display.text
                self.display.text = "Please fix your syntax!"
                Clock.schedule_once(partial(self.clear_all), 1)
                Clock.schedule_once(partial(self.add_char, old_text), 1.01)

            except Exception:
                self.display.text = "Error"
                self.error_msg = True

    def calculate_inverse(self, term):
        if term:
            term = "1/(" + term + ")"
            self.calculate(term)

    def del_char(self):

        if self.error_msg:
            self.display.text = ""
            self.content = False
            self.error_msg = False

        else:
            self.display.text = self.display.text[:-1]

            if self.display.text == "":
                self.content = False
                self.run_on_mult = False

    def clear_all(self, *args):
        self.display.text = ""
        self.content = False
        self.error_msg = False
        self.run_on_mult = False

    def factorial(self, term):
        term = float(term)
        if term == 0:
            self.display.text = "1"

        elif term.is_integer():
            try:
                self.display.text = str(np.prod(np.arange(1, int(term) + 1)))

            except MemoryError:
                self.display.text = "Error: Overflow"
                self.error_msg = True

            except Exception:
                self.display.text = "Error"
                self.error_msg = True


class CalculatorApp(App):

    def build(self):
        self.icon = "logo.ico"
        return CalcGridLayout()


if __name__ == "__main__":
    calc_test = CalculatorApp()
    calc_test.run()

    for i in pkgutil.iter_modules():
        print('"' + i[1] + '",')
