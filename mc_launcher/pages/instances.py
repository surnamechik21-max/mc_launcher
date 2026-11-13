# pages/instances.py — Сборки + управление модами
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea,
    QTabWidget, QPushButton, QFrame,
)
from widgets import Card, SectionTitle, DimLabel, ModRow, InstanceCard


class InstancesPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        layout.addWidget(SectionTitle("Сборки"))

        # Сетка сборок в скролле
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        grid_host = QWidget()
        grid = QHBoxLayout(grid_host)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(14)

        builds = [
            ("Fabulously Optimized", "1.21.4", "Fabric", "⚡"),
            ("Better MC",            "1.20.1", "Forge",  "🧱"),
            ("All the Mods 10",      "1.21.1", "NeoForge", "🌌"),
            ("RLCraft",              "1.12.2", "Forge",  "🐉"),
            ("Create: Astral",       "1.18.2", "Fabric", "⚙"),
            ("Vanilla",              "1.21.4", "Vanilla","🟩"),
        ]
        for name, ver, loader, icon in builds:
            grid.addWidget(InstanceCard(name, ver, loader, icon))
        grid.addStretch()

        scroll.setWidget(grid_host)
        layout.addWidget(scroll, 1)

        # Панель модов
        panel = Card()
        tabs = QTabWidget()

        mods_tab = QWidget()
        mods_layout = QVBoxLayout(mods_tab)
        mods_layout.setContentsMargins(0, 8, 0, 0)
        for name, ver, enabled in [
            ("Sodium",     "0.6.5",  True),
            ("Iris",       "1.8.0",  True),
            ("Lithium",    "0.14.3", True),
            ("Fabric API", "0.102.0", True),
            ("JEI",        "19.21",  False),
        ]:
            mods_layout.addWidget(ModRow(name, ver, enabled))
        mods_layout.addStretch()
        tabs.addTab(mods_tab, "Моды")

        for title in ("Ресурспаки", "Шейдеры", "Карты"):
            tabs.addTab(self._empty_tab(title), title)

        panel.layout().addWidget(tabs)

        # Кнопка «Обновить все»
        row = QHBoxLayout()
        row.addStretch()
        btn = QPushButton("⟳  Обновить все")
        row.addWidget(btn)
        panel.layout().addLayout(row)

        layout.addWidget(panel)

    def _empty_tab(self, title: str) -> QWidget:
        w = QWidget()
        v = QVBoxLayout(w)
        v.setContentsMargins(0, 12, 0, 0)
        v.addWidget(DimLabel(f"Здесь пока пусто — {title} не установлены."))
        v.addStretch()
        return w