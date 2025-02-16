[Setup]
AppName=DnD Translator
AppVersion=1.0
DefaultDirName={pf}\DnD Translator
DefaultGroupName=DnD Translator
OutputDir=.
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes
SetupIconFile=data\program_icon.ico

[Files]
Source: "requirements\dist\DnD_Translator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "python-3.13.2-amd64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall
Source: "venv\*"; DestDir: "{app}\venv"; Flags: ignoreversion recursesubdirs createallsubdirs

[Run]
Filename: "{tmp}\python-3.13.2-amd64.exe"; Parameters: "/quiet InstallAllUsers=1 PrependPath=1"; Flags: waituntilterminated
Filename: "{app}\python.exe"; Parameters: "-m venv venv"; Flags: waituntilterminated
Filename: "{app}\venv\Scripts\python.exe"; Parameters: "-m pip install --upgrade pip"; Flags: waituntilterminated
Filename: "{app}\venv\Scripts\python.exe"; Parameters: "-m pip install -r requirements.txt"; Flags: waituntilterminated

[Icons]
Name: "{group}\DnD Translator"; Filename: "{app}\DnD_Translator.exe"
