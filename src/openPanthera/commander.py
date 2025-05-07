"""
Command manager logic
"""
#!/usr/bin/python3
import hnyconfig as config
import openPanthera.containers as c
import openPanthera.display as ui
import openPanthera.schema as s
import openPanthera.modules as m

config.init('mariadb.conf.json')
schemas_list = m.read()





def _shortResolve(command:str)->int:
    """
    short command resolver

    :param: str:
    :return: int:
    """
    schema = s.VirtualSchema('', ui)
    shorters = c.short_specific_commands
    out = 0
    if command[0] in c.short_commands.keys():
        main = c.short_commands[command[0]]
        if command[1] in shorters[main].keys():
            sub = shorters[main][command[1]]
            if sub != 'clean-build':
                return schema.resolv(main, sub)
            for sub_sub in c.clean_build_types:
                result = schema.resolv(main, sub_sub)
                if result > out:
                    out = int(result+0)
    return 3

def _split(command:str)->list[str]:
    """
    command splitter

    :param:str:
    :return:list[str]
    """
    if len(command) > 2:
        return command.split(" ")
    return command

def resolve(command:str):
    """
    command resolver and cleaner

    :param:str:
    :return:int:
    """
    if command in ["h", "help"]:
        return helpCommand()
    clean_command = _split(command)
    if clean_command[0] == 'x' and clean_command[1] == 'x':
        clean_command = 'bx'
    if len(clean_command) == 2:
        return _shortResolve(clean_command)
    return 3

def helpCommand()->int:
    """
    help command

    :return:int:
    """
    shorters = c.short_specific_commands
    out = ''
    for command in c.short_commands.keys():
        for specific in shorters[c.short_commands[command]].keys():
            out += (
                command+
                specific+
                ' '+
                c.short_commands[command]+
                ' '+
                shorters[c.short_commands[command]][specific]+
                '\n'
            )
    ui.log(out)
    return 0
