import pygame
import os


def show_text(text, font, background=None, color=(255, 255, 255), bold=False, italic=False):
    if not text or text.isspace():
        text = " "

    if not pygame.get_init():
        pygame.init()

    width, height = 600, 400
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Загружаем и масштабируем фоновое изображение, если оно указано
    background_surface = None
    if background:
        try:
            background_surface = pygame.image.load(background).convert()
            background_surface = pygame.transform.scale(
                background_surface, (width, height))
        except (pygame.error, FileNotFoundError):
            print(f"Не удалось загрузить фоновое изображение: {background}")
            background_surface = None

    base_font_size = 36

    scale_factor = 1.0
    lines = text.split('\n')
    while lines and lines[-1].isspace():
        lines.pop()
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
    ctrl_pressed = False

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
                        # Масштабируем фоновое изображение при изменении размера окна
                        if background_surface and background:
                            try:
                                background_surface = pygame.image.load(
                                    background).convert()
                                background_surface = pygame.transform.scale(
                                    background_surface, (width, height))
                            except (pygame.error, FileNotFoundError):
                                print(
                                    f"Не удалось перезагрузить фон: {background}")

                        width_scale = (width * 0.9) / max_width
                        height_scale = (height * 0.9) / total_height
                        scale_factor = min(width_scale, height_scale)
                        scale_factor = max(0.1, min(5.0, scale_factor))
                    elif event.type == pygame.MOUSEWHEEL:
                        old_scale = scale_factor
                        scale_factor *= (1.1 if event.y > 0 else 0.9)
                        scale_factor = max(0.1, min(5.0, scale_factor))
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                            ctrl_pressed = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                            ctrl_pressed = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Левая кнопка мыши
                            dragging = True  # Начинаем перетаскивание в любом случае
                            last_mouse_pos = event.pos
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            dragging = False
                    elif event.type == pygame.MOUSEMOTION:
                        if dragging:  # Перетаскивание работает как с Ctrl, так и без него
                            current_pos = event.pos
                            offset_x += current_pos[0] - last_mouse_pos[0]
                            offset_y += current_pos[1] - last_mouse_pos[1]
                            last_mouse_pos = current_pos

                font_size = int(base_font_size * scale_factor)
                custom_font = pygame.font.Font(font_path, font_size)

                text_surfaces = [custom_font.render(
                    line, True, color) for line in lines]

                line_height = custom_font.get_linesize()
                total_height = line_height * len(lines)
                start_y = (height - total_height) // 2 + offset_y

                if background_surface:
                    screen.blit(background_surface, (0, 0))
                else:
                    screen.fill((0, 0, 0))

                for i, surface in enumerate(text_surfaces):
                    text_rect = surface.get_rect(
                        centerx=width // 2 + offset_x, y=start_y + i * line_height)
                    screen.blit(surface, text_rect)

                pygame.display.flip()

            except pygame.error as e:
                print(f"Ошибка pygame: {e}")
                break
    finally:
        pygame.quit()


if __name__ == "__main__":
    show_text("Hello\n World!", "InfernalFont-Regular.ttf")
