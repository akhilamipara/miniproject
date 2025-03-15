import streamlit as st
import pyautogui
import time
import screen_brightness_control as sbc
import os

def automate_notepad():
    try:
        pyautogui.press('win')
        time.sleep(2)
        pyautogui.write('notepad')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2) 

        pyautogui.write("Python is a versatile programming language widely used for web development, data analysis, machine learning, and automation, offering a clean and readable syntax that makes it beginner-friendly and suitable for a wide range of applications.",interval=0.05)
        time.sleep(5)

        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write('task_c')
        time.sleep(2)
        pyautogui.press('enter') 
        time.sleep(1)

        return "Notepad opened, message typed, and file saved successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

def gradual_brightness_change(target_level, step=3, delay=0.2):
    current_brightness = sbc.get_brightness(display=0)[0]
    if current_brightness < target_level:
        for level in range(current_brightness, target_level + 1, step):
            sbc.set_brightness(level)
            time.sleep(delay)
    else:
        for level in range(current_brightness, target_level - 1, -step):
            sbc.set_brightness(level)
            time.sleep(delay)
    sbc.set_brightness(target_level)
    return f"Brightness set to {target_level}%"

def open_vlc_and_play(video_path):
    try:
        os.startfile(video_path)  
        return f"Playing video: {video_path}"
    except Exception as e:
        return f"An error occurred while opening VLC: {e}"

def play_default_video():
    default_video_path ="C:\\Users\\DELL\\Videos\\52849-473336269_large.mp4" 
    return open_vlc_and_play(default_video_path)

def open_spotify_and_play():
    try:
        pyautogui.press('win')  
        time.sleep(1)
        pyautogui.write('spotify')  
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5) 

        pyautogui.hotkey('ctrl', 'k') 
        time.sleep(1)
        pyautogui.write('maharas')
        time.sleep(2)
        pyautogui.press('enter')  
        time.sleep(3)
        
        return "Spotify opened and song is playing!"
    except Exception as e:
        return f"An error occurred while opening Spotify: {e}"

st.title("Automation Suite: Notepad, Brightness, VLC & Spotify")

st.write("### Open Notepad and Save a File")
if st.button("Open Notepad"):
    result = automate_notepad()
    st.success(result)

st.write("### Adjust Screen Brightness")
if st.button("Decrease Brightness"):
    result = gradual_brightness_change(0, step=2, delay=0.1)
    st.success(result)

if st.button("Increase Brightness"):
    result = gradual_brightness_change(100, step=2, delay=0.1) 
    st.success(result)

st.write("Open VLC Player and Play Video")
if st.button("Play Video"):
    result = play_default_video()
    st.success(result)

st.write("Open Spotify and Play a Song")
if st.button("Play a Song on Spotify"):
    result = open_spotify_and_play()
    st.success(result)