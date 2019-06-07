import subprocess


class Process:
    p = None
    exit_code = None

    def __init__(self, command):
        self.command = command

    def start_process(self):
        p = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            ret = p.poll()
            line = p.stdout.readline()
            yield line
            if ret is not None:
                self.exit_code = ret
                break

    # pass command as string
    # outputs output to stdio and returns process exit code
    def run(self):
        print(f'CMD_EXECUTING: {self.command}')
        for line in self.start_process():
            line = line.rstrip()
            if line:
                print(line.decode('utf-8'))
        print(f'CMD_EXIT_CODE: {self.exit_code}')
        return self.exit_code
