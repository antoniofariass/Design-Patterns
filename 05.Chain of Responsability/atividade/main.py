from validators import PointCount,LetterACount,CountSpace

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