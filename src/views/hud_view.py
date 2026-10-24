import pygame

from src.config import COR_TEXTO, LARGURA, MAX_ITENS_PERDIDOS


class HudView:
    def __init__(self, tela, recursos):
        self.tela = tela
        self.recursos = recursos
        self.fonte_pontos = pygame.font.Font('fontes/Stardew_Valley.ttf', 46)

    def desenhar(self, model):
        faixa_placar = pygame.Rect(LARGURA // 2 - 46, 10, 92, 52)
        pygame.draw.rect(self.tela, (10, 14, 22), faixa_placar, border_radius=9)
        pygame.draw.rect(self.tela, (205, 215, 225), faixa_placar, width=1, border_radius=9)
        pontos = self.fonte_pontos.render(str(model.pontuacao), True, COR_TEXTO)
        self.tela.blit(pontos, pontos.get_rect(center=faixa_placar.center))

        vidas = MAX_ITENS_PERDIDOS - model.itens_perdidos
        tamanho, espaco, margem = 44, 8, 16
        inicio = LARGURA - margem - MAX_ITENS_PERDIDOS * (tamanho + espaco) + espaco
        for indice in range(MAX_ITENS_PERDIDOS):
            imagem = 'imagens/coracaoV.png' if indice < vidas else 'imagens/coracaoP.png'
            retangulo = pygame.Rect(inicio + indice * (tamanho + espaco), 12, tamanho, tamanho)
            self.recursos.desenhar(self.tela, imagem, retangulo)
