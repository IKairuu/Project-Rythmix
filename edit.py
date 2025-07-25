# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditMusic(object):
    def setupUi(self, EditMusic):
        EditMusic.setObjectName("EditMusic")
        EditMusic.resize(622, 371)
        EditMusic.setMinimumSize(QtCore.QSize(622, 371))
        EditMusic.setMaximumSize(QtCore.QSize(100000, 100000))
        EditMusic.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=EditMusic)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 110, 301, 142))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_music_title = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.edit_music_title.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_music_title.setObjectName("edit_music_title")
        self.gridLayout.addWidget(self.edit_music_title, 0, 0, 1, 1)
        self.edit_artist_line = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.edit_artist_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_artist_line.setObjectName("edit_artist_line")
        self.gridLayout.addWidget(self.edit_artist_line, 1, 1, 1, 1)
        self.edit_duration_line = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.edit_duration_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_duration_line.setObjectName("edit_duration_line")
        self.gridLayout.addWidget(self.edit_duration_line, 2, 1, 1, 1)
        self.edit_duration = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.edit_duration.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_duration.setObjectName("edit_duration")
        self.gridLayout.addWidget(self.edit_duration, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_back_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.edit_back_button.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_back_button.setObjectName("edit_back_button")
        self.horizontalLayout.addWidget(self.edit_back_button)
        self.edit_confirm_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.edit_confirm_button.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_confirm_button.setObjectName("edit_confirm_button")
        self.horizontalLayout.addWidget(self.edit_confirm_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.edit_music_title_line = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.edit_music_title_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_music_title_line.setObjectName("edit_music_title_line")
        self.gridLayout.addWidget(self.edit_music_title_line, 0, 1, 1, 1)
        self.edit_artist = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.edit_artist.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_artist.setObjectName("edit_artist")
        self.gridLayout.addWidget(self.edit_artist, 1, 0, 1, 1)
        self.edit_select_file = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.edit_select_file.setStyleSheet("background-color: rgb(20, 216, 92);")
        self.edit_select_file.setObjectName("edit_select_file")
        self.gridLayout.addWidget(self.edit_select_file, 3, 0, 1, 1)
        self.edit_select_file_line = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.edit_select_file_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edit_select_file_line.setObjectName("edit_select_file_line")
        self.gridLayout.addWidget(self.edit_select_file_line, 3, 1, 1, 1)

        self.retranslateUi(EditMusic)
        QtCore.QMetaObject.connectSlotsByName(EditMusic)

    def retranslateUi(self, EditMusic):
        _translate = QtCore.QCoreApplication.translate
        EditMusic.setWindowTitle(_translate("EditMusic", "EDIT MUSIC"))
        self.edit_music_title.setText(_translate("EditMusic", "Music Title"))
        self.edit_duration.setText(_translate("EditMusic", "Duration(MM:SS)"))
        self.edit_back_button.setText(_translate("EditMusic", "Back"))
        self.edit_confirm_button.setText(_translate("EditMusic", "Confirm"))
        self.edit_artist.setText(_translate("EditMusic", "Artist"))
        self.edit_select_file.setText(_translate("EditMusic", "Select File"))
