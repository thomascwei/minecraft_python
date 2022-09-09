from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def chicken_rain():
    """
    show time
    """
    x, y, z = mc.player.getPos()
    for i in range(100):
        mc.spawnEntity(x + random.random() * 10, y + 20, z + random.random() * 10, entity.CHICKEN)
        time.sleep(0.2)


def demo01():
    """
    正上方10格位置生出一隻雞
    """
    x, y, z = mc.player.getPos()
    mc.spawnEntity(x, y + 10, z, entity.CHICKEN)


def practice01():
    """
    製作一個五層高的柱子,在註解下方寫下你的程式碼
    """
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y + 1, z - 1, block.Block(79))
    mc.setBlock(x + 4, y + 2, z - 1, block.Block(79))
    mc.setBlock(x + 4, y + 3, z - 1, block.Block(79))
    mc.setBlock(x + 4, y + 4, z - 1, block.Block(79))
    mc.setBlock(x + 4, y + 5, z - 1, block.Block(79))


def last_practice01():
    """
    製作五個互相連接的方塊
    """
    # 在下方寫下你的程式碼
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y, z - 1, block.Block(79))
    mc.setBlock(x + 4, y, z + 1, block.Block(79))
    mc.setBlock(x + 4, y, z, block.Block(79))
    mc.setBlock(x + 4, y, z - 2, block.Block(79))
    mc.setBlock(x + 4, y, z + 2, block.Block(79))


if __name__ == '__main__':
    # demo01()
    chicken_rain()
    # practice01()
    # last_practice01()
