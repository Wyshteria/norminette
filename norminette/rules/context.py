from rules.norm_error import NormError

class Context:
    def __init__(self, filename, tokens):
        self.filename = filename
        self.filetype = filename.split('.')[-1]
        self.tokens = tokens
        self.errors = []
        self.scope = "global"
        self.indent_lvl = 0
        self.lines = 1
        self.functions = 0

    def peekToken(self, pos):
        if pos >= len(self.tokens):
            return None
        return self.tokens[pos]

    def popTokens(self, stop):
        for i in range(stop):
            if self.peekToken(i) is not None \
                    and self.peekToken(i).type == "NEWLINE":
                self.lines += 1
                if self.peekToken(i + 1) is not None \
                        and self.peekToken(i + 1).type == "NEWLINE":
                    # Append "consecutive newlines" error
                    self.pushError(9999, self.peekToken(i))
        self.tokens = self.tokens[stop:]

    def pushError(self, errno, tkn):
        self.errors.append(NormError(errno, tkn.pos[0], tkn.pos[1]))