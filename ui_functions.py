from .estimate import Main
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
from .delineate import model
from .delineate import estimate
from .delineate import control
from .delineate import utility
import dendropy
from .delineateestimate import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class UIFunctions(Main):

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


    def download1(self):
        try:
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
                    truncated_tree_file_size=10,
                    underflow_protection=False)

        except Exception:
            QMessageBox.warning(self, "Warning", "The delimitation is failed")
            return

        QMessageBox.information(self, "Information", "The output generated successfully")


    def cmb(self):
        print(self.comboBox.currentText())


    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
