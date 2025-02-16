import pygame
import os


def show_text(text, font, bold=False, italic=False):
    # Если текст пустой, показываем пустое окно
    if not text or text.isspace():
        text = " "  # Используем пробел вместо пустой строки

    # Проверяем, не инициализирован ли уже pygame
    if not pygame.get_init():
        pygame.init()

    width, height = 600, 400
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    base_font_size = 36

    scale_factor = 1.0
    lines = text.split('\n')
    # Убираем пустые строки в конце текста
    while lines and lines[-1].isspace():
        lines.pop()
    # Если после очистки не осталось строк, добавляем одну пустую
    if not lines:
        lines = [" "]

    if font != "harpers" and font != 'infernal':
        if bold and italic:
            font_path = f'data/fonts/{font}/{font}-bold-italic.ttf'
        elif bold:
            font_path = f'data/fonts/{font}/{font}-bold.ttf'
        elif italic:
            font_path = f'data/fonts/{font}/{font}-italic.ttf'
        else:
            font_path = f'data/fonts/{font}/{font}.ttf'
    else:
        font_path = f'data/fonts/{font}/{font}.ttf'

    temp_font = pygame.font.Font(font_path, base_font_size)

    max_width = max(temp_font.size(line)[0] for line in lines)
    total_height = temp_font.get_linesize() * len(lines)

    width_scale = (width * 0.9) / max_width
    height_scale = (height * 0.9) / total_height

    scale_factor = min(width_scale, height_scale)
    scale_factor = max(0.1, min(5.0, scale_factor))

    dragging = False
    offset_x, offset_y = 0, 0
    last_mouse_pos = (0, 0)

    running = True
    try:
        while running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.VIDEORESIZE:
                        width, height = event.size
                        screen = pygame.display.set_mode(
                            (width, height), pygame.RESIZABLE)
                        width_scale = (width * 0.9) / max_width
                        height_scale = (height * 0.9) / total_height
                        scale_factor = min(width_scale, height_scale)
                        scale_factor = max(0.1, min(5.0, scale_factor))
                    elif event.type == pygame.MOUSEWHEEL:
                        old_scale = scale_factor
                        scale_factor *= (1.1 if event.y > 0 else 0.9)
                        scale_factor = max(0.1, min(5.0, scale_factor))
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            dragging = True
                            last_mouse_pos = event.pos
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            dragging = False
                    elif event.type == pygame.MOUSEMOTION:
                        if dragging:
                            current_pos = event.pos
                            offset_x += current_pos[0] - last_mouse_pos[0]
                            offset_y += current_pos[1] - last_mouse_pos[1]
                            last_mouse_pos = current_pos

                font_size = int(base_font_size * scale_factor)
                custom_font = pygame.font.Font(font_path, font_size)

                text_surfaces = [custom_font.render(
                    line, True, (255, 255, 255)) for line in lines]

                line_height = custom_font.get_linesize()
                total_height = line_height * len(lines)
                start_y = (height - total_height) // 2 + offset_y

                screen.fill((0, 0, 0))

                for i, surface in enumerate(text_surfaces):
                    text_rect = surface.get_rect(
                        centerx=width // 2 + offset_x, y=start_y + i * line_height)
                    screen.blit(surface, text_rect)

                pygame.display.flip()

            except pygame.error:
                break
    finally:
        # Убеждаемся, что pygame корректно закрывается даже при ошибках
        pygame.quit()


if __name__ == "__main__":
    show_text("Hello\n World!", "InfernalFont-Regular.ttf")
