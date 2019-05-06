class WordAnalyse:
    key_word = ['void', 'int', 'float', 'double', 'if', 'else', 'for', 'do', 'while', 'break', 'continue', 'goto']
    one_symbol = ['+', '-', '*', ';', ',', '(', ')', '{', '}', '!', '%', '=', '<', '>', '[', ']', '/', '\\', '"', '\'']
    two_symbol = ['++', '--', '>>', '<<', '+=', '-=', '*=', '/=', '&&', '||', '>=', '<=', '<>', '!=', '==', '/*', '*/', '%=']

    def __init__(self, filename):
        # IO stream
        self.strlen = 0
        self.str_end = False
        self.IO_preprosess(filename)

        self.char = ''
        self.p = 0
        self.token = []
        self.case = ''
        self.current_case = None
        self.result = []

        # begin analyse
        while self.next_char():
            if self.english_word():
                if self.case != '注释*':
                    self.case = 'Alpha'
                self.out(self.case)
                continue
            elif self.number():
                if self.case != '注释*':
                    self.case = 'Digit'
                self.out(self.case)
                continue
            elif self.symbol():
                self.out(self.case)
            elif self.is_none():
                continue

    def IO_preprosess(self, filename):
        try:
            self.inputIO = open(filename, 'r', encoding='utf-8').read()
            self.inputIO = self.inputIO.replace('\t', "")
            self.strlen = len(self.inputIO)
            # self.inputIO = self.inputIO.replace('\n', "")
        except:
            print("Cannot read file!")

    def is_none(self):
        if self.char == ' ' or self.char == '\n':
            return True

    def english_word(self):
        if self.char.isalpha():
            while self.char.isalnum():
                self.token.append(self.char)
                self.next_char()
            self.retract()
            return True
        return False

    def number(self):
        if self.char.isdigit():
            while self.char.isdigit():
                self.token.append(self.char)
                self.next_char()
            self.retract()
            return True
        return False

    def symbol(self):
        first = self.char
        self.next_char()
        second = self.char
        if first + second in self.two_symbol:
            self.token.append(first + second)
            if first + second == '*/' or first + second == '/*':
                if self.case != '注释*':
                    self.case = '注释*'
                else:
                    self.case = '*注释'
            else:
                self.case = 'Two_Symbol'
            return True
        elif first in self.one_symbol:
            self.token.append(first)
            self.retract()
            self.case = 'One_Symbol'
            return True
        else:
            self.retract()
            return False

    def out(self, case):
        prestr = ""
        for i in self.token:
            prestr += i
        self.token = []
        if case == 'Alpha':
            if prestr in self.key_word:
                case = 'KeyWord'
        self.result.append([case, prestr])
        # print("<"+case + ", " + prestr + ">", end=' ')

    def retract(self):
        self.str_end = False
        self.p -= 1

    def next_char(self):
        if self.strlen == self.p:
            return False
        try:
            self.char = self.inputIO[self.p]
            self.p += 1
            if self.strlen == self.p:
                return False
            return True
        except:
            return False

