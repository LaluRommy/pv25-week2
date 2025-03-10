from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QHBoxLayout, QVBoxLayout
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Registrasi")
        self.setGeometry(100, 100, 400, 200)
        
        navLayout = QHBoxLayout()
        profilLayout = QVBoxLayout()
        layout = QGridLayout()
        
        #Navigasi
        self.homeButton = QPushButton("Home")
        self.contactButton = QPushButton("Contact")
        self.aboutButton = QPushButton("About")
        navLayout.addWidget(self.homeButton)
        navLayout.addWidget(self.contactButton)
        navLayout.addWidget(self.aboutButton)
        
        #Profil
        self.namaLabel = QLabel("Nama : Lalu Rommy")
        self.nimLabel = QLabel("NIM : F1D022058")
        self.kelasLabel = QLabel("Kelas : C")
        profilLayout.addWidget(self.namaLabel)
        profilLayout.addWidget(self.nimLabel)
        profilLayout.addWidget(self.kelasLabel)
        
        # Nama Depan
        self.first_name_label = QLabel("Nama Depan:")
        self.first_name_input = QLineEdit()
        layout.addWidget(self.first_name_label, 0, 0)
        layout.addWidget(self.first_name_input, 0, 1)

        # Nama Belakang
        self.last_name_label = QLabel("Nama Belakang:")
        self.last_name_input = QLineEdit()
        layout.addWidget(self.last_name_label, 0, 2)
        layout.addWidget(self.last_name_input, 0, 3)

        # Email
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label, 1, 0)
        layout.addWidget(self.email_input, 1, 1, 1, 3)

        # Password
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        layout.addWidget(self.password_label, 2, 0)
        layout.addWidget(self.password_input, 2, 1, 1, 3)

        # Konfirmasi Password
        self.confirm_password_label = QLabel("Konfirmasi Password:")
        self.confirm_password_input = QLineEdit()
        layout.addWidget(self.confirm_password_label, 3, 0)
        layout.addWidget(self.confirm_password_input, 3, 1, 1, 3)

        # Tombol Submit
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button, 4, 1, 1, 2)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(navLayout)
        mainLayout.addLayout(profilLayout)
        mainLayout.addLayout(layout)
        
        self.setLayout(mainLayout)

    def submit_form(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not (first_name and last_name and email and password and confirm_password):
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Peringatan", "Password tidak cocok!")
            return

        QMessageBox.information(self, "Sukses", "Registrasi berhasil!")

if __name__ == "__main__":
    app = QApplication([])
    window = RegistrationForm()
    window.show()
    app.exec_()
