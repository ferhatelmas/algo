class SignatureDecorator:
    def applyDecoration(self, name, commands, decorations):
        for c, d in zip(commands, decorations):
            if c == "surround":
                name = d + name + d[::-1]
            elif c == "prepend":
                name = d + name
            else:
                name += d
        return name
