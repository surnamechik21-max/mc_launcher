# pages/home.py — Главная страница
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton,
)
from PyQt6.QtCore import Qt
from widgets import Card, SectionTitle, DimLabel, StatRow


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        # Заголовок
        layout.addWidget(SectionTitle("Главная"))

        # Аккаунт + статус серверов
        top = QHBoxLayout()
        top.setSpacing(16)

        acc = Card()
        acc.layout().addWidget(StatRow("👤", "Steve_Player", "Microsoft лицензия"))
        top.addWidget(acc, 1)

        status = Card()
        status.layout().addWidget(
            StatRow("🌐", "Статус серверов", "● Все сервисы работают")
        )
        top.addWidget(status, 1)
        layout.addLayout(top)

        # Новость
        news = Card()
        news.layout().addWidget(QLabel("📰  Обновление 1.21.4 уже доступно"))
        news.layout().addWidget(
            DimLabel("Скачайте новую версию игры из каталога сборок.")
        )
        layout.addWidget(news)

        layout.addStretch()

        # Нижняя панель: выбор версии + ИГРАТЬ
        bottom = Card()
        row = QHBoxLayout()
        row.setSpacing(12)

        version = QComboBox()
        version.addItems([
            "Vanilla 1.21.4",
            "Fabric 1.21.4",
            "Forge 1.20.1",
            "NeoForge 1.21.1",
            "Quilt 1.20.4",
        ])
        version.setFixedHeight(48)
        row.addWidget(version, 1)

        play = QPushButton("ИГРАТЬ")
        play.setObjectName("playButton")
        play.setFixedSize(260, 56)
        play.setCursor(Qt.CursorShape.PointingHandCursor)
        row.addWidget(play)

        bottom.layout().addLayout(row)
        layout.addWidget(bottom