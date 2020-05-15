import sys
import os
import PySide2
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtWidgets, QtGui
import random
import networkx
dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

def LogsTextEditOutput(textEdit,text="",newline=True,newNumber=True):
    if not hasattr(LogsTextEditOutput,"lineNumber"):
        LogsTextEditOutput.lineNumber=0

    textEditCursor = textEdit.textCursor()
    textEditCursor.movePosition(QtGui.QTextCursor.End)
    if newNumber:
        if newline:
            textEditCursor.insertText("["+str("{:>8}".format(LogsTextEditOutput.lineNumber))+"] "+text+"\n")
        else:
            textEditCursor.insertText(text)
    else:
        if newline:
            textEditCursor.insertText("["+str("{:>8}".format(LogsTextEditOutput.lineNumber))+"] "+text)
        else:
            textEditCursor.insertText(text)

    LogsTextEditOutput.lineNumber+=1
    textEdit.setTextCursor(textEditCursor)
    textEdit.ensureCursorVisible()
