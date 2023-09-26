import PyQt6.QtWidgets as pw
import PyQt6.QtGui as pg
import sys
import sqlite3


class MainWindow(pw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management App")

        file_menu_item = self.menuBar().addMenu("&File")
        add_student_action = pg.QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        help_menu_item = self.menuBar().addMenu("&Help")
        about_action = pg.QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = pw.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, pw.QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog
        dialog.exec()


class InsertDialog(pw.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Data Insertion")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = pw.QVBoxLayout()

        self.student_name = pw.QLineEdit()  # Add Name
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = pw.QComboBox()  # Add Combobox of courses
        courses = ["Biology", "Maths", "Astro.", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile = pw.QLineEdit()  # Add Mobile Widget
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = pw.QPushButton("Register")
        button.clicked().connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUE (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()


app = pw.QApplication(sys.argv)
front = MainWindow()
front.show()
front.load_data()
sys.exit(app.exec())
