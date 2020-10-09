import ctypes
from ctypes import wintypes


path = u'D:\\projects\\ardom-1\\file_crawler_project\\insert_to_excel.py'
winlib = ctypes.CDLL('C:\Windows\System32\kernel32.dll')

hosize = wintypes.DWORD()
losize = winlib.GetCompressedFileSizeW(path, ctypes.byref(hosize))
size = hosize.value << 32 | losize 

print('GetCompressedFileSizeW hosize - {}' .format(hosize.value))
print('GetCompressedFileSizeW losize - {}' .format(losize))
print('size - {}' .format(size))


path_dir = u'D:\\'

sectorsPerCluster = wintypes.DWORD()
bytesPerSector = wintypes.DWORD()
NumberOfFreeClusters = wintypes.DWORD()
TotalNumberOfClusters = wintypes.DWORD()

# https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getcompressedfilesizew

# https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdiskfreespacew
bool_return = winlib.GetDiskFreeSpaceW(None, 
                                ctypes.byref(sectorsPerCluster),
                                ctypes.byref(bytesPerSector), 
                                ctypes.byref(NumberOfFreeClusters),
                                ctypes.byref(TotalNumberOfClusters))


clusterSize = sectorsPerCluster.value * bytesPerSector.value

#print('need to return nonzero - {}' .format(bool_return))
print('sectorsPerCluster - {}' .format(sectorsPerCluster.value))
print('bytesPerSector - {}' .format(bytesPerSector.value))

print(NumberOfFreeClusters.value)
print('clusterSize - {}' .format(clusterSize))
print('error - {}' .format(winlib.GetLastError()))

# return ((size + clusterSize - 1) / clusterSize) * clusterSize;

size_on_disk = int(((size + clusterSize - 1) / clusterSize)) * clusterSize
print('size on disk - {}' .format(size_on_disk))
