from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def practice01():
    # 取得當前位置
    x, y, z = mc.player.getPos()
    print(x, y, z)
    # 建金字塔 5,3,1
    # 第一層
    mc.setBlocks(x + 2, y + 1, z - 2,
                 x + 6, y + 1, z + 2,
                 block.Block(57))
    # 第二層
    mc.setBlocks(x + 5, y + 2, z + 1,
                 x + 3, y + 2, z - 1,
                 block.Block(57))
    # 第三層
    mc.setBlock(x + 4, y + 3, z, block.Block(57))
    # 移動到塔頂
    mc.player.setPos(x + 4, y + 4, z)


def demo01():
    """
    移動角色
    :return:
    """
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y + 100, z)


def demo02():
    """
    招喚凋零怪
    :return:
    """
    x, y, z = mc.player.getPos()
    mc.spawnEntity(x + 3, y - 3, z + 3, entity.Entity(64))


def demo03():
    """
    移除凋零怪
    :return:
    """
    mc.removeEntities(64)


if __name__ == '__main__':
    practice01()
    # demo02()
    # demo03()
