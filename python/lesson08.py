from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def demo():
    # 取得當前位置
    x, y, z = mc.player.getTilePos()

    i = 0
    # while 迴圈
    while i < 5:
        # 若為真執行以下
        mc.postToChat("{} {} {}".format(x + i, y, z))
        i = i + 1
        i = i + 1


def practice01():
    """
    用一個while圈產生 TNT,鑽石,TNT,鑽石...的一組方塊
    :return:
    """
    # 取得當前位置
    x, y, z = mc.player.getTilePos()
    i = 0
    while i < 5:
        mc.setBlock(x + i * 2, y, z, block.Block(46))
        mc.setBlock(x + i * 2 + 1, y, z, block.Block(57))

        i = i + 1


if __name__ == '__main__':
    # demo()
    practice01()
