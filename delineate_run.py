from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from delineateestimate import *
from PyQt5.uic import loadUiType
import time, datetime
import asyncio
from PyQt5.QtCore import QThread
import contextlib
import sys
import os
import argparse
import subprocess
import math
import itertools
import collections
import json
from dendropy.dataio import nexusprocessing
from dendropy.model import birthdeath
from delineate import model
from delineate import estimate
from delineate import control
from delineate import utility
import dendropy
from collections import defaultdict
from functools import partial
import tempfile
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5 import QtWebEngineWidgets

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

FORM_CLASS,_=loadUiType(resource_path("delineate_run.ui"))

def factory(arg):
    result= float(arg)
    return result

def_dict = defaultdict(partial(factory, 'default value'))
def_dict['None']=  None
def_dict['True']=  True
def_dict['False']=  False

class MyAbstract(QThread):
    """Base export thread"""
    done = pyqtSignal(object)
    fail = pyqtSignal(object)
    loop = asyncio.get_event_loop()

    def __init__(self, func, parent=None):
        super().__init__(parent)
        self.func= func

    def run(self):
        try:
            result= self.loop.run_until_complete(self.func())

        except Exception as exception:
            print(exception)
            self.fail.emit(exception)
        else:
            self.done.emit(result)

class Main(QDialog, FORM_CLASS):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(resource_path("Delineate.ico")))
        self.setWindowTitle("Delineate")
        self.progressBar.setStyle(QStyleFactory.create("windows"))
        self.progressBar.setRange(0, 1)
        self.launcher= MyAbstract(self.download2)
        self.box= QMessageBox()
        self.setWindowTitle("delineate")
        self.f= tempfile.TemporaryDirectory()
        self.gp.setVisible(False)
        self.reset_placement()
        self.filepath= defaultdict(lambda: None)
        self.outpath= defaultdict(lambda: None)
        self.toolButton_2.setEnabled(False)
        self.toolButton_3.setEnabled(False)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

        self.m2.setText('False')
        self.m3.setText('None')
        self.m4.setText('1e-08')
        self.m5.setText('None')
        self.m6.setText("0.95")
        self.m7.setText("False")
        self.m8.setText('None')
        self.m9.setText('10')
        self.Handel_Buttons()


    def Handel_Buttons(self):
        self.toolButton.clicked.connect(self.open_file1)
        self.toolButton_5.clicked.connect(self.open_file2)
        self.toolButton_2.clicked.connect(self.download3)
        self.toolButton_3.clicked.connect(self.save_all)
        self.toolButton_4.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.BtnHandler)
        self.listWidget.itemDoubleClicked.connect(self.Clicked)


    def open_file1(self):
        msg = 'Select the input rooted ultrametric population tree file\n'
        QMessageBox.information(self, 'Add input tree file', msg)
        sel = 'Select tree file'
        tree = self.file_dialog(sel, ".")
        if tree:
            self.filepath['file1']= tree



    def open_file2(self):
        msg = 'Select input species assignment constraint table'
        QMessageBox.information(self, 'Add input table file', msg)
        sel = 'Select table file'
        table = self.file_dialog(sel, ".")
        if table:
            self.filepath['file2']= table
        self.toolButton_2.setEnabled(True)


    def file_dialog(self, msg, path):
        return QFileDialog.getOpenFileName(self, msg, path)[0]


    async def download2(self):

        self.toolButton_2.setEnabled(True)
        self.toolButton_3.setEnabled(True)
        m1= self.comboBox.currentText()
        m2= def_dict[self.m2.text()]
        m3= self.m3.text()
        def_dict.default_factory = partial(factory, m3)
        m3= def_dict[self.m3.text()]
        if m3: m3= float(m3)

        m4= float(self.m4.text())
        m5= self.m5.text()
        def_dict.default_factory = partial(factory, m5)
        m5= def_dict[self.m5.text()]
        if m5: m5= float(m5)

        m8= self.m8.text()
        def_dict.default_factory = partial(factory, m8)
        m8= def_dict[self.m8.text()]
        if m8: m8= float(m8)

        m6= float(self.m6.text())
        m7= def_dict[self.m7.text()]
        m9= int(self.m9.text())
        tmpfname=self.filepath['file1']
        _, filename= os.path.split(tmpfname)
        filename= filename.split(".")[0]
        output= self.f.name
        self.outpath['output']= output

        self.unique= str(int(time.time()))
        save_file = output
        execute_species_partition_estimation(self.filepath['file1'], self.filepath['file2'], self.outpath['output'],
                extra_info_field_value=None,
                figtree_display_label='species-lineage',
                no_primary_tree_file=False,
                no_translate_tree_tokens=False,
                preserve_underscores=True,
                report_constrained_cumulative_probability_threshold=m6,
                report_constrained_probability_threshold=m8,
                report_mle_only=m7,
                speciation_completion_rate=None,
                speciation_completion_rate_estimation_initial=m5,
                speciation_completion_rate_estimation_max=m3,
                speciation_completion_rate_estimation_min=m4,
                store_relabeled_trees=None,
                tree_format= m1,
                tree_info=False,
                truncated_tree_file_size=m9, funcs= None,
                underflow_protection=m2)
        onlyfiles = [self.listWidget.addItem(f) for f in os.listdir(save_file) if os.path.isfile(os.path.join(save_file, f))]


    def save_all(self):
        try:
            msg = 'Please browse to output folder to save all files'
            QMessageBox.information(self, 'Browse output folder', msg)
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.Directory)
            if dlg.exec_():
                filenames = dlg.selectedFiles()
                filename= QDir.toNativeSeparators(str(filenames[0]))
            import shutil
            file_names = os.listdir(self.outpath['output'])

            for file_name in file_names:
                shutil.copy(os.path.join(self.outpath['output'], file_name), filename)
        except Exception as e:

            QMessageBox.warning(self, "Warning", f"The output  is not saved because {e}")


    def clear(self):
        self.toolButton_2.setEnabled(False)
        self.toolButton_3.setEnabled(False)

        self.m2.setText('False')
        self.m3.setText('None')
        self.m4.setText('1e-08')
        self.m5.setText('None')
        self.m6.setText("0.95")
        self.m7.setText("False")
        self.m8.setText('None')
        self.m9.setText('10')
        self.listWidget.clear()
        import os, shutil
        folder = self.f.name
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                QMessageBox.warning(self, "Warning", 'Failed to delete %s. Reason: %s' % (file_path, e))


    def BtnHandler(self):
        if self.pushButton.isChecked():
            self.gp.setVisible(True)

        else:
            self.gp.setVisible(False)
            self.reset_placement()


    def reset_placement(self):
        g = QDesktopWidget().availableGeometry()
        self.resize(0.1 * g.width(), 0.4 * g.height())
        self.move(g.center().x() - self.width() / 2, g.center().y() - self.height() / 2)

    @pyqtSlot()
    def download3(self):
        def fail(exception):
            
            QMessageBox.warning(self, "Warning", f"The output not obtained, please check input file and parameters and error is {exception}")
            pass

        def done(result):
            QMessageBox.information(self, "Information", "The output data generated successfully")


        def started():
            self.progressBar.setRange(0, 0)


        def finished():
            self.progressBar.setRange(0, 1)
            pass


        self.launcher.started.connect(started)
        self.launcher.finished.connect(finished)
        self.launcher.done.connect(done)
        self.launcher.fail.connect(fail)
        self.launcher.start()


    def Clicked(self, item2):
        try:

            self.w= AnotherWindow()
            name= item2.text()
            self.w.setWindowIcon(QIcon(resource_path(os.path.join("icon", "delineate.ico"))))
            f = open(os.path.join(self.outpath['output'], name), "rt")
            mytext1 = QGraphicsSimpleTextItem(f.read())
            self.w.scene.addItem(mytext1)
            f.close()
            self.w.layout.addWidget(self.w.graph1)
            self.w.setLayout(self.w.layout)

            self.w.setWindowTitle("delineate")
            self.w.show()
        except Exception as e:
            QMessageBox.warning(self, "Warning", f"The view  is not obtained because {e}")


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.graph1= QGraphicsView()
        self.scene = QGraphicsScene()
        self.graph1.setScene(self.scene)
        self.m_output = QtWebEngineWidgets.QWebEngineView()


def main1():

    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':
    main1()
