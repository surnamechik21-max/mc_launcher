# pages/settings.py — Настройки лаунчера
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSlider, QSpinBox, QCheckBox, QScrollArea,
)
from PyQt6.QtCore import Qt
from widgets import Card, SectionTitle, DimLabel


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(16)

        outer.addWidget(SectionTitle("Настройки"))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        host = QWidget()
        layout = QVBoxLayout(host)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        # ---------- ОЗУ ----------
        ram = Card()
        ram.layout().addWidget(QLabel("Выделение ОЗУ"))
        self.ram_label = DimLabel("8 ГБ · рекомендовано 6–8 ГБ")
        ram.layout().addWidget(self.ram_label)

        self.ram_slider = QSlider(Qt.Orientation.Horizontal)
        self.ram_slider.setMinimum(2)
        self.ram_slider.setMaximum(16)
        self.ram_slider.setValue(8)
        self.ram_slider.setTickInterval(1)
        self.ram_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.ram_slider.valueChanged.connect(
            lambda v: self.ram_label.setText(
                f"{v} ГБ · рекомендовано 6–8 ГБ"
            )
        )
        ram.layout().addWidget(self.ram_slider)
        layout.addWidget(ram)

        # ---------- Установка ----------
        install = Card()
        install.layout().addWidget(QLabel("Установка игры"))

        install.layout().addLayout(self._path_row(
            "Папка игры", "%APPDATA%/.minecraft", "Обзор…"
        ))
        install.layout().addLayout(self._path_row(
            "Java Runtime", "C:/Program Files/Java/jdk-21/bin/java.exe",
            "Автоподбор"
        ))
        layout.addWidget(install)

        # ---------- Окно игры ----------
        window = Card()
        window.layout().addWidget(QLabel("Окно игры"))

        res_row = QHBoxLayout()
        res_row.addWidget(QLabel("Разрешение:"))
        self.w_input = QSpinBox()
        self.w_input.setRange(640, 7680)
        self.w_input.setValue(1280)
        res_row.addWidget(self.w_input)
        res_row.addWidget(QLabel("×"))
        self.h_input = QSpinBox()
        self.h_input.setRange(480, 4320)
        self.h_input.setValue(720)
        res_row.addWidget(self.h_input)
        res_row.addStretch()
        window.layout().addLayout(res_row)

        window.layout().addWidget(DimLabel("JVM-аргументы:"))
        jvm = QLineEdit("-XX:+UseG1GC -XX:+ParallelRefProcEnabled")
        window.layout().addWidget(jvm)
        layout.addWidget(window)

        # ---------- Лаунчер ----------
        launcher = Card()
        launcher.layout().addWidget(QLabel("Лаунчер"))
        for text, checked in [
            ("Закрывать лаунчер при запуске игры", True),
            ("Проверять обновления при старте",    True),
            ("Показывать снапшоты",                False),
        ]:
            cb = QCheckBox(text)
            cb.setChecked(checked)
            launcher.layout().addWidget(cb)
        layout.addWidget(launcher)

        layout.addStretch()
        scroll.setWidget(host)
        outer.addWidget(scroll, 1)

    def _path_row(self, label: str, value: str, button: str) -> QHBoxLayout:
        row = QHBoxLayout()
        lbl = QLabel(label)
        lbl.setFixedWidth(120)
        row.addWidget(lbl)

        field = QLineEdit(value)
        row.addWidget(field, 1)

        btn = QPushButton(button)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        row.addWidget(btn)
        return row