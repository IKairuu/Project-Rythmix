import mysql.connector 
from mysql.connector import errorcode as err
import os

class MusicManagerDatabase():  
    def __init__(self):
        self._user_name = ""
        self._password = ""
        self._user_id = ""
        
    def set_username_password(self, username:str, password:str, id:str):
        self._user_name = username
        self._password = password
        self._user_id = id
    
    def get_username_password(self):
        return self._user_name, self._password, self._user_id
    
    def connect_database(self):
        try:
            db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "music_manager",
            password = "guyguy23CV"
            )
            return db
        except mysql.connector.Error as error:
            if error.errno == err.ER_ACCESS_DENIED_ERROR:
                return 'Username or Password are Incorrect'
            elif error.errno == err.ER_BAD_DB_ERROR:
                return 'Database Not Found'
            else:
                return err
    
    def get_user_info(self, db):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM users')
            user_list = cursor.fetchall()
            user_dict = [{'id': users[0], 'username':users[1], 'user_password':users[2]} for users in user_list]
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            return user_dict
    
    def sign_in(self, db, username:str, password:str):
        try:
            cursor = db.cursor()
            cursor.execute('INSERT INTO users (username, user_password) VALUES (%s, %s)', (username, password))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def save_music(self, db, title:str, artist:str, duration:str, file_name, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('INSERT INTO playlist (title, artist, duration, file_name, user_id) VALUES (%s, %s, %s, %s, %s)', (title, artist, duration, file_name, user_id))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def get_user_music_info(self, db, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM playlist WHERE user_id = %s', (user_id, ))
            music_list = cursor.fetchall()
            
            music_dict = [{'id':music[0], 'title':music[1], 'artist':music[2], 'duration':music[3], 'file_name':music[4], 'user_id':music[5],} for music in music_list]
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            return music_dict
    
    def delete_music(self, db, user_id:str, title:str):
        try:
            cursor = db.cursor()
            cursor.execute('DELETE FROM playlist WHERE title=%s AND user_id=%s', (title, user_id))

            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def play_music(self, db, title:str, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT file_name FROM playlist WHERE title=%s AND user_id=%s', (title,user_id))
            file = cursor.fetchone()
            song = file[0]
            db.commit() 
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            return song
    
    def search_music(self, db, title_artist:str):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM playlist WHERE title=%s OR artist=%s', (title_artist, ))
            music_list = cursor.fetchall()
            music_dict = [{'id':music[0], 'title':music[1], 'artist':music[2], 'duration':music[3], 'file_name':music[4], 'user_id':music[5],} for music in music_list]
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            return music_dict
    
    def edit_music(self, db, title:str, artist:str, duration:str, filename, song_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('UPDATE playlist SET title=%s, artist=%s, duration=%s, file_name=%s WHERE id=%s', (title, artist, duration, filename, song_id))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            
    def edit_fav_music(self, db, title:str, artist:str, duration:str, filename, song_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('UPDATE favorites SET title=%s, artist=%s, duration=%s, file_name=%s WHERE music_id=%s', (title, artist, duration, filename, song_id))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def add_favorite(self, db, music_id:str, title:str, artist:str, duration:str, filename:str, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('INSERT INTO favorites (music_id, title, artist, duration, file_name, user_id) VALUES (%s, %s, %s, %s, %s, %s)', (music_id, title, artist, duration, filename, user_id))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def get_fav_music(self, db, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM favorites WHERE user_id = %s', (user_id, ))
            music_list = cursor.fetchall()
            
            music_dict = [{'id':music[0], 'title':music[1], 'artist':music[2], 'duration':music[3], 'file_name':music[4], 'user_id':music[5],} for music in music_list]
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            return music_dict
    
    def remove_to_favorites(self, db, user_id:str, music_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('DELETE FROM favorites WHERE music_id=%s AND user_id=%s', (music_id, user_id))
            
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def delete_account_database(self, db, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('DELETE FROM users WHERE id=%s', (user_id, ))
            
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
    
    def edit_account_database(self, db, username:str, password:str, user_id:str):
        try:
            cursor = db.cursor()
            cursor.execute('UPDATE users SET username=%s, user_password=%s WHERE id=%s', (username, password, user_id))
            db.commit()
        except mysql.connector.Error as error:
            print(error)
        else:
            cursor.close()
            db.close()
            