#from .ui_diui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *
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
from delineateestimate import *
from PyQt5.uic import loadUiType
import time, datetime
import asyncio
from PyQt5.QtCore import QThread
#from asyncqt import (QEventLoop, QThreadExecutor)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

FORM_CLASS, _= loadUiType("diui.ui")

class MyAbstract(QThread):
    """Base export thread"""

    loop = asyncio.get_event_loop()
    def __init__(self, func, parent=None):
        super().__init__(parent)
        self.func= func


    def run(self):
        self.loop.run_until_complete(self.func())
        self.loop.close()




class Main(QDialog, FORM_CLASS):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.Handel_Buttons()
        self.setWindowIcon(QIcon("Delineate.ico"))
        self.setWindowTitle("Delineate")
        self.progressBar.setStyle(QStyleFactory.create("windows"))
        self.progressBar.setRange(0, 1)
        self.launcher= MyAbstract(self.download1)


        self.pushButton.setToolTip("This is population-level phylogeny tree")
        self.pushButton_4.setToolTip("DELINEATE analysis to explore all possible partitions that vary in the species assignments of these populations")
        self.pushButton_3.setToolTip("result entries (trees and partitions) are given in order of descending probability")
        self.lineEdit.setToolTip("Please choose nexus or newick file format")
        self.lineEdit_2.setToolTip("a priori species assignments for as many population lineages with three columns")
        self.lineEdit_3.setToolTip("partition listed in the JSON file, trees illustrate the different partitions")


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.browse_file1)
        self.pushButton_2.clicked.connect(self.browse_file2)
        self.pushButton_3.clicked.connect(self.browse_file3)
        self.pushButton_4.clicked.connect(self.download2)

        self.pushButton_5.clicked.connect(self.clear)
        self.comboBox.currentTextChanged.connect(self.cmb)


    def browse_file1(self):
        self.browse_file = QFileDialog.getOpenFileName(self, "browse file", directory=".",filter="All Files (*.*)")
        self.lineEdit.setText(QDir.toNativeSeparators(str(self.browse_file[0])))
        return self.browse_file[0]


    def browse_file2(self):
        self.browse_file = QFileDialog.getOpenFileName(self, "browse file", directory=".",filter="All Files (*.*)")
        self.lineEdit_2.setText(QDir.toNativeSeparators(str(self.browse_file[0])))
        return self.browse_file[0]


    def browse_file3(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.lineEdit_3.setText(QDir.toNativeSeparators(str(filenames[0])))

    # def apply(self):
    #     QApplication.processEvents()
    #


    def download2(self):

        def started():
            self.pushButton_4.setText('Please wait analysis is going on')
            self.progressBar.setRange(0, 0)


        def finished():
            self.progressBar.setRange(0, 1)
            self.pushButton_4.setText('Download')
            pass


        self.launcher.started.connect(started)
        self.launcher.finished.connect(finished)

        self.launcher.start()




    async def download1(self):
        # try:
        input_file1= self.lineEdit.text()
        input_file2= self.lineEdit_2.text()
        output_file= self.lineEdit_3.text()

        tree_format= self.comboBox.currentText()



        execute_species_partition_estimation(input_file1, input_file2, output_file,
                extra_info_field_value=None,
                figtree_display_label='species-lineage',
                no_primary_tree_file=False,
                no_translate_tree_tokens=False,
                preserve_underscores=True,
                report_constrained_cumulative_probability_threshold=0.95,
                report_constrained_probability_threshold=None,
                report_mle_only=False,
                speciation_completion_rate=None,
                speciation_completion_rate_estimation_initial=None,
                speciation_completion_rate_estimation_max=None,
                speciation_completion_rate_estimation_min=1e-08,
                store_relabeled_trees=None,
                tree_format= tree_format,
                tree_info=False,
                truncated_tree_file_size=10, funcs= None,
                underflow_protection=False)



        # except Exception as e:
        #     QMessageBox.warning(self, "Warning", f"The delimitation is failed because {e}")
        #     return
        #
        # QMessageBox.information(self, "Information", "The output generated successfully")


    def cmb(self):
        print(self.comboBox.currentText())


    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")



def main1():

    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':
    main1()
