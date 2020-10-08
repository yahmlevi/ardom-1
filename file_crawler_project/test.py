import os 
import ctypes
from ctypes import *
from ctypes import wintypes


path = b'D:\\projects\\ardom-1\\test_c.c'
winlib = ctypes.CDLL('C:\Windows\System32\kernel32.dll')


size = wintypes.DWORD()
#print(winlib.GetCompressedFileSizeW(path, ctypes.byref(size)))
#print(winlib.GetCompressedFileSizeW(path))


SectorsPerCluster = wintypes.DWORD()
BytesPerSector = wintypes.DWORD()
NumberOfFreeClusters = wintypes.DWORD()
TotalNumberOfClusters = wintypes.DWORD()
bool_return = winlib.GetDiskFreeSpaceW(path, ctypes.byref(SectorsPerCluster),
                                ctypes.byref(BytesPerSector), ctypes.byref(NumberOfFreeClusters), ctypes.byref(TotalNumberOfClusters))
print(bool_return)
print(BytesPerSector)
print(SectorsPerCluster)
#print('test')
print(winlib.GetLastError())




#print(windll.kernel32.GetCompressedFileSizeW(path))
#print(windll.kernel32.GetCompressedFileSizeW('D:\projects\ardom-1\file_crawler_project\hello_world.exe'))
#print(windll.kernel32.GetDiskFreeSpaceW('D:\projects\ardom-1\file_crawler_project\hello_world.exe'))

