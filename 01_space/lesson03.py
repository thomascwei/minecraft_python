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
        # 猜猜會印出幾次
        mc.postToChat("哈囉")
        # 先觀察i的變化
        mc.postToChat(i)
        # 把你的程式碼放迴圈裡，用i取代慢慢增加的數字


def practice01():
    """
    修改前一課製作柱子程式碼，改用迴圈減少你的程式碼
    """
    x, y, z = mc.player.getTilePos()
    for i in range(1000):
        # 生成一個方塊
        mc.setBlock(x + 4, y + i, z - 1, block.Block(11))
        # 將i印出在聊天視窗
        # mc.postToChat(i)


def practice02():
    """
    通天塔
    """
    # 在下方寫下你的程式碼
    x, y, z = mc.player.getPos()
    for i in range(300):
        mc.setBlock(x + i, y + 1, z + 1, block.Block(79))


if __name__ == '__main__':
    practice02()
