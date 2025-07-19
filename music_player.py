import sys, os
import tkinter, shutil, tkinter.filedialog, tkinter.messagebox, re
from login import Ui_Login_Window as login_frame
from create import Ui_CreateAccountFrame as create_frame
from main import Ui_MainFrame as main_frame
from importMusic import Ui_ImportMusic as music_import_frame
from edit import Ui_EditMusic as edit_music_frame
from editaccount import Ui_EditAccount as edit_account_frame
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QStackedWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from database import MusicManagerDatabase as database
from pygame import mixer
        
class LoginFrame(QMainWindow, login_frame):
    def __init__(self, database):
        super().__init__() 
        self.setupUi(self)
        self.database = database
        self.update_users()
        
        self.create_account_button.clicked.connect(self.go_to_create_account)
        self.login_button.clicked.connect(self.go_to_main_frame)
    
    def go_to_create_account(self):
        widget.setCurrentWidget(create_page)
    
    def go_to_main_frame(self):
        found = False
        print(self.users_list)
        for users in self.users_list:
            if users['username'] == self.login_name_line.text() and users['user_password'] == self.login_password_line.text():
                found = True
                id = users['id']
                break
        
        if found:
            print(self.database.get_username_password)
            self.database.set_username_password(self.login_name_line.text(), self.login_password_line.text(), id)
            tkinter.messagebox.showinfo(title="LOGIN", message=f'Logged In as {self.login_name_line.text()}')
            self.login_name_line.clear()
            self.login_password_line.clear()
            user_page.refresh()
            user_page.update_import_table()
            user_page.update_playlist_table()
            user_page.update_fav_table()
            edit_music_page.refresh()
            import_music_page.refresh()
            widget.setCurrentWidget(user_page)
        else:
            tkinter.messagebox.showerror(title='User Not Found', message='User is not found')
        
    def update_users(self):
        connect = self.database.connect_database()
        self.users_list = self.database.get_user_info(connect)

    def remove_user(self, user_id:str):
        for index, users in enumerate(self.users_list):
            if users['id'] == user_id: 
                self.users_list.pop(index)
                break
    
    def edit_user(self, user_id:str, new_username:str, new_password:str):
        for users in self.users_list:
            if users['id'] == user_id:
                users['username'] = new_username
                users['user_password'] = new_password
                break
                

class CreateAccount(QDialog, create_frame):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.users = self.get_user_list()
        self.setupUi(self)
        
        self.create_back_button.clicked.connect(self.go_to_login)
        self.create_account_button.clicked.connect(self.confirm_create_account)
        
    def go_to_login(self):
        widget.setCurrentWidget(login_page)
    
    def confirm_create_account(self):
        error = False
        connect2 = self.database.connect_database()
        user_list = self.get_user_list()
        for users in user_list:
            if users['username'] == self.create_name_line.text():
                error = True
                tkinter.messagebox.showerror(title='Invalid Username', message='Username is already used')
                break
            elif len(self.create_password_line.text()) <= 8:
                error = True
                tkinter.messagebox.showerror(title='Invalid Input', message='Password must be 8 characters or more')
                break
                
        if not error:
            self.database.sign_in(connect2, self.create_name_line.text(), self.create_password_line.text())
            login_page.update_users()
            self.create_name_line.clear()
            self.create_password_line.clear()
            widget.setCurrentWidget(login_page)
    
    def get_user_list(self):
        connect = self.database.connect_database()
        user_list = self.database.get_user_info(connect)
        return user_list

class MainFrame(QDialog, main_frame): #MAIN INTERFACE OF THE USER
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setupUi(self)
        self.playing = False
        self.current_music = ""
        
        self.edit_music_button.clicked.connect(self.go_to_edit_music)
        self.import_button.clicked.connect(self.go_to_import_music)
        self.edit_account_button.clicked.connect(self.go_to_edit_account)
        self.delete_music_button.clicked.connect(self.delete_music_table)
        self.play_play.clicked.connect(lambda:self.play_music('playlist'))
        self.play_pause.clicked.connect(self.pause_music)
        self.play_volume.valueChanged.connect(self.play_change_volume)
        self.play_rewind.clicked.connect(self.move_music)
        self.add_fav_button.clicked.connect(self.add_to_favorites)
        self.remove_fav_button.clicked.connect(self.remove_favorite)
        self.fav_play.clicked.connect(lambda:self.play_music('favorites'))
        self.fav_pause.clicked.connect(self.pause_music)
        self.fav_rewind.clicked.connect(self.move_music)
        self.fav_volume.valueChanged.connect(self.play_change_volume)
        self.search_button.clicked.connect(self.update_search_table)
        self.search_play_2.clicked.connect(lambda:self.play_music('search'))
        self.search_pause_2.clicked.connect(self.pause_music)
        self.search_rewind_2.clicked.connect(self.move_music)
        self.search_volume.valueChanged.connect(self.play_change_volume)
        self.delete_account_button.clicked.connect(self.delete_account)
        self.sign_out_button.clicked.connect(self.sign_out)
        
    def refresh(self):
        self.username, self.password, self.id = self.database.get_username_password()
        
    def go_to_edit_music(self):
        connect, connect2 = self.database.connect_database(), self.database.connect_database()
        counts = 0
        id = ""
        song = ""
        user_playlist = self.database.get_user_music_info(connect2, self.id)
        for row in range(self.import_table.rowCount()):
            if self.import_table.item(row, 1).checkState() == Qt.CheckState.Checked:
                counts += 1
                song = self.import_table.item(row, 1).text()
        
        for music in user_playlist:
            if song == music['title']:
                id = music['id']
        
        if counts > 1:
            tkinter.messagebox.showerror(title='Music Player', message='You May Only Select One Music')
            return None
        elif counts == 0:
            tkinter.messagebox.showerror(title='Music Player', message='No Music Selected')
            return None
        else:
            edit_music_page.get_selected_music(id)
            widget.setCurrentWidget(edit_music_page)
    
    def go_to_import_music(self):
        widget.setCurrentWidget(import_music_page)
    
    def go_to_edit_account(self):
        widget.setCurrentWidget(edit_account_page)
    
    def select_music(self, play:str) -> str:
        song = ""
        selected = 0
        if play == 'playlist':
            for rows in range(self.play_table.rowCount()):
                if self.play_table.item(rows, 1).checkState() == Qt.CheckState.Checked:
                    selected += 1
                    song = self.play_table.item(rows, 1).text()
        elif play == 'search':
            for rows in range(self.search_table.rowCount()):
                if self.search_table.item(rows, 1).checkState() == Qt.CheckState.Checked:
                    selected += 1
                    song = self.search_table.item(rows, 1).text()
        elif play == 'favorites':
            for rows in range(self.fav_table.rowCount()):
                if self.fav_table.item(rows, 1).checkState() == Qt.CheckState.Checked:
                    selected += 1
                    song = self.fav_table.item(rows, 1).text()
        
        if selected > 1:
            tkinter.messagebox.showerror(title='Music Player', message='You May Only Select One Music')
            return None
        elif selected == 0:
            tkinter.messagebox.showerror(title='Music Player', message='No Music Selected')
            return None
        else:
            return song
    
    def play_music(self, play:str):
        selected_song = self.select_music(play)
        connect = self.database.connect_database()
        if selected_song is not None:
            if self.current_music != selected_song:
                self.current_music = selected_song
                self.file_name = self.database.play_music(connect, selected_song, self.id)
        
                self.playing = True
                self.play_title.setText(selected_song)
                self.fav_title.setText(selected_song)
                self.search_title.setText(selected_song)
                self.play_volume.setValue(99)
                self.fav_volume.setValue(99)
                self.search_volume.setValue(99)
                
                tkinter.Tk().withdraw()
                mixer.init()
                mixer.music.load(self.file_name)
                mixer.music.set_volume(0.9)
                mixer.music.play()
            else:
                if not self.playing:    
                    mixer.music.unpause()
                    self.playing = True
                    
    def move_music(self):
        rewind = (mixer.music.get_pos()-10000)/1000
        if rewind > 0: mixer.music.play(0, rewind)
        else: mixer.music.play(0, 0)
        
    def pause_music(self):
        if self.current_music != "":
            mixer.music.pause()
            self.playing = False
    
    def play_change_volume(self, value):
        mixer.init()
        mixer.music.set_volume(round(value*0.01, 1))
        self.fav_volume.setValue(value)
        self.play_volume.setValue(value)
        self.search_volume.setValue(value)

    def update_import_table(self):
        connect = self.database.connect_database()
        self.playlist = self.database.get_user_music_info(connect, self.id)
        if len(self.playlist) != 0:
            setRowCount = self.import_table.setRowCount(len(self.playlist)-1)
            self.import_table.insertRow(self.import_table.rowCount())
            for rows in range(self.import_table.rowCount()):
                id = QTableWidgetItem(str(self.playlist[rows]['id']))
                title = QTableWidgetItem(self.playlist[rows]['title'])
                artist = QTableWidgetItem(self.playlist[rows]['artist'])
                duration = QTableWidgetItem(str(self.playlist[rows]['duration']))
                title.setCheckState(Qt.CheckState.Unchecked)
                music_list = [id, title, artist, duration]
                for column, values in enumerate(music_list):
                    self.import_table.setItem(rows, column, values)
    
    def update_search_table(self):
        self.search_table.setRowCount(0)
        connect = self.database.connect_database()
        user_music = self.database.get_user_music_info(connect, self.id)
        searched = []
        for songs in user_music:
            if songs['title'] == self.search_line.text() or songs['artist'] == self.search_line.text():
                searched.append(songs)
        if len(searched) != 0:
            setRowCount = self.search_table.setRowCount(len(searched)-1)
            self.search_table.insertRow(self.search_table.rowCount())
            for rows in range(self.search_table.rowCount()):
                id = QTableWidgetItem(str(searched[rows]['id']))
                title = QTableWidgetItem(searched[rows]['title'])
                artist = QTableWidgetItem(searched[rows]['artist'])
                duration = QTableWidgetItem(str(searched[rows]['duration']))
                title.setCheckState(Qt.CheckState.Unchecked)
                music_list = [id, title, artist, duration]
                for column, values in enumerate(music_list):
                    self.search_table.setItem(rows, column, values)
        
        self.search_line.clear()

    def update_playlist_table(self):
        connect = self.database.connect_database()
        self.playlist = self.database.get_user_music_info(connect, self.id)
        if len(self.playlist) != 0:
            setRowCount = self.play_table.setRowCount(len(self.playlist)-1)
            self.play_table.insertRow(self.play_table.rowCount())
            for rows in range(self.play_table.rowCount()):
                id = QTableWidgetItem(str(self.playlist[rows]['id']))
                title = QTableWidgetItem(self.playlist[rows]['title'])
                artist = QTableWidgetItem(self.playlist[rows]['artist'])
                duration = QTableWidgetItem(str(self.playlist[rows]['duration']))
                title.setCheckState(Qt.CheckState.Unchecked)
                music_list = [id, title, artist, duration]
                for column, values in enumerate(music_list):
                    self.play_table.setItem(rows, column, values)
    
    def delete_music_table(self):
        deleted = False
        for row in range(self.import_table.rowCount()):
            connect, connect2 = self.database.connect_database(), self.database.connect_database()
            if self.import_table.item(row, 1).checkState() == Qt.CheckState.Checked:
                self.database.delete_music(connect, self.id, self.import_table.item(row, 1).text())
                self.database.remove_to_favorites(connect2, self.id, self.import_table.item(row, 0).text())
                deleted = True
        
        if deleted: 
            self.import_table.setRowCount(0)
            self.play_table.setRowCount(0)
                
        self.update_fav_table()
        self.update_import_table()
        self.update_playlist_table()
        self.update_search_table()
    
    def add_to_favorites(self):
        connect, connect2 = self.database.connect_database(), self.database.connect_database()
        user_playlist = self.database.get_user_music_info(connect, self.id)
        fav_playlist = self.database.get_fav_music(connect2, self.id)
        
        for rows in range(self.import_table.rowCount()):
            found = False
            connect3 = self.database.connect_database()
            if self.import_table.item(rows, 1).checkState() == Qt.CheckState.Checked:
                if fav_playlist is not None:
                    for favs in fav_playlist:
                        if favs['title'] == self.import_table.item(rows, 1).text():
                            found = True
                    if not found:
                        for music in user_playlist:
                            if music['title'] == self.import_table.item(rows, 1).text():
                                self.database.add_favorite(connect3, music['id'], music['title'], music['artist'], music['duration'], music['file_name'], self.id)
        
        self.update_fav_table()
    
    def remove_favorite(self):
        connect = self.database.connect_database()
        deleted = False
        
        for rows in range(self.fav_table.rowCount()):
            connect2 = self.database.connect_database()
            if self.fav_table.item(rows, 1).checkState() == Qt.CheckState.Checked:
                self.database.remove_to_favorites(connect2, self.id, self.fav_table.item(rows, 0).text())
                deleted = True
        
        if deleted:
            self.fav_table.setRowCount(0)
        
        self.update_fav_table()
    
    def update_fav_table(self):
        self.fav_table.setRowCount(0)
        connect = self.database.connect_database()
        self.playlist = self.database.get_fav_music(connect, self.id)
        if len(self.playlist) != 0:
            setRowCount = self.fav_table.setRowCount(len(self.playlist)-1)
            self.fav_table.insertRow(self.fav_table.rowCount())
            for rows in range(self.fav_table.rowCount()):
                id = QTableWidgetItem(str(self.playlist[rows]['id']))
                title = QTableWidgetItem(self.playlist[rows]['title'])
                artist = QTableWidgetItem(self.playlist[rows]['artist'])
                duration = QTableWidgetItem(str(self.playlist[rows]['duration']))
                title.setCheckState(Qt.CheckState.Unchecked)
                music_list = [id, title, artist, duration]
                for column, values in enumerate(music_list):
                    self.fav_table.setItem(rows, column, values)
    
    def delete_account(self):
        connect, connect4 = self.database.connect_database(), self.database.connect_database()
        music_list = self.database.get_user_music_info(connect, self.id)
        user_response = tkinter.messagebox.askyesno(title='Rythmix', message='Are you sure you want to delete account?')
        
        if user_response:
            for songs in music_list:
                connect2, connect3 = self.database.connect_database(), self.database.connect_database()
                self.database.remove_to_favorites(connect2, self.id, songs['id'])
                self.database.delete_music(connect3, self.id, songs['title'])
            
            login_page.remove_user(self.id)
            self.database.delete_account_database(connect4, self.id)
            mixer.init()
            mixer.music.stop()
            self.search_line.clear()
            self.play_volume.setValue(99)
            self.fav_volume.setValue(99)
            self.search_volume.setValue(99)
            self.fav_title.setText('NO MUSIC PLAYING')
            self.play_title.setText('NO MUSIC PLAYING')
            self.search_title.setText('NO MUSIC PLAYING')
            self.database.set_username_password("", "", "")
        
            widget.setCurrentWidget(login_page)
        else:
            widget.setCurrentWidget(user_page)
    
    def sign_out(self):
        user_response = tkinter.messagebox.askyesno(title='Rythmix', message='Are you sure you want to sign out?')
        if user_response:
            mixer.init()
            mixer.music.stop()
            self.search_line.clear()
            self.fav_title.setText('NO MUSIC PLAYING')
            self.play_title.setText('NO MUSIC PLAYING')
            self.search_title.setText('NO MUSIC PLAYING')   
            self.play_volume.setValue(99)
            self.fav_volume.setValue(99)
            self.search_volume.setValue(99)
            self.import_table.setRowCount(0)
            self.play_table.setRowCount(0)
            self.fav_table.setRowCount(0)
            self.search_table.setRowCount(0)
            self.database.set_username_password("", "", "")
            
            widget.setCurrentWidget(login_page)
       
class EditMusicFrame(QDialog, edit_music_frame):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.selected_music = ""
        self.file_location = ""
        self.destination = ""
        self.setupUi(self)
        
        self.edit_back_button.clicked.connect(self.go_to_main_frame)
        self.edit_select_file.clicked.connect(self.select_file)
        self.edit_confirm_button.clicked.connect(self.confirm_edit_music)
    
    def go_to_main_frame(self):
        widget.setCurrentWidget(user_page)
    
    def refresh(self):
        self.username, self.password, self.id = self.database.get_username_password()
    
    def select_file(self):
        tkinter.Tk().withdraw()
        self.file_location = tkinter.filedialog.askopenfilename()
        self.destination = os.getcwd()
        self.edit_select_file_line.setText(self.file_location)
        
    def confirm_edit_music(self):
        connect, connect2, connect3 = self.database.connect_database(), self.database.connect_database(), self.database.connect_database()
        file = self.file_location.split('/')
        file_name = file[len(file)-1]
        duration_pattern = '[0-9]{2}:[0-9]{2}:[0-9]{2}'
        check_duration = re.findall(duration_pattern, self.edit_duration_line.text())
        error = False
        
        if len(check_duration) != 1:
            tkinter.messagebox.showerror(title='Input Error', message="Input Duration Invalid")
            error = True
        elif self.edit_music_title_line.text() == "":
            tkinter.messagebox.showerror(title='Input Error', message="Title Input Error")
            error = True
            
        if not error:
            self.database.edit_music(connect2, self.edit_music_title_line.text(), self.edit_artist_line.text(), self.edit_duration_line.text(), file_name, self.selected_music)
            self.database.edit_fav_music(connect3, self.edit_music_title_line.text(), self.edit_artist_line.text(), self.edit_duration_line.text(), file_name, self.selected_music)
            try: 
                move = shutil.move(self.file_location, self.destination)
                move
            except:
                tkinter.messagebox.showwarning(title='File Already Exist', message='File Already exists in Directory')
        
        self.edit_music_title_line.clear()
        self.edit_artist_line.clear()
        self.edit_duration_line.clear()
        self.edit_select_file_line.clear()
        self.file_location = ""
        self.destination = ""
        user_page.update_import_table()
        user_page.update_playlist_table()
        user_page.update_fav_table()
        user_page.update_search_table()
        widget.setCurrentWidget(user_page)
    
    def get_selected_music(self, id:str):
        self.selected_music = id
    
class ImportMusicFrame(QDialog, music_import_frame):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.database = database
        
        self.import_back_button.clicked.connect(self.go_to_main_frame)
        self.select_file_button.clicked.connect(self.import_select_file)
        self.import_confirm_button.clicked.connect(self.save_imported_music)

    def refresh(self):
        self.username, self.password, self.id = self.database.get_username_password()
        
    def go_to_main_frame(self):
        widget.setCurrentWidget(user_page)
    
    def import_select_file(self):
        tkinter.Tk().withdraw()
        self.file_location = tkinter.filedialog.askopenfilename()
        self.destination = os.getcwd()
        self.select_file_line.setText(self.file_location)
        
    
    def save_imported_music(self):
        connect, connect2 = self.database.connect_database(), self.database.connect_database()
        user_playlist = self.database.get_user_music_info(connect, self.id)
        file = self.file_location.split('/')
        file_name = file[len(file)-1]
        duration_pattern = '[0-9]{2}:[0-9]{2}:[0-9]{2}'
        check_duration = re.findall(duration_pattern, self.import_duration_line.text())
        error = False
        
        for music in user_playlist:
            if music['title'] == self.import_title_line.text():
                tkinter.messagebox.showerror(title='Error', message='Title is already in your playlist')
                error = True
                break
        
        if len(check_duration) > 1 or len(check_duration) < 1:
            tkinter.messagebox.showerror(title='Input Error', message="Input Duration Invalid")
            error = True
        elif self.import_title_line.text() == "":
            tkinter.messagebox.showerror(title='Input Error', message="Title Input Error")
            error = True
            
        if not error:
            self.database.save_music(connect2, self.import_title_line.text(), self.import_artist_line.text(), self.import_duration_line.text(), file_name, self.id)
            try: 
                move = shutil.move(self.file_location, self.destination)
                move
            except:
                tkinter.messagebox.showwarning(title='File Already Exist', message='File Already exists in Directory')
            
        self.import_title_line.clear()
        self.import_artist_line.clear()
        self.import_duration_line.clear()
        self.select_file_line.clear()
        self.file_location = ""
        self.destination = ""
        user_page.update_import_table()
        user_page.update_playlist_table()
        user_page.update_search_table()
        user_page.update_fav_table()
        widget.setCurrentWidget(user_page)
        
class EditAccountFrame(QDialog, edit_account_frame):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setupUi(self)
    
        self.edit_acc_back.clicked.connect(self.go_to_main_frame)
        self.edit_acc_confirm.clicked.connect(self.edit_account)
    
    def go_to_main_frame(self):
        widget.setCurrentWidget(user_page)
    
    def edit_account(self):
        connect, connect2 = self.database.connect_database(), self.database.connect_database()
        username, password, id = self.database.get_username_password()
        users = self.database.get_user_info(connect) #list of dicts
        error = False
        if self.edit_username_line.text() == username and self.edit_password_line.text() == password:
            for accs in users:
                if accs['username'] == self.new_username_line.text():
                    tkinter.messagebox.showerror(title='Invalid Input', message='Username is already used')
                    error = True
                    break
            
            if len(self.new_password_line.text()) <= 8:
                tkinter.messagebox.showerror(title='Invalid Input', message='Password must be 8 characters or more')                
                error = True
            
            if not error:
                self.database.edit_account_database(connect2, self.new_username_line.text(), self.new_password_line.text(), id)
                self.database.set_username_password(self.new_username_line.text(), self.new_password_line.text(), id)
                login_page.edit_user(id, self.new_username_line.text(), self.new_password_line.text())
                tkinter.messagebox.showinfo(title='Rythmix', message='Account Successfully edited')
        else:
            tkinter.messagebox.showerror(title="Invalid Input", message='Invalid Username or Password')
        
        self.edit_username_line.clear()
        self.edit_password_line.clear()
        self.new_username_line.clear()
        self.new_password_line.clear()
        
        widget.setCurrentWidget(user_page)
                 
app = QApplication(sys.argv)
widget = QStackedWidget()
parent = database()
login_page = LoginFrame(parent)
create_page = CreateAccount(parent)
user_page = MainFrame(parent)
edit_music_page = EditMusicFrame(parent)
import_music_page = ImportMusicFrame(parent)
edit_account_page = EditAccountFrame(parent)
widget.addWidget(login_page)
widget.addWidget(create_page)
widget.addWidget(user_page)
widget.addWidget(edit_music_page)
widget.addWidget(import_music_page)
widget.addWidget(edit_account_page)

widget.show()

app.exec()
