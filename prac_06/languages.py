"""
Estimate: 60 minutes
Actual: 40 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():


   python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
   ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
   visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
   print(python)

   languages = [python, ruby, visual_basic]

   print("The dynamically typed languages are:")
   for languages in languages:
       if languages.is_dynamic():
           print( languages.Language)
main()
