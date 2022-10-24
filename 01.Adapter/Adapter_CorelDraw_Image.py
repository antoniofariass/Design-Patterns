from ImagemTarget import ImagemTarget
from CorelDraw_Image import CorelDraw_Image

class Adapter_CorelDraw_Image(CorelDraw_Image,ImagemTarget):

    def carregarImagem(nomeDoArquivo):
        CorelDraw_Image.CorelDraw_CarregarImagem(nomeDoArquivo)

    def desenharImagem(posX, posY, largura, altura):
        CorelDraw_Image.CorelDraw_DesenharImagem(posX,posY)