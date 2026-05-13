import pygame

from ui.colors import Colores


class Render:

    def __init__(self, screen, city, tile_size):

        self.screen = screen
        self.city = city
        self.tile_size = tile_size

        self.ancho_mapa = (
            (city.grid_size - 1)
            * tile_size
        )

        self.alto_mapa = (
            (city.grid_size - 1)
            * tile_size
        )

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        self.offset_x = (
            screen_width - self.ancho_mapa
        ) // 2

        self.offset_y = (
            screen_height - self.alto_mapa
        ) // 2

        self.font = pygame.font.SysFont(
            "Courier New",
            24,
            bold=True
        )

    def to_screen(self, x, y):

        return (
            x * self.tile_size + self.offset_x,
            y * self.tile_size + self.offset_y
        )

    def render_caminos(self):

        for camino in self.city.caminos:

            start = self.to_screen(
                camino.inicio.x,
                camino.inicio.y
            )

            end = self.to_screen(
                camino.fin.x,
                camino.fin.y
            )

            pygame.draw.line(
                self.screen,
                Colores.GRIS_OSCURO,
                start,
                end,
                4
            )
    def render_sentidos(self):

        for x in range(self.city.grid_size):

            simbolo = "↓"

            if x % 2 != 0:
                simbolo = "↑"

            pos_x = (
                x * self.tile_size
                + self.offset_x
            )

            pos_y = self.offset_y - 40

            texto = self.font.render(
                simbolo,
                True,
                Colores.NEGRO
            )

            rect = texto.get_rect(
                center=(pos_x, pos_y)
            )

            self.screen.blit(
                texto,
                rect
            )

        for y in range(self.city.grid_size):

            simbolo = "→"

            if y % 2 != 0:
                simbolo = "←"

            pos_x = self.offset_x - 40

            pos_y = (
                y * self.tile_size
                + self.offset_y
            )

            texto = self.font.render(
                simbolo,
                True,
                Colores.NEGRO
            )

            rect = texto.get_rect(
                center=(pos_x, pos_y)
            )

            self.screen.blit(
                texto,
                rect
            )

    def render_intersecciones(self):

        for row in self.city.intersecciones:

            for interseccion in row:

                pos = self.to_screen(
                    interseccion.x,
                    interseccion.y
                )

                pygame.draw.circle(
                    self.screen,
                    Colores.AMARILLO,
                    pos,
                    6
                )

    def render_autos(self, autos):

        for auto in autos:

            pos = self.to_screen(
                auto.x,
                auto.y
            )

            rect = pygame.Rect(
                pos[0] - 8,
                pos[1] - 8,
                16,
                16
            )

            pygame.draw.rect(
                self.screen,
                auto.color,
                rect
            )

    def render(self, autos):

        self.screen.fill(Colores.GRIS)
        self.render_caminos()
        self.render_intersecciones()
        self.render_sentidos()  
        self.render_autos(autos)