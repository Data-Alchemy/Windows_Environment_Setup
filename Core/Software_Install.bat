@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
choco install openssh
choco install mobaxterm
choco install wsl
choco install fiddler
choco install googlechrome
choco install lastpass-chrome
choco install notepadplusplus
choco install tabular-editor
choco install python --version=3.9.0
choco install pycharm-community
choco install daxstudio
choco install powerbi
choco install visualstudio2019professional
choco install vscode
choco install dbeaver
choco install visualstudio2019-workload-azure
choco install ssms
choco install azure-cli
choco install gitkraken
