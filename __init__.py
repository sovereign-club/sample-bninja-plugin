"""
Sample plugin for Binary Ninja that demonstrates how to run a task in the background.
"""

from binaryninja.plugin import BackgroundTaskThread, PluginCommand

class SampleInBackground(BackgroundTaskThread):
    """import 
    A class to execute a background task within Binary Ninja.
    """

    def __init__(self, bv, msg):
        """
        Initialize the background task with the given BinaryView and message.
        """
        BackgroundTaskThread.__init__(self, msg, True)
        self.bv = bv

    def run(self):
        """
        Method to execute the background task.
        """
        pass

def sample_in_background(bv):
    """
    Function to start the background task in Binary Ninja.
    """
    bg_task = SampleInBackground(bv, "Executing sample plugin")
    bg_task.start()

PluginCommand.register(
    "eshard",
    "This plugin demonstrates a basic Binary Ninja plugin structure.",
    sample_in_background
)
