#$FileOrFolderPath=D:\projects\ardom-1\sql_functions\testdatabase.db

IF((Test-Path -Path $FileOrFolderPath) -eq $false) { 
    Write-Warning "File or directory does not exist."        
} 
Else { 
    $LockingProcess = CMD /C "openfiles /query /fo table | find /I ""$FileOrFolderPath""" 
    Write-Host $LockingProcess 
}