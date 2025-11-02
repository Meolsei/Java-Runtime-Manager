import subprocess
import os
import ctypes

if os.name.lower() != 'nt':
    print('This only works on Windows.\nI recommend SDKMAN for Linux/macOS.')
    exit(1)


def isAdmin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def setJavaHome(javaVersion, vendor, vendors):
    sysPath = [env for env in os.environ['PATH'].split(
        os.pathsep) if 'jre' not in env and 'jdk' not in env]

    usrPath = [p for p in subprocess.check_output(['powershell', '-Command', '[Environment]::GetEnvironmentVariable("PATH", "User")']
                                                  ).decode('utf-8').split(os.pathsep) if 'jre' not in p.lower() and 'jdk' not in p.lower()]

    for type_ in ('jre', 'jdk'):
        path = vendors[vendor].format(version=javaVersion, type=type_)

        if os.path.exists(path):
            sysPath = [path] + sysPath
            usrPath = [path] + usrPath

            print(f"Setting JAVA_HOME to {path}...")

            subprocess.run(
                ['powershell', '-Command',
                 f'New-ItemProperty -Path "HKLM:SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" -Name JAVA_HOME -Value "{path}" -PropertyType String -Force'],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            subprocess.run([
                'powershell', '-Command',
                f'New-ItemProperty -Path "HKLM:SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" -Name PATH -Value "{os.pathsep.join(sysPath)}" -PropertyType String -Force'],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            subprocess.run([
                'powershell', '-Command',
                f'[Environment]::SetEnvironmentVariable("PATH", "{os.pathsep.join(usrPath)}", "User")'
            ])

            return True

    return False


if isAdmin():
    javaVersions = {
        '8', '11', '17', '21', '25'
    }

    vendors = {
        'Oracle': 'C:/Program Files/Java/{type}-{version}',
        'Adoptium': 'C:/Program Files/Eclipse Adoptium/{type}-{version}',
        'Zulu': 'C:/Program Files/Zulu/zulu-{version}-{type}'
    }

    while True:
        javaVersion = input('Input Java Version: ')
        if javaVersion in javaVersions:
            break
        else:
            print(f'Invalid version.\n{", ".join(javaVersions)}')

    while True:
        vendor = input('Input Java Vendor: ')
        if vendor in vendors:
            break
        else:
            print(f'Invalid vendor.\n{", ".join(vendors.keys())}')

    setJavaHome(javaVersion, vendor, vendors)

else:
    print('Please run as an administrator.')
