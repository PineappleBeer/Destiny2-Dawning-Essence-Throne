
import time;
import pyautogui as pg;
from lib.util import compareImg;

pasteCode = 0; # 避免重复粘贴

# 打开输入框
def openInput(): 
    if compareImg('./img/input.png') == 0:
        pg.press('enter');
        return 1;
    return 0;

# 输入英文队伍码
def inputCodeEn():
    pg.typewrite('/j bigBro#6666', interval = 0.2);
    return 0;

# 输入中文队伍码
def inputCodeCn():
    pg.typewrite('/j ');
    pg.press('shift');
    time.sleep(0.2)
    pg.typewrite('dl1', interval = 0.2);
    time.sleep(0.2)
    pg.press('shift');
    time.sleep(0.2)
    pg.typewrite('#6666', interval = 0.2);
    return 0;

# 检查是否加入成功
def checkJoin():
    global pasteCode;

    if compareImg('./img/error.png') != 0:
        pg.press('esc');
        return 0;
    elif compareImg('./img/success.png') != 0:
        pasteCode = 1;
        return 1;
    return 0;

# 加入队伍
def joinTeam():
    openInput();
    time.sleep(1);
    if compareImg('./img/input.png') != 0: # 因为无法使用pyautogui的热键来复制粘贴代码，所以选择手动输入
        inputCodeCn();
        #inputCodeEn();
    else:
        return 0;
    time.sleep(1);
    pg.press('enter');
    time.sleep(5);
    checkJoin();
    return 1;



def exitGame():
    global pasteCode;

    pasteCode = 0;
    pg.keyDown('o');
    time.sleep(3);
    pg.keyUp('o');
    return 1;

while(1): 
    navigationBtn = compareImg('./img/navigationBtn.png');
    abilitiesBtn = compareImg('./img/abilities.png');
    exitBtn = compareImg('./img/exitBtn.png');

    if (navigationBtn != 0) & (pasteCode == 0):
        joinTeam();
    elif abilitiesBtn != 0:
        pg.press('tab');
        exitGame();
    elif exitBtn != 0:
        exitGame();
        
    time.sleep(1);
