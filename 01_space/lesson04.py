from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time
import random

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def listen():
    """
    監聽遊戲內的chat message
    """
    while True:
        for event in mc.events.pollChatPosts():
            print(event.message)
            if event.message == "1":
                front_fire()
            elif event.message == "2":
                lava_pool()
            elif event.message == "3":
                land_pool()
            elif event.message == "4":
                fire_ball()


def demo01():
    """
    while loop demo
    :return:
    """
    while 1 > 0:
        print("1真的大於0嗎?")


def demo02():
    """
    while loop 每圈都+1, 直到=10000
    :return:
    """
    i = 0
    while 1 < 1000:
        print(i)
        i = i + 1


def practice01():
    """
    用迴圈修改front_fire, 要用到兩層迴圈喔
    """


def practice02():
    """
    用while做無窮迴圈
    :return:
    """


def front_fire():
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    print(dir)
    mc.setBlock(x + 4 * dir.x, y, z + 4 * dir.z, block.FIRE)
    mc.setBlock(x + 4 * dir.x, y, z + 4 * dir.z + 1, block.FIRE)
    mc.setBlock(x + 4 * dir.x, y, z + 4 * dir.z - 1, block.FIRE)
    mc.setBlock(x + 4 * dir.x + 1, y, z + 4 * dir.z, block.FIRE)
    mc.setBlock(x + 4 * dir.x + 1, y, z + 4 * dir.z + 1, block.FIRE)
    mc.setBlock(x + 4 * dir.x + 1, y, z + 4 * dir.z - 1, block.FIRE)
    mc.setBlock(x + 4 * dir.x - 1, y, z + 4 * dir.z, block.FIRE)
    mc.setBlock(x + 4 * dir.x - 1, y, z + 4 * dir.z + 1, block.FIRE)
    mc.setBlock(x + 4 * dir.x - 1, y, z + 4 * dir.z - 1, block.FIRE)


def lava_pool():
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    print(dir)
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z - 1, block.AIR)

    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z - 1, block.AIR)

    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z, block.LAVA)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z + 1, block.LAVA)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z - 1, block.LAVA)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z, block.LAVA)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z + 1, block.LAVA)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z - 1, block.LAVA)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z, block.LAVA)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z + 1, block.LAVA)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z - 1, block.LAVA)


def land_pool():
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    print(dir)
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z, block.Block(3))
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z + 1, block.Block(3))
    mc.setBlock(x + 4 * dir.x, y - 1, z + 4 * dir.z - 1, block.Block(3))
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z, block.Block(3))
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z + 1, block.Block(3))
    mc.setBlock(x + 4 * dir.x + 1, y - 1, z + 4 * dir.z - 1, block.Block(3))
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z, block.Block(3))
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z + 1, block.Block(3))
    mc.setBlock(x + 4 * dir.x - 1, y - 1, z + 4 * dir.z - 1, block.Block(3))

    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x, y - 2, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x + 1, y - 2, z + 4 * dir.z - 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z + 1, block.AIR)
    mc.setBlock(x + 4 * dir.x - 1, y - 2, z + 4 * dir.z - 1, block.AIR)


def fire_ball():
    """
    前方火球
    """
    x, y, z = mc.player.getPos()
    dir = mc.player.getDirection()
    mc.spawnEntity(x + 4 * dir.x, y - 1, z + 4 * dir.z, entity.DRAGON_FIREBALL)


if __name__ == '__main__':
    # demo01()
    # front_fire()
    listen()
