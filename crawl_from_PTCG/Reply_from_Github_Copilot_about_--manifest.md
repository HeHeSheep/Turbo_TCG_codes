要在Python腳本中請求管理員權限，你可以使用`ctypes`模塊。但是，當你將Python腳本打包成可執行文件時，你需要使用一個清單文件來請求管理員權限。

以下是一個步驟指南：

1. 創建一個名為`YourAppName.exe.manifest`的清單文件（將`YourAppName`替換為你的應用程序的名稱）。清單文件的內容應為：

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity version="1.0.0.0" name="YourAppName"/>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```

2. 當你使用PyInstaller將Python腳本打包成可執行文件時，你需要包含清單文件。你可以通過使用`--manifest`選項，後面跟著你的清單文件的路徑來實現這一點：

```bash
pyinstaller --onefile --manifest YourAppName.exe.manifest YourAppName.py
```

這將創建一個在運行時請求管理員權限的可執行文件。用戶將看到一個用戶帳戶控制（UAC）提示，要求他們允許以管理員權限運行應用程序。
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To request administrative privileges in a Python script, you can use the `ctypes` module. However, when you package your Python script into an executable file, you need to use a manifest file to request the administrative privileges.

Here is a step-by-step guide:

1. Create a manifest file with the name `YourAppName.exe.manifest` (replace `YourAppName` with the name of your application). The content of the manifest file should be:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity version="1.0.0.0" name="YourAppName"/>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```

2. When you package your Python script into an executable file using PyInstaller, you need to include the manifest file. You can do this by using the `--manifest` option followed by the path to your manifest file:

```bash
pyinstaller --onefile --manifest YourAppName.exe.manifest YourAppName.py
```

This will create an executable file that requests administrative privileges when it is run. The user will see a User Account Control (UAC) prompt asking for permission to run the application with administrative privileges.