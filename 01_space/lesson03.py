from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def demo01():
    """
    for 迴圈演示
    """
    for i in range(5):
        print("i=", i)
        # 先觀察i的變化
        # 把你的程式碼放迴圈裡，用i取代慢慢增加的數字


def practice01():
    """
    修改前一課製作一個五層高的柱子程式碼，改用迴圈減少你的程式碼
    """


if __name__ == '__main__':
    demo01()
