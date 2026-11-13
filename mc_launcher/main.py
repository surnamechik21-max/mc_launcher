# main.py — точка входа Emerald Launcher
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget, QFrame, QButtonGroup,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from styles import STYLESHEET
from pages.home import HomePage
from pages.instances import InstancesPage
from pages.catalog import CatalogPage
from pages.skins import SkinsPage
from pages.settings import SettingsPage


class NavButton(QPushButton):
    """Кнопка бокового меню с активным состоянием."""
    def __init__(self, text: str, icon: str = ""):
        super().__init__(f"{icon}   {text}" if icon else text)
        self.setObjectName("navButton")
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(44)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Emerald Launcher")
        self.resize(1280, 820)
        self.setMinimumSize(1100, 720)

        # Корневой контейнер
        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)

        outer = QHBoxLayout(root)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(16)

        # ---------- Сайдбар ----------
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)
        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(14, 20, 14, 20)
        side_layout.setSpacing(6)

        logo = QLabel("◆  Emerald")
        logo.setObjectName("logo")
        side_layout.addWidget(logo)
        side_layout.addSpacing(10)

        # Кнопки навигации
        self.nav_buttons = []
        nav_items = [
            ("Главная",        "🏠", 0),
            ("Сборки",         "📦", 1),
            ("Каталог модов",  "🧩", 2),
            ("Скины и плащи",  "🎨", 3),
            ("Настройки",      "⚙",  4),
        ]
        self.btn_group = QButtonGroup(self)
        self.btn_group.setExclusive(True)

        for text, icon, index in nav_items:
            btn = NavButton(text, icon)
            btn.clicked.connect(lambda _, i=index: self.switch_page(i))
            self.btn_group.addButton(btn, index)
            side_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        side_layout.addStretch()

        # Профиль внизу
        profile = QLabel("👤  Steve_Player\n     ● Лицензия")
        profile.setObjectName("profile")
        side_layout.addWidget(profile)

        outer.addWidget(sidebar)

        # ---------- Контент ----------
        self.stack = QStackedWidget()
        self.stack.setObjectName("content")
        self.stack.addWidget(HomePage())
        self.stack.addWidget(InstancesPage())
        self.stack.addWidget(CatalogPage())
        self.stack.addWidget(SkinsPage())
        self.stack.addWidget(SettingsPage())
        outer.addWidget(self.stack, 1)

        # Стартовая страница
        self.nav_buttons[0].setChecked(True)
        self.switch_page(0)

    def switch_page(self, index: int):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Emerald Launcher")
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
