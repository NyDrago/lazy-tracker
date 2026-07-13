# lazy-tracker

super duper optimized 2.8 kbs python script to make your wallpaper track your mouse cursor across the screen by cycling through frames


## how it works
- **hyprland (wayland native):** reads your cursor coordinates directly via `hyprctl` so wayland's locked down security model doesn't block it.
- **performance saving:** automatically pauses the background rendering loop if a window is active or fullscreen so it doesn't waste cpu cycles while you're gaming or coding.
- **universal fallback:** falls back to `pyautogui` for basic x11 linux environments if hyprland isn't running.

## dependencies
- `python3`
- `awww` (wallpaper daemon for hyprland)
- `pyautogui` (only if you need the x11 fallback backend) IF IT REJECTS THE INSTALLATION run **pip install pyautogui --break-system-packages** in your terminal

## setup
(steps very similar on windows but without the dawww-daemon ofc)
1. dump your animation frames into a directory. (use numbers or abcs to sort them. frame_001.png frame_002.png etc work best though. **also if youre going to double digits you must use 00 01 02 all the way till ten NOT 1 2 3 4 5... 10)**
2. open with your text editor `temperantLazyTracker.py` and set your path
3. change the screen width if needed in that same file **IF YOUR MOUSE TRACKING FEELS WEIRD, KEEP ON CHANGING THE WIDTH TILL ITS RIGHT. (by weird like not tracking some frames or doing it too fast or too slow)**
4. make sure your script opens with startup. (run in with python, like **python ~/temperantLazyTracker.py**) make sure you change it to your actual directory tho
5. IGNORE THIS IF YOURE NOT ON HYPRLAND make sure awww-daemon also runs on startup in your hyprland file.

i have NO idea how much DEs this works on. so far ive tested on hyprland, xfce, lxqt and they worked. but this is originally made for hyprland so dont expect it to work well elsewhere.. (if youre de cannot switch wallpapers quickly like on lxqt. try to get a different wallpaper manager or else itll be laggy. )
