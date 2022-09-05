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
    x, y, z = mc.player.getPos()
    for i in range(100):
        mc.spawnEntity(x + random.random() * 10, y + 20, z + random.random() * 10, entity.CHICKEN)
        time.sleep(0.2)


if __name__ == '__main__':
    chicken_rain()

