class ProgrammingLanguage:
    def __init__(self,Language, Typing, Reflection, Year):
        self.Language = Language
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def is_dynamic(self):
        return self.Typing == self.Typing

    def __str__(self):
        return f'{self.Language}, {self.Typing} Typing, Reflection = {self.Reflection}, First appeared in  {self.Year}'


