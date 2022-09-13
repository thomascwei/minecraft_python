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
    建一個TNT+FIRE
    """
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z, block.TNT)
    mc.setBlock(x + 4 * dir.x, y, z + 4 * dir.z, block.FIRE)


def demo02():
    """
    建一個紅石燈
    """
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    mc.setBlock(x + 2 * dir.x, y, z + 2 * dir.z, block.Block(50))


def demo03():
    """
    清除怪物
    :return:
    """
    for i in range(50, 70):
        mc.removeEntities(i)


def demo07():
    """
    正前方生出一隻牛
    """
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    mc.spawnEntity(x + 1 * dir.x, y, z + 1 * dir.z, entity.COW)


if __name__ == '__main__':
    demo01()
