# 🎵 Project-Rythmix
A Python-based desktop application for organizing and playing your local MP3 music collection. The Rythmix provides a user-friendly interface for importing songs, managing metadata, and controlling playback, all powered by PyQt6, Pygame, and MySQL Database.

## 📖 Project Overview

Rythmix is a lightweight, offline desktop app that lets users:

- 🎶 Import and play MP3 files

- 📝 Edit music metadata (title, artist, album, etc.)

- 👤 Create and manage user accounts

- 🧾 Store music and account data persistently in an SQLite database

- 🎛️ Use a clean, modern interface built with PyQt6

It’s an ideal solution for local music library enthusiasts looking for a sleek, minimal MP3 organizer and player.

## 🧪 Library Tutorials 
### 📚 PyQt6
Used for designing the graphical user interface (GUI). .ui files were built in Qt Designer and converted to Python code.
> Install:
```
pip install PyQt6
```
> Convert .ui
```
pyuic6 login.ui -o login.py
```

### 🎮 Pygame 
Handles audio playback (MP3 files). Enables play, pause, stop, and volume controls.
> Install:
```
pip install pygame
```
> Basic example: 
```
pyuic6 login.ui -o login.py
```

🗃️ MySQL 
Stores user data and music entries persistently. The database file is Music_App.db.
