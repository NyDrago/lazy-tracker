#!/usr/bin/env python3
#MADE BY TEMPERANCE!! (with love. github.com/nydrago || nydrago on discord)
import os
import time
import json
import subprocess

frame_dir = "/home/temperance/Pictures/mio_frames" # make sure to replace this with your actual directory containing the frames!!
last_frame_idx = -1

is_hyprland = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE") is not None

if not is_hyprland:
    try:
        import pyautogui
        screen_width, screen_height = pyautogui.size()
        use_pyautogui = True
    except Exception as e:
        print(f"failed to initialize pyautogui backend: {e}")
        use_pyautogui = False
else:
    screen_width = 1080  #this doesnt have to do with your actual screen width. just set it to whatever works for you. the more frames you have the less it should be. but just set it as whatever works
    use_pyautogui = False

def get_sorted_frames():
    try:
        return sorted([
            os.path.join(frame_dir, f)
            for f in os.listdir(frame_dir)
            if f.endswith((".png", ".jpg", ".jpeg"))
        ])
    except:
        return []

def is_window_focused_or_fullscreen():
    if is_hyprland:
        try:
            out = subprocess.check_output(["hyprctl", "activewindow", "-j"]).decode()
            win_data = json.loads(out)
            if not win_data or win_data.get("class") == "":
                return False
            if win_data.get("fullscreen", False) or (win_data.get("class") and not win_data.get("floating", False)):
                return True
            return False
        except:
            return False
    return False

def get_mouse_x():
    if is_hyprland:
        try:
            out = subprocess.check_output(["hyprctl", "cursorpos", "-j"]).decode()
            return json.loads(out)["x"]
        except:
            return 0
    elif use_pyautogui:
        try:
            return pyautogui.position().x
        except:
            return 0
    return 0

def apply_wallpaper(frame_path):
    if is_hyprland:
        subprocess.run(["awww", "img", frame_path, "--transition-type", "none"])
    else:
        subprocess.run(["pcmanfm-qt", "-w", frame_path])
frames = get_sorted_frames()
total_frames = len(frames)
print(f"tracking system initialized. backend: {'hyprland native' if is_hyprland else 'pyautogui universal'}")

while True:
    if total_frames == 0:
        time.sleep(1)
        frames = get_sorted_frames()
        total_frames = len(frames)
        continue

    if is_window_focused_or_fullscreen():
        time.sleep(0.1)
        continue

    mx = get_mouse_x()
    mx = max(0, min(mx, screen_width - 1))

    frame_idx = round((mx / (screen_width - 1)) * (total_frames - 1))

    if frame_idx != last_frame_idx:
        print(frame_idx, os.path.basename(frames[frame_idx]))
        apply_wallpaper(frames[frame_idx])
        last_frame_idx = frame_idx

    time.sleep(0.016)
    # yo im goated right?
