from binaryninja.plugin import BackgroundTaskThread, PluginCommand

class SampleInBackground(BackgroundTaskThread):
    def __init__(self, bv, msg):
        BackgroundTaskThread.__init__(self, msg, True)
        self.bv = bv

    def run(self):
        pass

def sample_in_background(bv):
    bg_task = SampleInBackground(bv, "Executing sample plugin")
    bg_task.start()

PluginCommand.register("Sample Plugin", "This plugin demonstrates a basic Binary Ninja plugin structure.", sample_in_background)