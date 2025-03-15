# Automation Suite: Notepad, Brightness, VLC & Spotify

## Overview
This project automates multiple tasks using Python, including:
- Opening Notepad and typing a predefined message.
- Adjusting screen brightness gradually.
- Playing a video using VLC Media Player.
- Opening Spotify and playing a specific song.

The automation is controlled using a **Streamlit** web interface.

## Features
1. **Notepad Automation**
   - Opens Notepad.
   - Writes a predefined message.
   - Saves the file as `task_c.txt`.

2. **Brightness Control**
   - Gradually increases or decreases the screen brightness.

3. **VLC Media Player Automation**
   - Opens and plays a predefined video file.

4. **Spotify Automation**
   - Opens Spotify.
   - Searches for a song and plays it.

## Requirements
Make sure you have the following dependencies installed:

```bash
pip install streamlit pyautogui screen-brightness-control
```

## How to Run
1. Clone or download this project.
2. Open a terminal and navigate to the project folder.
3. Run the following command to start the Streamlit app:

```bash
streamlit run task_c.py.py
```

4. The web interface will open in your browser.
5. Click the buttons to perform the automated tasks.

## Notes
- The script uses `pyautogui` for UI automation. Ensure that your system has **Notepad, VLC, and Spotify installed**.
- If VLC does not open, check the default video path in the script and update it accordingly.
- Some delays are added using `time.sleep()` to ensure smooth execution.

## License
This project is open-source and available for use under the MIT License.

