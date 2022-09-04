from mcpi_e import block
from mcpi_e import entity
# from mcpi_e.entity import *
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def show_current_pos():
    use_pos = mc.player.getPos()
    print("pos: x:{},y:{},z:{}".format(use_pos.x, use_pos.y, use_pos.z))


def home():
    (x, y, z) = mc.player.getPos()
    # 前
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3 + i, y + j, z + 3, block.Block(20))
    # 後
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3 + i, y + j, z - 3, block.Block(20))
    # 左
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3, y + j, z - 3 + i, block.Block(20))
    # 右
    for i in range(6):
        for j in range(3):
            mc.setBlock(x + 3, y + j, z - 3 + i, block.Block(20))
    # 地板
    mc.setBlocks(x - 3, y - 1, z - 3, x + 3, y - 1, z + 3, block.Block(20))
    # 屋頂
    mc.setBlocks(x - 3, y + 4, z - 3, x + 3, y + 4, z + 3, block.Block(20))
    # 門
    mc.setBlock(x + 3, y, z, block.Block(64))
    mc.setBlock(x + 3, y + 1, z, block.Block(64))


def wall():
    (x, y, z) = mc.player.getPos()
    for i in range(20):
        for j in range(10):
            mc.setBlock(x - 10 + i, y + j, z + 3, block.Block(41))


def tnt():
    (x, y, z) = mc.player.getPos()
    for i in range(20):
        for j in range(10):
            mc.setBlock(x - 10 + i, y + j, z + 3, block.TNT)


def spawn():
    pos = mc.player.getPos()
    number = 5
    for i in range(number):
        mc.spawnEntity(pos.x, pos.y, pos.z, entity.CHICKEN)
        time.sleep(1)


def fire_around():
    while True:
        (x, y, z) = mc.player.getPos()
        # 前
        for i in range(6):
            for j in range(3):
                mc.setBlock(x - 3 + i, y + j, z + 3, block.Block(51))
        # 後
        for i in range(6):
            for j in range(3):
                mc.setBlock(x - 3 + i, y + j, z - 3, block.Block(51))
        # 左
        for i in range(6):
            for j in range(3):
                mc.setBlock(x - 3, y + j, z - 3 + i, block.Block(51))
        # 右
        for i in range(6):
            for j in range(3):
                mc.setBlock(x + 3, y + j, z - 3 + i, block.Block(51))
        time.sleep(1)


def create_lava():
    x, y, z = mc.player.getPos()
    mc.setBlock(x - 5, y + 5, z - 5, block.Block(10))
    mc.setBlock(x - 5, y + 5, z, block.Block(10))
    mc.setBlock(x - 5, y + 5, z + 5, block.Block(10))


def create_wood():
    x, y, z = mc.player.getPos()
    mc.setBlock(x - 3, y, z - 1, block.Block(5))
    mc.setBlock(x - 3, y, z, block.Block(5))
    mc.setBlock(x - 3, y, z + 1, block.Block(5))


if __name__ == '__main__':
    # mc.postToChat("hello everybody,   I am Jim")
    # 作業: 請製作連續三格連在一起的石塊
    (x, y, z) = mc.player.getPos()
    print(x, y, z)
    mc.setBlock(x + 4, y, z - 1, block.Block(9))
    mc.setBlock(x + 4, y, z + 1, block.Block(9))
    mc.setBlock(x + 4, y, z, block.Block(9))
