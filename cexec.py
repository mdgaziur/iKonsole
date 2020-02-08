from commands_list import IKONSOLE_CMD_BUILTIN

for cmd in IKONSOLE_CMD_BUILTIN:
    exec('from commands.' + cmd + ' import ' + cmd)


def cexec(command, IKONSOLE_CMD_BUILTIN):
    func_name = command[0]
    print(func_name + '(command)')
    exec(func_name + '(command)')
