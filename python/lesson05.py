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
    # mc.spawnEntity(x + 2 * dir.x, y, z + 2 * dir.z, entity.COW)
    mc.setBlock(x + 1 * dir.x, y, z + 1 * dir.z, block.Block(62))

    # mc.setBlock(x + 1 * dir.x, y, z + 1 * dir.z, block.WOOD)
    mc.setBlock(x + 1 * dir.x, y + 1, z + 1 * dir.z, block.IRON_BLOCK)


if __name__ == '__main__':
    # demo02()
    x, y, z = mc.player.getPos()
    # mc.setBlock(x + 1 * dirr.x, y + 1, z + 1 * dirr.z, block.DIAMOND_BLOCK)
    mc.setBlocks(x - 2, y - 2, z - 2,
                 x - 2, y + 2, z + 2,
                 block.Block(46))

    mc.setBlock(x - 2, y + 1, z, block.Block(91))
