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
    建一個TNT+壓力板
    """
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y - 1, z, block.TNT)
    mc.setBlock(x + 4, y, z, block.Block(72))


def demo02():
    """
    建一個紅石燈
    """
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y, z, block.Block(278))


def demo04():
    """
    建一個金治台
    """
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x + 1, y, z, block.Block(58))

def demo05():
    """
    建木劍
    """
    x, y, z = mc.player.getTilePos()
    mc.getBlock(x + 1, y, z, block.Block(268))

def demo03():
    """
    清除怪物
    :return:
    """
    for i in range(50, 70):
        mc.removeEntities(i)


if __name__ == '__main__':
    demo03()
    # demo04()
    demo05()
