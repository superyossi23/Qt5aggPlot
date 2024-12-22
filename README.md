# Qt5aggPlot

## HOW TO USE
- Run main.py
- Configure main.ini before use
- Works only for csv currently
- Can drag&drop a csv file

## For Developers
- Replace setupUI from main_.ui when to update gui
~~~.py
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    #########################################################
    # ⇓ Replace setupUI from main_.ui ⇓ #
    #########################################################
    def setupUi(self, MainWindow):
~~~


## COMMANDS
- pyuic5 -x main_.ui -o main_.py
- pyinstaller main.py --onedir
- pip freeze --local > requirements.txt


## REFERENCES
- https://pyshine.com/Make-GUI-With-Matplotlib-And-PyQt5/#google_vignette
- https://pyshine.com/Drag-Drop-CSV-File-on-PyQt5-GUI/
- 