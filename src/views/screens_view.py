import pygame

from src import config
from src.config import CHAO_Y, COR_TEXTO, COR_TEXTO_SUAVE, LARGURA
from src.models.lixeiras import LIXEIRAS

COR_TEXTO_MURAL = (43, 24, 12)


class ScreensView:
    def __init__(self, tela, recursos):
        self.tela = tela
        self.recursos = recursos
        self.fonte_game_over = pygame.font.Font('fontes/Stardew_Valley.ttf', config.TAMANHO_FONTE_GAME_OVER)
        self.fonte_pontuacao_final = pygame.font.Font('fontes/Starshines.ttf', config.TAMANHO_FONTE_PONTUACAO_FINAL)
        self.fonte = pygame.font.Font('fontes/Starshines.ttf', 28)
        self.fonte_pequena = pygame.font.Font('fontes/Stardew_Valley.ttf', 21)
        self.fonte_titulo_informacoes = pygame.font.Font('fontes/Starshines.ttf', 36)
        self.fonte_informacoes = pygame.font.Font(None, 30)
        self.botao_voltar = pygame.Rect(LARGURA // 2 - 100, CHAO_Y - 122, 200, 38)

    def _texto_centralizado(self, texto, y, fonte, cor=COR_TEXTO, x=None, sombra=False):
        superficie = fonte.render(texto, True, cor)
        destino = superficie.get_rect(center=(LARGURA // 2 if x is None else x, y))
        if sombra:
            self.tela.blit(fonte.render(texto, True, (0, 0, 0)), destino.move(2, 2))
        self.tela.blit(superficie, destino)

    def _painel(self):
        self.recursos.desenhar(self.tela, 'imagens/mural.png', pygame.Rect(0, 0, LARGURA, CHAO_Y))

    def _botao(self, retangulo, texto):
        pygame.draw.rect(self.tela, (76, 40, 18), retangulo, border_radius=8)
        pygame.draw.rect(self.tela, (230, 173, 96), retangulo, width=2, border_radius=8)
        superficie = self.fonte.render(texto, True, (255, 236, 197))
        self.tela.blit(superficie, superficie.get_rect(center=retangulo.center))

    def clicou_voltar(self, posicao):
        return self.botao_voltar.collidepoint(posicao)

    def desenhar_menu(self, usando_camera=True):
        self.recursos.desenhar(self.tela, 'imagens/logo1.png', pygame.Rect(250, 65, 300, 150))
        inicio, regras = (
            ('agachem juntos para começar', 'pule para abrir as informações') if usando_camera
            else ('aperte espaço para iniciar', 'aperte x para regras')
        )
        self._texto_centralizado(inicio, 285, self.fonte)
        self._texto_centralizado(regras, 330, self.fonte_pequena, COR_TEXTO_SUAVE)

    def desenhar_regras(self, usando_camera=True):
        self._painel()
        self._texto_centralizado('Informações', 85, self.fonte_titulo_informacoes, COR_TEXTO_MURAL)
        self._desenhar_categorias(175)
        linhas = (
            'Acerto +1 ponto',
            'Erro -1 ponto',
            'Lixo no chão -1 coração',
        )
        for indice, linha in enumerate(linhas):
            self._texto_centralizado(linha, 270 + indice * 30, self.fonte_informacoes, COR_TEXTO_MURAL)
        self._botao(self.botao_voltar, 'Voltar')

    def _desenhar_categorias(self, y):
        for indice, classe in enumerate(LIXEIRAS):
            x = LARGURA // 2 + (indice - (len(LIXEIRAS) - 1) / 2) * 110
            imagem = pygame.Rect(x - 40, y - 40, 80, 80)
            self.recursos.desenhar(self.tela, classe.IMAGEM, imagem)
            self._texto_centralizado(classe.NOME.capitalize(), y + 55,
                                     self.fonte_informacoes, COR_TEXTO_MURAL, x=x)

    def desenhar_calibracao(self, progresso=0.0, status=None, usando_camera=True, aviso=''):
        self.desenhar_menu(usando_camera)

    def desenhar_contagem(self, numero):
        self._texto_centralizado(str(numero), CHAO_Y // 2, pygame.font.Font('fontes/Starshines.ttf', 144), sombra=True)

    def desenhar_fim(self, pontuacao):
        self.recursos.desenhar(self.tela, 'imagens/final.png', pygame.Rect(20, 20, LARGURA - 40, CHAO_Y - 40))
        self._texto_centralizado('GAME OVER', CHAO_Y // 2 - 40, self.fonte_game_over, config.COR_GAME_OVER)
        self._texto_centralizado(f'Pontuação: {pontuacao}', CHAO_Y // 2 + 30,
                                 self.fonte_pontuacao_final, config.COR_PONTUACAO_FINAL)
