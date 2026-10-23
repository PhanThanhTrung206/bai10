
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QVBoxLayout
)


class FormThongTin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vi du widget co ban")
        self.resize(320, 250)

        # O nhap ho ten
        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("Nhap ho ten...")

        # Danh sach chon thanh pho
        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems(
            ["Ha Noi", "Da Nang", "TP.HCM", "Hue"]
        )

        # Nut xac nhan va nhan ket qua
        nut_xac_nhan = QPushButton("Xac nhan")
        self.nhan_ket_qua = QLabel("")

        # Tao layout doc
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ho ten:"))
        layout.addWidget(self.o_nhap_ten)
        layout.addWidget(QLabel("Thanh pho:"))
        layout.addWidget(self.chon_thanh_pho)
        layout.addWidget(nut_xac_nhan)
        layout.addWidget(self.nhan_ket_qua)

        self.setLayout(layout)

        # Xu ly su kien bam nut
        nut_xac_nhan.clicked.connect(self.xac_nhan)

    def xac_nhan(self):
        ho_ten = self.o_nhap_ten.text()
        thanh_pho = self.chon_thanh_pho.currentText()

        if ho_ten.strip() == "":
            self.nhan_ket_qua.setText("Vui long nhap ho ten!")
        else:
            self.nhan_ket_qua.setText(
                f"Ho ten: {ho_ten}\nThanh pho: {thanh_pho}"
            )


app = QApplication(sys.argv)
cua_so = FormThongTin()
cua_so.show()
sys.exit(app.exec_())
