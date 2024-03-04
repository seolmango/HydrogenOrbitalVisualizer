import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QComboBox, QLabel, QPushButton, QHBoxLayout, QSlider
from PyQt5.QtGui import QIcon
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from Orbital import Orbital
from WaveFunction import FIRST_BOHR_RADIUS
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap
cmap = pl.cm.plasma
my_cmap = cmap(np.arange(cmap.N))
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)
my_cmap = ListedColormap(my_cmap)


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        self.axes = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)
        self.orbital = Orbital(1, 's', 'none')

    def orbit_update(self, n, shape, direction, precision):
        self.orbital.change_wave(n, shape, direction)
        self.draw_wave(scale=n, precision=precision)

    def draw_wave(self, scale, precision):
        result = []
        limit = (-6 * FIRST_BOHR_RADIUS * scale, 6 * FIRST_BOHR_RADIUS * scale)
        x = np.linspace(-6 * FIRST_BOHR_RADIUS * scale, 6 * FIRST_BOHR_RADIUS * scale, precision)
        y = np.linspace(-6 * FIRST_BOHR_RADIUS * scale, 6 * FIRST_BOHR_RADIUS * scale, precision)
        z = np.linspace(-6 * FIRST_BOHR_RADIUS * scale, 6 * FIRST_BOHR_RADIUS * scale, precision)

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
        X = np.array(X)
        Y = np.array(Y)
        Z = np.array(Z)
        result = np.array(result)
        result = result / result.sum()

        valid = np.where(result > 0.1 * result.mean())
        X = X[valid]
        Y = Y[valid]
        Z = Z[valid]
        result = result[valid]

        self.axes.clear()
        self.axes.set(xlim3d=limit, ylim3d=limit, zlim3d=limit, box_aspect=(1,1,1))
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
        self.n_combo.addItems(["1", "2", "3", "4"])
        self.l_combo = QComboBox()
        self.l_combo.addItems(["s"])
        def l_combo_reset():
            self.l_combo.clear()
            if self.n_combo.currentText() == "1":
                self.l_combo.addItems(["s"])
            elif self.n_combo.currentText() == "2":
                self.l_combo.addItems(["s", "p"])
            elif self.n_combo.currentText() == "3":
                self.l_combo.addItems(["s", "p", "d"])
            elif self.n_combo.currentText() == "4":
                self.l_combo.addItems(["s", "p", "d", "f"])
        self.m_combo = QComboBox()
        self.m_combo.addItems(["none"])
        def m_combo_reset():
            self.m_combo.clear()
            if self.l_combo.currentText() == "s":
                self.m_combo.addItems(["none"])
            elif self.l_combo.currentText() == "p":
                self.m_combo.addItems(["x", "y", "z"])
            elif self.l_combo.currentText() == "d":
                self.m_combo.addItems(["z^2", "xz", "yz", "xy", "x^2-y^2"])
            elif self.l_combo.currentText() == "f":
                self.m_combo.addItems(["z^3", "xz^2", "yz^2", "xyz", "z(x^2-y^2)", "x(x^2-3y^2)", "y(3x^2-y^2)"])
        self.n_combo.currentIndexChanged.connect(l_combo_reset)
        self.l_combo.currentIndexChanged.connect(m_combo_reset)
        nml_layout.addWidget(QLabel("n(주양자수):"))
        nml_layout.addWidget(self.n_combo)
        nml_layout.addWidget(QLabel("l(부양자수):"))
        nml_layout.addWidget(self.l_combo)
        nml_layout.addWidget(QLabel("orientation(배향):"))
        nml_layout.addWidget(self.m_combo)
        redraw_button = QPushButton("Redraw")
        def redraw():
            redraw_button.setEnabled(False)
            self.sc.orbit_update(int(self.n_combo.currentText()), self.l_combo.currentText(), self.m_combo.currentText(), self.scale_slider.value())
            redraw_button.setEnabled(True)
        redraw_button.clicked.connect(redraw)
        nml_layout.addWidget(redraw_button)

        slider_layout = QHBoxLayout()
        self.scale_slider = QSlider()
        self.scale_slider.setRange(10, 50)
        self.scale_slider.setValue(20)
        self.scale_slider.setOrientation(1)
        scale_label = QLabel("Precision(정밀도):")
        value_label = QLabel(str(self.scale_slider.value()))
        slider_layout.addWidget(scale_label)
        slider_layout.addWidget(self.scale_slider)
        slider_layout.addWidget(value_label)

        def scale_change():
            value_label.setText(str(self.scale_slider.value()))

        self.scale_slider.valueChanged.connect(scale_change)

        layout = QVBoxLayout()
        layout.addLayout(nml_layout)
        layout.addLayout(slider_layout)
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        self.setLayout(layout)
        self.setWindowTitle("Hydrogen Orbital Visualizer")
        self.setWindowIcon(QIcon('icon.png'))
        self.sc.orbit_update(int(self.n_combo.currentText()), self.l_combo.currentText(), self.m_combo.currentText(), self.scale_slider.value())
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())