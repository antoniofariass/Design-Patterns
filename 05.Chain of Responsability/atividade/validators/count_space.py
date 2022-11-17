from .interface import ValidatorInterface


class CountSpace(ValidatorInterface):
    
    def action(self,text) -> None:
        count = 0
        
        for i in range(0, len(text)):
            
            if text[i] == " ":
                count += 1
            
        print(f'The string have {count} spaces.')
 