from abc import ABC,abstractmethod

class ValidatorInterface(ABC):

    @abstractmethod
    def action(self) -> None:
        pass

class CountSpace(ValidatorInterface):
    
    def action(self,text) -> None:
        count = 0
        
        for i in range(0, len(text)):
            
            if text[i] == " ":
                count += 1
            
        print(f'The string have {count} spaces.')


class LetterACount(ValidatorInterface):
    
    def action(self,text) -> None:
        count = 0
        
        for i in range(0, len(text)):
            
            if text[i] == "a":
                count += 1
            
        print(f'The string have {count} letter A.')


class PointCount(ValidatorInterface):
    
    def action(self,text) -> None:
        count = 0
        
        for i in range(0, len(text)):
            
            if text[i] == ".":
                count += 1
            
        print(f'The string have {count} points.')


class Validator():
    def __init__(self) -> None:
        self.validators = [
            PointCount(),
            LetterACount(),
            CountSpace()
        ]
    
    def process(self,text: str):
        for v in self.validators:
            v.action(text)

Validator = Validator()
Validator.process('Estou testando se esta tudo funcionando.')