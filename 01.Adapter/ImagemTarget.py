from abc import ABC, abstractmethod
from Adapter_CorelDraw_Image import Adapter_CorelDraw_Image

class ImagemTarget(ABC):

    @abstractmethod
    def carregarImagem(nomeDoArquivo):
        return
    
    @abstractmethod
    def desenharImagem(posX,posY,largura,altura):
        return