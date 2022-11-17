from abc import ABC,abstractmethod

class ValidatorInterface(ABC):

    @abstractmethod
    def action(self) -> None:
        pass
