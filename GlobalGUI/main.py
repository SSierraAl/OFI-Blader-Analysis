# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

from random import randint

import pyqtgraph as pg
import sys
from PySide6.QtCore import QTimer
import subprocess as sp
from Arduino_Plot import *
from insert_laser_graph import *
from weight_analysis import *
from threadweight import *
from plot import *
from Thread_Arduino import *

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QIcon

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)


        # ZABER CONECTION
        # ///////////////////////////////////////////////////////////////
        #try:
         #   print('------- Init Zaber -------')
          #  InitializeZaber(self)
        #except:
         #   print('------- Error Zaber Connection -------')
          #  self.ui.load_pages.n_devices_p3.setText("0 Devices")


        # DAQ CONECTION
        # ///////////////////////////////////////////////////////////////
        #SetDAQParams(self)
        #InsertLaserGraphs2(self)
        #insert_Laser_graph(self)
        #InitializeDaq(self)
        
        #self.colores=pl.GraphTest()
        #self.colores.number=100
        
        #self.ui.load_pages.LayoutLaser.addWidget(self.colores)


        # FlLUIGENT CONECTION
        # ///////////////////////////////////////////////////////////////
        #try:
         #   InitFluigent_Sensor(self)
          #  print("------- Init Fluigent -------")
        #except:
         #   print("------- Error Fluigent Connection -------")


        # global bandera
        # global extProc
        # bandera=True
        # def Zkeyboard():
        #     global bandera
        #     global extProc
            
        #     if bandera:
        #         extProc = sp.Popen(['python','ZaberKeyboard.py']) # runs myPyScript.py 
        #         status = sp.Popen.poll(extProc) # status should be 'None'
        #         print(status)
        #         bandera=False
        #     else:
        #         sp.Popen.terminate(extProc) # closes the process
        #         status = sp.Popen.poll(extProc) 
        #         print(status)
        #         bandera=True

        # self.ui.load_pages.Keyboard_p3.clicked.connect(Zkeyboard)
        
        
        #self.data_Arduino=fs.data_arduino(self)        
        
        # ///////////////////////////////////////////////////////////////
        self.contasas=1
        self.cont_weight=1

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

        #print("delete that")

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()


        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu0 
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.Maintenance)
            #self.timerArduino.stop()
            #self.timerDAQ.stop()
            #self.timerPLOT.start()
            #self.timerWait.stop()
            #self.timer.start()
            #self.timerDaq.stop()
            #self.timer2Daq.stop()
        
        # Widget colors
        if btn.objectName() == "btn_colors":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page)
            if(self.contasas == 1):
                
                init_ports(self)
                self.contasas=0


        # Widget weight
        if btn.objectName() == "btn_search":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_calib)
            
            if(self.cont_weight == 1):
                self.cont_weight=0
                init_plot(self)


        # WIDGETS BTN
        if btn.objectName() == "btn_widgets":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.Maintenance)
            #self.timerArduino.stop()
            #self.timerDAQ.stop()
            self.timerPLOT.stop()
            #self.timerWait.stop()
            #self.timer.stop()
            #self.timer2.stop()
            #self.timerDaq.start()
            #self.timer2Daq.start()


    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        #print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())