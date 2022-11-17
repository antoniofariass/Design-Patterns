from .interface import ValidatorInterface

class LetterACount(ValidatorInterface):
    
    def action(self,text) -> None:
        count = 0
        
        for i in range(0, len(text)):
            
            if text[i] == "a":
                count += 1
            
        print(f'The string have {count} letter A.')
 