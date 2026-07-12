# lazy-tracker

super duper optimized 2.8 kbs python script to make your wallpaper track your mouse cursor across the screen by cycling through frames

>FUCK windows NO WINDOWS SUPPORT keep using your wallpaper engine bloat while WE are on a 2.8 kbs script

## how it works
- **hyprland (wayland native):** reads your cursor coordinates directly via `hyprctl` so wayland's locked down security model doesn't block it.
- **performance saving:** automatically pauses the background rendering loop if a window is active or fullscreen so it doesn't waste cpu cycles while you're gaming or coding.
- **universal fallback:** falls back to `pyautogui` for basic x11 linux environments if hyprland isn't running.

## dependencies
- `python3`
- `awww` (wallpaper daemon for hyprland)
- `pyautogui` (only if you need the x11 fallback backend) IF IT REJECTS THE INSTALLATION run **pip install pyautogui --break-system-packages** in your terminal

## setup
1. dump your animation frames into a directory. (use numbers or abcs to sort them. frame_001.png frame_002.png etc work best though. **also if youre going to double digits you must use 00 01 02 all the way till ten NOT 1 2 3 4 5... 10)**
2. open `temperantLazyTracker.py` and set your path
3. make sure your script opens with startup. (run in with python, like **python ~/temperantLazyTracker.py**) make sure you change it to your actual directory tho

