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
    # 前
    mc.setBlocks(x + 3, y + 1, z - 3,
                 x - 3, y + 3, z + 3,
                 block.Block(0))
    # 後
    # mc.setBlocks(x - 1, y, z,
    #              x - 1, y + 3, z,
    #              block.Block(0))
    # # 左
    # mc.setBlocks(x, y, z + 1,
    #              x, y + 3, z + 1,
    #              block.Block(0))
    # # 右
    # mc.setBlocks(x, y, z - 1,
    #              x, y + 3, z - 1,
    #              block.Block(0))


def chicken_BBQ():
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 2, y, z, block.FIRE)
    for i in range(10):
        time.sleep(0.5)
        mc.spawnEntity(x + 2, y + 2, z, entity.CHICKEN)


if __name__ == '__main__':
    # while True:
    #     # time.sleep(0.1)
    #     practice01()
    chicken_BBQ()
