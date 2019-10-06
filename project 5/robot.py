class Robot:
    def __init__(self, name, src, dst):
        self.name = name
        self.dst = dst
        self.path = [src, ]
