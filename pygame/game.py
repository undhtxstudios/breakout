from breakout import Breakout
from common.constants import DEFAULT_RESOLUTION, resolutions, DEFAULT_FPS, FPS, DEFAULT_THEME, themes

def main(resolution=DEFAULT_RESOLUTION, fps=DEFAULT_FPS, theme=DEFAULT_THEME):

    if resolution not in resolutions:
        # add debug info
        return

    if fps not in FPS:
        return
    
    if theme not in themes:
        return

    Breakout(resolution, fps, theme).run()

if __name__ == '__main__':
    main()