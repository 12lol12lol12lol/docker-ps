#!/usr/bin/env python3
import subprocess

ID_LENGTH = 20
NAME_LENGTH = 60
STATUS_LENGTH = 10

if __name__ == '__main__':
    result_str = ''
    CSI="\x1B["
    res = subprocess.getstatusoutput("docker ps -a --format '{{.ID}}@{{.Names}}@{{.Status}}@'")
    status, values = res[0], res[1]
    if not status:
        args = values.split('@')
        temp = [iter(args)] * 3
        values = zip(*temp)
        for value in values:
            docker_id, docker_name ,lower_status = value[0].strip(), value[1].strip(), value[2].lower()
            if lower_status.startswith('up'):
                #  If OK green
                result_str += CSI+"32;40m" + f'{docker_id.ljust(ID_LENGTH)} {docker_name.ljust(NAME_LENGTH)} {lower_status.ljust(STATUS_LENGTH)}' + CSI + "0m"
            elif lower_status.startswith('exited'):
                # If Exited red
                result_str += CSI+"31;40m" + f'{docker_id.ljust(ID_LENGTH)} {docker_name.ljust(NAME_LENGTH)} {lower_status.ljust(STATUS_LENGTH)}' + CSI + "0m"
            else:
                result_str += CSI+"33;40m" + f'{docker_id.ljust(ID_LENGTH)} {docker_name.ljust(NAME_LENGTH)} {lower_status.ljust(STATUS_LENGTH)}' + CSI + "0m"
            result_str += '\n'
    else:
        result_str = values
    print(result_str)
