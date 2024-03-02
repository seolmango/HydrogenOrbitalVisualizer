import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QComboBox, QLabel, QPushButton, QHBoxLayout
import matplotlib
from mpl_toolkits.mplot3d import Axes3D  # 3D 그래프를 위한 모듈 추가
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from Orbital import Orbital
from WaveFunction import FIRST_BOHR_RADIUS
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap
cmap = pl.cm.viridis
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)
my_cmap = ListedColormap(my_cmap)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)
        self.orbital = Orbital(1, 's', 'none')

    def orbit_update(self, n, shape, direction):
        self.orbital.change_wave(n, shape, direction)
        self.draw_wave(scale=n)

    def draw_wave(self, scale):
        result = []
        x = np.linspace(-5 * FIRST_BOHR_RADIUS * scale, 5 * FIRST_BOHR_RADIUS * scale, 20)
        y = np.linspace(-5 * FIRST_BOHR_RADIUS * scale, 5 * FIRST_BOHR_RADIUS * scale, 20)
        z = np.linspace(-5 * FIRST_BOHR_RADIUS * scale, 5 * FIRST_BOHR_RADIUS * scale, 20)

        X = []
        Y = []
        Z = []
        for i in range(len(x)):
            for j in range(len(y)):
                for k in range(len(z)):
                    r = np.sqrt(x[i]**2 + y[j]**2 + z[k]**2)
                    theta = np.arccos(z[k] / r)
                    phi = np.arctan2(y[j], x[i])
                    percent = self.orbital.wave(r, theta, phi)**2
                    result.append(percent)
                    X.append(x[i])
                    Y.append(y[j])
                    Z.append(z[k])


        self.axes.clear()
        self.axes.scatter(X, Y, Z, c=result, cmap=my_cmap)
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.axes.set_zlabel('Z')
        self.draw()

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.sc = MplCanvas()
        toolbar = NavigationToolbar(self.sc, self)

        nml_layout = QHBoxLayout()
        self.n_combo = QComboBox()
        self.n_combo.addItems(["1", "2"])
        self.l_combo = QComboBox()
        self.l_combo.addItems(["s"])
        def l_combo_reset():
            self.l_combo.clear()
            if self.n_combo.currentText() == "1":
                self.l_combo.addItems(["s"])
            elif self.n_combo.currentText() == "2":
                self.l_combo.addItems(["s", "p"])
        self.m_combo = QComboBox()
        self.m_combo.addItems(["none"])
        def m_combo_reset():
            self.m_combo.clear()
            if self.l_combo.currentText() == "s":
                self.m_combo.addItems(["none"])
            elif self.l_combo.currentText() == "p":
                self.m_combo.addItems(["x", "y", "z"])
        self.n_combo.currentIndexChanged.connect(l_combo_reset)
        self.l_combo.currentIndexChanged.connect(m_combo_reset)
        nml_layout.addWidget(QLabel("n:"))
        nml_layout.addWidget(self.n_combo)
        nml_layout.addWidget(QLabel("l:"))
        nml_layout.addWidget(self.l_combo)
        nml_layout.addWidget(QLabel("ori:"))
        nml_layout.addWidget(self.m_combo)
        redraw_button = QPushButton("Redraw")
        def redraw():
            redraw_button.setEnabled(False)
            self.sc.orbit_update(int(self.n_combo.currentText()), self.l_combo.currentText(), self.m_combo.currentText())
            redraw_button.setEnabled(True)
        redraw_button.clicked.connect(redraw)
        nml_layout.addWidget(redraw_button)

        layout = QVBoxLayout()
        layout.addLayout(nml_layout)
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        self.setLayout(layout)
        self.setWindowTitle("Orbital Viewer")
        self.sc.orbit_update(int(self.n_combo.currentText()), self.l_combo.currentText(), self.m_combo.currentText())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())