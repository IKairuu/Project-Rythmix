# 🎵 Project-Rythmix
A Python-based desktop application for organizing and playing your local MP3 music collection. The Rythmix provides a user-friendly interface for importing songs, managing metadata, and controlling playback, all powered by PyQt6, Pygame, and MySQL Database.

## 📖 Project Overview

Rythmix is a lightweight, offline desktop app that lets users:

- 🎶 Import and play MP3 files

- 📝 Edit music metadata (title, artist, album, etc.)

- 👤 Create and manage user accounts

- 🧾 Store music and account data persistently in the  MySQL database

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

### 🗃️ MySQL 
Stores user data and music entries persistently. The database file is Music_App.db.

Download [MySQL Workbench here](https://dev.mysql.com/downloads/mysql/)
> Example:
```
db = mysql.connector.connect(
host = "localhost",
user = "root",
database = "database_name",
password = "password"
)         
```

> [!IMPORTANT]
>   Execute each line in  the file(main_query.sql)


### 🧠 How the Program Works
1. Login / Account Creation - Users can sign up or log in with credentials. Data is stored in MySQL Database.

2. Main Dashboard - Displays the music library. Users can import new music or select tracks to play.

3. Music Importing - Allows adding new MP3 files. Metadata can be edited post-import.

4. Music Playback - Controlled by pygame.mixer with play/pause/stop functions.

5. Edit Functions - Users can update their account info or music details directly.

### ⚙️ Technologies Used

| Technology | Purpose | 
| --- | --- |
| Python3 | Core programming language |
| PyQt6 | UI framework for GUI design |
| Pygame | MP3 playback (mixer module) |
| MySQL Workbench | Local database |
| Qt Designer | GUI layout creation |
| OS module | File path and directory handling |

## 🌱 Future Improvements
### 🎥 YouTube Integration
- Import music directly from YouTube
- Use yt-dlp or pytube to download and convert audio
- Auto-fill metadata from video title and description

### 🔍 Search and Filter
- Search tracks by title, artist, or album
- Add sorting by name, date, or length

### 📂 Playlist Support
- Create custom playlists

- Support for playback queues

### 🎨 Theme Options
- Add light/dark mode toggle

- User-selectable color themes

### ☁️ Cloud Sync (Optional)
- Backup user data and songs to a cloud service

### ✅ Testing and Stability
- Add exception handling, input validation

- Add unit tests and error logging


