from validators import CarneValidator,NosValidator,BananaValidator

class Validator:
    
    def __init__(self) -> None:
        self.validators = [
            BananaValidator(),
            NosValidator(),
            CarneValidator()
        ]
    
    def process(self,comida: str):
        for v in self.validators:
            if v.validate(comida): return v.action()
    
Validator = Validator()
Validator.process('banana')