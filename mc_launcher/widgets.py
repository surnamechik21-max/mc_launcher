# widgets.py — переиспользуемые компоненты интерфейса
from PyQt6.QtWidgets import (
    QFrame, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
)
from PyQt6.QtCore import Qt


class Card(QFrame):
    """Полупрозрачная карточка с внутренним layout."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(6)

    def layout(self):
        return self._layout


class Badge(QLabel):
    """Цветной бейдж статуса."""
    def __init__(self, text: str, color: str = "#10B981"):
        super().__init__(text)
        self.setStyleSheet(
            f"color: {color}; background: rgba(16,185,129,0.14);"
            f"border-radius: 8px; padding: 3px 10px; font-size: 11px;"
        )


class SectionTitle(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("title")


class DimLabel(QLabel):
    def __init__(self, text: str = ""):
        super().__init__(text)
        self.setObjectName("dim")
        self.setWordWrap(True)


class StatRow(QWidget):
    """Строка 'иконка + заголовок + подпись'."""
    def __init__(self, icon: str, title: str, subtitle: str = ""):
        super().__init__()
        h = QHBoxLayout(self)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(10)

        ico = QLabel(icon)
        ico.setStyleSheet("font-size: 22px;")
        ico.setFixedWidth(30)
        h.addWidget(ico)

        col = QVBoxLayout()
        col.setSpacing(2)
        t = QLabel(title)
        t.setStyleSheet("font-weight: 600; font-size: 14px;")
        col.addWidget(t)
        if subtitle:
            col.addWidget(DimLabel(subtitle))
        h.addLayout(col)
        h.addStretch()


class ModRow(QWidget):
    """Строка мода: название + версия + переключатель."""
    def __init__(self, name: str, version: str, enabled: bool = True):
        super().__init__()
        h = QHBoxLayout(self)
        h.setContentsMargins(0, 6, 0, 6)

        col = QVBoxLayout()
        col.setSpacing(2)
        n = QLabel(name)
        n.setStyleSheet("font-weight: 600; font-size: 13px;")
        v = QLabel(f"v{version}")
        v.setObjectName("dim")
        col.addWidget(n)
        col.addWidget(v)
        h.addLayout(col)
        h.addStretch()

        from PyQt6.QtWidgets import QCheckBox
        cb = QCheckBox()
        cb.setChecked(enabled)
        h.addWidget(cb)


class InstanceCard(Card):
    """Карточка сборки Minecraft."""
    def __init__(self, name: str, version: str, loader: str, icon: str = "🧱"):
        super().__init__()
        self.setFixedSize(220, 150)
        self.layout().setSpacing(4)

        ico = QLabel(icon)
        ico.setStyleSheet("font-size: 36px; color: #10B981;")
        self.layout().addWidget(ico)

        title = QLabel(name)
        title.setStyleSheet("font-weight: 600; font-size: 14px;")
        title.setWordWrap(True)
        self.layout().addWidget(title)

        self.layout().addWidget(DimLabel(f"Minecraft {version} · {loader}"))
        self.layout().addStretch()

        play = QPushButton("▶  Играть")
        play.setStyleSheet(
            "background: rgba(16,185,129,0.22); color: #10B981;"
            "border: 1px solid rgba(16,185,129,0.4);"
            "border-radius: 8px; padding: 6px 10px; font-size: 12px;"
        )
        play.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout().addWidget(play)