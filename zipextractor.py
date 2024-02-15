import zipfile

def extractor(filepath,folderpath):
    with zipfile.ZipFile(filepath,'r') as extract:
        extract.extractall(folderpath)

if __name__=="__main__":
    extractor(filepath=r"C:\Users\saive\PycharmProjects\Unzip App\compressed.zip",folderpath=r"C:\Users\saive\PycharmProjects\Unzip App\Unzip files")