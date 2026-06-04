class Parser:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def peek(self):
        return self.text[self.pos] if self.pos < len(self.text) else ""

    def expr(self):
        value = self.term()
        while self.peek() == "+":
            self.pos += 1
            value += self.term()
        return value

    def term(self):
        value = self.factor()
        while self.peek() == "*":
            self.pos += 1
            value *= self.factor()
        return value

    def factor(self):
        start = self.pos
        while self.peek().isdigit():
            self.pos += 1
        return int(self.text[start:self.pos])


print(Parser("2+3*4").expr())
