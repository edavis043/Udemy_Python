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


app = pw.QApplication(sys.argv)
front = MainWindow()
front.show()
front.load_data()
sys.exit(app.exec())
