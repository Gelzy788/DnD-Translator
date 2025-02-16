import pygame
import os


def show_text(text, font, bold=False, italic=False):
    pygame.init()

    # Начальные размеры окна
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    base_font_size = 36
    # Коэффициент масштабирования текста
    scale_factor = 1.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                screen = pygame.display.set_mode(
                    (width, height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEWHEEL:
                # Изменяем масштаб при прокрутке колесика
                # Увеличиваем/уменьшаем на 10% за одну прокрутку
                scale_factor *= (1.1 if event.y > 0 else 0.9)
                # Ограничиваем минимальный и максимальный масштаб
                scale_factor = max(0.1, min(5.0, scale_factor))

        # Масштабируем размер шрифта относительно высоты окна и коэффициента масштабирования
        font_size = int(base_font_size * (height / 400) * scale_factor)
        font_path = f'data/fonts/infernal/{font}'
        custom_font = pygame.font.Font(font_path, font_size)

        lines = text.split('\n')
        text_surfaces = [custom_font.render(
            line, True, (255, 255, 255)) for line in lines]

        line_height = custom_font.get_linesize()
        total_height = line_height * len(lines)

        start_y = (height - total_height) // 2

        screen.fill((0, 0, 0))

        for i, surface in enumerate(text_surfaces):
            text_rect = surface.get_rect(
                centerx=width // 2, y=start_y + i * line_height)
            screen.blit(surface, text_rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    show_text("Hello\n World!", "InfernalFont-Regular.ttf")
