# pages/catalog.py — Каталог модов (Modrinth/CurseForge)
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QComboBox, QScrollArea, QPushButton,
)
from PyQt6.QtCore import Qt
from widgets import Card, SectionTitle, DimLabel


class CatalogPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        layout.addWidget(SectionTitle("Каталог модов"))

        # Фильтры
        filters = QHBoxLayout()
        filters.setSpacing(12)

        search = QLineEdit()
        search.setPlaceholderText("🔍  Поиск по Modrinth / CurseForge…")
        search.setFixedHeight(42)
        filters.addWidget(search, 3)

        version = QComboBox()
        version.addItems(["1.21.4", "1.21.1", "1.20.1", "1.19.2", "1.18.2"])
        version.setFixedHeight(42)
        filters.addWidget(version, 1)

        loader = QComboBox()
        loader.addItems(["Fabric", "Forge", "NeoForge", "Quilt"])
        loader.setFixedHeight(42)
        filters.addWidget(loader, 1)

        category = QComboBox()
        category.addItems(["Все категории", "Оптимизация", "Технологии",
                           "Магия", "Приключения", "Строительство"])
        category.setFixedHeight(42)
        filters.addWidget(category, 1)

        layout.addLayout(filters)

        # Сетка модов
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        host = QWidget()
        grid = QHBoxLayout(host)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(14)

        mods = [
            ("Sodium",        "Оптимизация рендера",  "12.4M"),
            ("Iris Shaders",  "Поддержка шейдеров",   "8.1M"),
            ("JEI",           "Просмотр рецептов",    "6.9M"),
            ("Create",        "Технологии и механизмы","5.2M"),
            ("Botania",       "Магия и цветы",        "3.8M"),
            ("Twilight Forest","Приключения",         "2.7M"),
        ]
        for name, desc, downloads in mods:
            grid.addWidget(self._mod_card(name, desc, downloads))
        grid.addStretch()

        scroll.setWidget(host)
        layout.addWidget(scroll, 1)

    def _mod_card(self, name: str, desc: str, downloads: str) -> Card:
        card = Card()
        card.setFixedWidth(260)

        title = QLabel(name)
        title.setStyleSheet("font-weight: 600; font-size: 14px;")
        card.layout().addWidget(title)

        card.layout().addWidget(DimLabel(desc))

        meta = QLabel(f"⬇ {downloads}")
        meta.setObjectName("dim")
        card.layout().addWidget(meta)

        btn = QPushButton("Установить")
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        card.layout().addWidget(btn)

        return card