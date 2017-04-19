import os
import re
import traceback
import logging
import platform
from distutils.version import StrictVersion

from P4 import P4, P4Exception, Progress, OutputHandler

import perforce.DCCInterop
import perforce.Utils as Utils
import PerforceMenu

# try:
#     AppUtils.closeWindow(ui.perforceMenu)
# except:
#     ui = None

def init():
    global ui
    # try:
    #     # cmds.deleteUI(ui.perforceMenu)
    #     AppUtils.closeWindow(ui.perforceMenu)
    # except:
    #     pass

    p4 = P4()
    if p4.p4config_file == 'noconfig':
        Utils.loadP4Config(p4)

    # DCCInterop.initCallbacks()

    try:
        ui = PerforceMenu.MainShelf(p4)

        ui.addMenu()
    except ValueError as e:
        Utils.p4Logger().critical(e)

    # mu.executeDeferred('ui.addMenu()')


def close():
    global ui

    # DCCInterop.cleanupCallbacks()

    # try:
    #     # cmds.deleteUI(ui.perforceMenu)
    #     AppUtils.closeWindow(ui.perforceMenu)
    # except Exception as e:
    #     raise e

    ui.close()

    #del ui