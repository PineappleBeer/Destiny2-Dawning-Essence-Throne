
from PIL import ImageGrab;
import numpy as np;
import cv2 as cv;
import pyautogui as pg;


def getScreen():
  im = ImageGrab.grab().convert('L');
  im = np.array(im);
  return im;

# 图像匹配
def compareImg(path):
    tl = cv.imread(path, 0);
    sc = getScreen();
    r = cv.matchTemplate(sc, tl, cv.TM_CCOEFF_NORMED);
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(r);
    if max_val > 0.9:
        return max_val;
    return 0;

# 判断队伍加满，因为假如是三个人队伍，除了车头另外两个队友加入时间不一样，导致排列不一样，所以需要两张图
def checkTeam():
    team = compareImg('./img/team.png');
    team2 = compareImg('./img/team2.png');
    if (team != 0) | (team2 != 0):
        return 1;
    return 0;

# 移动鼠标并点击
def moveClick(po):
    pg.moveTo(po[0] + 10, po[1] + 10);
    pg.click();