# get OS type https://stackoverflow.com/questions/7330187/how-to-find-the-windows-version-from-the-powershell-command-line/7330368
# fix for powershell script not digitally signed - https://caiomsouza.medium.com/fix-for-powershell-script-not-digitally-signed-69f0ed518715


# [System.Environment]::OSVersion.Version
# systeminfo /fo csv | ConvertFrom-Csv | select OS*, System*, Hotfix* | Format-List

#$path = "HKCU:\Software\Yahm\Tests"
#New-Item –Path $path –Name MyKey
#New-ItemProperty -Path $path\MyKey -Name "MyValue" -Value 0 -PropertyType "DWORD"

Set-Variable -Name "test" -Value (systeminfo | findstr /B /C:"OS Name")
#systeminfo | findstr /B /C:"OS Name"
return $test
