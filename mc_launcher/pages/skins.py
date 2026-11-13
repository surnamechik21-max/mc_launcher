# pages/skins.py — Скины и плащи (2D-превью)
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
    QPushButton, QFrame,
)
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen
from widgets import Card, SectionTitle, DimLabel


class SkinPreview(QFrame):
    """Простой 2D-персонаж, нарисованный в paintEvent."""
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 340)
        self.setStyleSheet("background: rgba(13,17,23,0.5); border-radius: 14px;")

    def paintEvent(self, event):
        super().paintEvent(event)
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        cx = self.width() // 2
        top = 30

        # Голова
        head = QRect(cx - 45, top, 90, 90)
        p.setBrush(QBrush(QColor("#C89B7B")))
        p.setPen(QPen(QColor("#0B0F14"), 2))
        p.drawRoundedRect(head, 10, 10)

        # Волосы
        p.setBrush(QBrush(QColor("#3B2A1E")))
        p.drawRect(cx - 45, top, 90, 24)

        # Глаза
        p.setBrush(QBrush(QColor("#10B981")))
        p.setPen(Qt.PenStyle.NoPen)
        p.drawEllipse(cx - 24, top + 42, 14, 14)
        p.drawEllipse(cx + 10, top + 42, 14, 14)

        # Тело (футболка)
        body = QRect(cx - 55, top + 100, 110, 130)
        p.setBrush(QBrush(QColor("#10B981")))
        p.setPen(QPen(QColor("#0B0F14"), 2))
        p.drawRoundedRect(body, 12, 12)

        # Руки
        p.setBrush(QBrush(QColor("#C89B7B")))
        p.drawRoundedRect(QRect(cx - 90, top + 100, 30, 110), 8, 8)
        p.drawRoundedRect(QRect(cx + 60, top + 100, 30, 110), 8, 8)

        # Ноги
        p.setBrush(QBrush(QColor("#1F2937")))
        p.drawRoundedRect(QRect(cx - 45, top + 230, 38, 100), 8, 8)
        p.drawRoundedRect(QRect(cx + 7,  top + 230, 38, 100), 8, 8)

        p.end()


class SkinsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        # Превью
        left = Card()
        left.layout().addWidget(QLabel("Предпросмотр"))
        left.layout().addWidget(SkinPreview(), 1)
        layout.addWidget(left, 3)

        # Панель управления
        right = Card()
        right.layout().addWidget(QLabel("Скин и плащ"))

        right.layout().addWidget(DimLabel("Модель:"))
        model = QComboBox()
        model.addItems(["Steve (классика)", "Alex (тонкая)"])
        right.layout().addWidget(model)

        right.layout().addSpacing(12)

        upload = QPushButton("📤  Загрузить скин (.png)")
        upload.setCursor(Qt.CursorShape.PointingHandCursor)
        right.layout().addWidget(upload)

        cape = QPushButton("🧥  Выбрать плащ")
        cape.setCursor(Qt.CursorShape.PointingHandCursor)
        right.layout().addWidget(cape)

        right.layout().addSpacing(12)
        right.layout().addWidget(DimLabel("Формат: PNG 64×64 или 64×32"))
        right.layout().addStretch()

        layout.addWidget(right, 2)