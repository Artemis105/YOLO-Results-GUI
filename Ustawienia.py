import os

local=os.path.dirname(os.path.abspath('aplikacja_pred.py'))

Path_to_img=local
Path_to_model=local
Path_to_save=local
Path_to_label=local

Path_to_img+=f"\\Dane\\zdjecia"
Path_to_model+=f"\\Dane\\model"
Path_to_save+=f"\\Dane\\Zapis"
Path_to_label+=f"\\Dane\\label"
domyslny=''


roz_model='.pt'
def img_list():
    if os.path.exists(Path_to_img):
        pliki=os.listdir(Path_to_img)
        rozszerzenia=('.jpg', '.jpeg', '.png')
        wek=[]
        if not pliki:
            print('Folder zdjecia jest pusty.')
        else:
            for i in pliki:
                if i.endswith(rozszerzenia):
                    wek.append(i)
            if not wek:
                print('W folderze zdjecia nie ma plików o odpowiednim rozszerzeniu')

    else:
        print('Folder zdjecia nie istnieje')
    return wek;

def model_list():
    if os.path.exists(Path_to_model):
        pliki = os.listdir(Path_to_model)
        wek = []
        if not pliki:
            print('Folder model jest pusty.')
        else:
            for i in pliki:
                if i.endswith(roz_model):
                    wek.append(i)
            if not wek:
                print('W folderze model nie ma plików o odpowiednim rozszerzeniu')
    else:
        print('Folder model nie istnieje')
    return wek;
