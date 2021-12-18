
import time;
import pyautogui as pg;
from lib.util import compareImg, checkTeam, moveClick;

teamReady = 0;
hasRole = 1;

# 开始操作
def start():
    navigationBtn = compareImg('./img/navigationBtn.png');
    cityBtn = compareImg('./img/cityBtn.png');
    throneBtn = compareImg('./img/throneBtn.png');
    startgameBtn = compareImg('./img/startgameBtn.png');

    if navigationBtn != 0:
        moveClick(navigationBtn)
    elif cityBtn != 0:
        moveClick(cityBtn)
    elif throneBtn != 0:
        moveClick(throneBtn)
    elif startgameBtn != 0: #开始游戏，五秒后狂按ESC
        moveClick(startgameBtn)
        time.sleep(5);
        exitGame();

# 狂按ESC回到切换角色页面
def exitGame():
    global teamReady;
    global hasRole;
    
    esc = 1;
    while(esc):
        pg.press('esc');
        time.sleep(1); # 等待面板弹出
        switchBtn = compareImg('./img/switchBtn.png');
        if switchBtn != 0:
            moveClick(switchBtn);
            time.sleep(1); # 等待确认切换面板
            confirmBtn = compareImg('./img/confirmBtn.png');
            if confirmBtn != 0:
                moveClick(confirmBtn);
                esc = 0;
                teamReady = 0;
                hasRole = 0;

# 切换角色
def switchRole():
    global hasRole;

    roleBtn = compareImg('./img/roleBtn.png');
    if roleBtn != 0:
        moveClick(roleBtn);
        hasRole = 1;
    return 1;

while(1): 
    if hasRole == 0:
        switchRole();
    elif (teamReady == 0) & (checkTeam() == 1): # 判断队伍加满
        teamReady = 1;  

    if teamReady == 1:    
        start();

    time.sleep(1);