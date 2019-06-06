import subprocess


class Process:
    p = None
    exit_code = None

    def __init__(self, command):
        self.command = command

    def run(self):
        p = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            ret = p.poll()
            line = p.stdout.readline()
            yield line
            if ret is not None:
                self.exit_code = ret
                break
