# styles.py — тёмная тема лаунчера (QSS)

STYLESHEET = """
/* ---------- Общий фон ---------- */
QWidget#root {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #0B0F14, stop:0.5 #0E1520, stop:1 #0B1A1A);
}

/* ---------- Сайдбар ---------- */
QFrame#sidebar {
    background: rgba(22, 27, 34, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
}

QLabel#logo {
    color: #10B981;
    font-size: 18px;
    font-weight: 700;
    padding-left: 8px;
}

QLabel#profile {
    color: #8B949E;
    font-size: 12px;
    padding: 8px;
    line-height: 1.6;
}

/* ---------- Навигация ---------- */
QPushButton#navButton {
    background: transparent;
    color: #8B949E;
    border: none;
    border-radius: 10px;
    padding: 10px 14px;
    text-align: left;
    font-size: 14px;
}
QPushButton#navButton:hover {
    background: rgba(255, 255, 255, 0.06);
}
QPushButton#navButton:checked {
    background: rgba(16, 185, 129, 0.18);
    color: #10B981;
    font-weight: 600;
}

/* ---------- Карточки ---------- */
QFrame#card {
    background: rgba(30, 36, 45, 0.66);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
}

QLabel {
    color: #E6EDF3;
}

QLabel#dim {
    color: #8B949E;
    font-size: 11px;
}

QLabel#accent {
    color: #10B981;
}

QLabel#title {
    font-size: 26px;
    font-weight: 700;
}

QLabel#subtitle {
    font-size: 14px;
    color: #8B949E;
}

/* ---------- Кнопка ИГРАТЬ ---------- */
QPushButton#playButton {
    background: #10B981;
    color: #04110C;
    border: none;
    border-radius: 14px;
    font-size: 22px;
    font-weight: 800;
    padding: 12px 24px;
}
QPushButton#playButton:hover {
    background: #34D399;
}
QPushButton#playButton:pressed {
    background: #0EA371;
}

/* ---------- Обычная кнопка ---------- */
QPushButton {
    background: rgba(255, 255, 255, 0.07);
    color: #E6EDF3;
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 10px;
    padding: 8px 16px;
    font-size: 13px;
}
QPushButton:hover {
    background: rgba(16, 185, 129, 0.22);
    border-color: rgba(16, 185, 129, 0.5);
}

/* ---------- Поля ввода ---------- */
QLineEdit, QComboBox, QSpinBox {
    background: rgba(13, 17, 23, 0.8);
    color: #E6EDF3;
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 10px;
    padding: 8px 12px;
    font-size: 13px;
}
QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border-color: #10B981;
}
QComboBox::drop-down {
    border: none;
    width: 24px;
}
QComboBox QAbstractItemView {
    background: #161B22;
    color: #E6EDF3;
    selection-background-color: rgba(16, 185, 129, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* ---------- Чекбоксы ---------- */
QCheckBox {
    color: #E6EDF3;
    font-size: 13px;
    spacing: 10px;
}
QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(13, 17, 23, 0.8);
}
QCheckBox::indicator:checked {
    background: #10B981;
    border-color: #10B981;
}

/* ---------- Слайдер ---------- */
QSlider::groove:horizontal {
    height: 6px;
    background: rgba(255, 255, 255, 0.10);
    border-radius: 3px;
}
QSlider::handle:horizontal {
    width: 18px;
    height: 18px;
    margin: -7px 0;
    background: #10B981;
    border-radius: 9px;
}
QSlider::sub-page:horizontal {
    background: #10B981;
    border-radius: 3px;
}

/* ---------- Табы ---------- */
QTabWidget::pane {
    border: none;
    background: transparent;
}
QTabBar::tab {
    background: transparent;
    color: #8B949E;
    padding: 8px 16px;
    border-radius: 8px;
    margin-right: 4px;
}
QTabBar::tab:selected {
    background: rgba(16, 185, 129, 0.18);
    color: #10B981;
}
QTabBar::tab:hover {
    background: rgba(255, 255, 255, 0.06);
}

/* ---------- Скролл ---------- */
QScrollArea {
    border: none;
    background: transparent;
}
QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 0;
}
QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background: rgba(16, 185, 129, 0.5);
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}
"""
