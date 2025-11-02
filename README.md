# Java Runtime Manager (JRM)
## Description
A lightweight Python tool to manage Java installations, because SDKMAN doesn't exist on Windows.

## Features
- Detects and sets multiple Java vendors (Oracle, Adoptium, Zulu)
- Updates `JAVA_HOME` automatically
- Cleans old Java entries from system and user PATHs.
- No additional packages needed

## Requirements
- Windows
- Python 3.x
- Administrator privileges to update system variables

## Installation & Usage
1. Clone the repository:
    ```bat
    git clone https://github.com/Meolsei/Java-Runtime-Manager.git
    cd Java-Runtime-Manager
    ```
2. Run the script as an administrator:
    ```bat
    python main.py
    ```
3. Follow the prompts:
    ```text
    Input Java Version: (8, 11, 17, 21, 25)
    Input Java Vendor: (Adoptium, Oracle, Zulu)
    ```

The script will update `JAVA_HOME` and `PATH` automatically.

## Testing
- For PowerShell, run the following command:
    ```ps1
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")
    java -version
    ```
- For Command Prompt, run the following command:
    ```bat
    # Command Prompt
    set PATH=%PATH%;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem
    java -version
    ```

## Notes
- This script only works on Windows. Unix users can use SDKMAN:
    ```bash
    curl -s "https://get.sdkman.io" | bash
    ```
- No 3rd party packages needed

## Contributing
- Feel free to submit bug reports or feature requests
- PRs are welcome

## License
This project is licensed under the MIT License, which permits you to freely use or modify it, granted the notice is included in any copy made.
