#!/usr/bin/env python3
# MADE BY TEMPERANCE!! (github.com/nydrago || nydrago on discord)
# MIT License - Copyright (c) 2026 TEMPERANCE
import os
import time
import ctypes

SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

frame_directory = r"C:\Users\UrUser\Desktop\mio_frames"
previous_frame_index = -1

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def fetch_ordered_frames(target_dir):
    if not os.path.isdir(target_dir):
        return []
    valid_extensions = (".png", ".jpg", ".jpeg")
    found_files = [
        os.path.abspath(os.path.join(target_dir, file_name))
        for file_name in os.listdir(target_dir)
        if file_name.lower().endswith(valid_extensions)
    ]
    return sorted(found_files)

def fetch_cursor_x():
    cursor_coordinates = POINT()
    user32.GetCursorPos(ctypes.byref(cursor_coordinates))
    return cursor_coordinates.x

def update_system_wallpaper(image_path):
    user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 
        0, 
        image_path, 
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )

display_width = user32.GetSystemMetrics(0)
animation_frames = fetch_ordered_frames(frame_directory)
frame_count = len(animation_frames)

while True:
    if frame_count == 0:
        time.sleep(1.5)
        animation_frames = fetch_ordered_frames(frame_directory)
        frame_count = len(animation_frames)
        continue

    current_x = fetch_cursor_x()
    
    if current_x < 0:
        current_x = 0
    elif current_x >= display_width:
        current_x = display_width - 1

    calculated_index = int((current_x / display_width) * frame_count)
    if calculated_index >= frame_count:
        calculated_index = frame_count - 1

    if calculated_index != previous_frame_index:
        update_system_wallpaper(animation_frames[calculated_index])
        previous_frame_index = calculated_index

    time.sleep(0.016)
