from mcpi_e import block
from mcpi_e import entity
from mcpi_e.minecraft import Minecraft
import time

serverAddress = "127.0.0.1"  # change to your minecraft server
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "thomascwei"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)


def show_current_pos():
    use_pos = mc.player.getTilePos()
    print("你目前的座標: x:{},y:{},z:{}".format(use_pos.x, use_pos.y, use_pos.z))
    mc.postToChat("你目前的座標: x:{},y:{},z:{}".format(use_pos.x, use_pos.y, use_pos.z))


def demo01():
    """
    建一個方塊
    """
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y, z, block.Block(57))


def practice01():
    """
    製作三個互相連接的方塊
    """
    # 在下方寫下你的程式碼
    x, y, z = mc.player.getPos()
    mc.setBlock(x + 4, y, z - 1, block.Block(9))
    mc.setBlock(x + 4, y, z + 1, block.Block(9))
    mc.setBlock(x + 4, y, z, block.Block(9))


def home():
    """
    show time
    """
    (x, y, z) = mc.player.getPos()
    # 前
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3 + i, y + j, z + 3, block.Block(17.2))
    # 後
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3 + i, y + j, z - 3, block.Block(17.2))
    # 左
    for i in range(6):
        for j in range(3):
            mc.setBlock(x - 3, y + j, z - 3 + i, block.Block(17.2))
    # 右
    for i in range(6):
        for j in range(3):
            mc.setBlock(x + 3, y + j, z - 3 + i, block.Block(17.2))
    # 地板
    mc.setBlocks(x - 3, y - 1, z - 3, x + 3, y - 1, z + 3, block.Block(17.2))
    # 屋頂
    # mc.setBlocks(x - 3, y + 4, z - 3, x + 3, y + 4, z + 3, block.Block(20))
    # 門
    mc.setBlocks(x + 3, y, z,
                 x + 3, y + 1, z,
                 block.Block(64))
    # 精製台
    mc.setBlock(x + 2, y, z + 1, block.Block(58))
    # 木材
    mc.setBlock(x + 2, y + 1, z + 1, block.WOOD)
    mc.setBlock(x + 2, y + 2, z + 1, block.WOOD)
    # 石
    mc.setBlock(x + 2, y, z + 2, block.STONE)
    mc.setBlock(x + 2, y + 1, z + 2, block.STONE)
    mc.setBlock(x + 2, y + 2, z + 2, block.STONE)

    # 熔爐
    mc.setBlock(x + 2, y, z - 1, block.Block(62))
    # 鐵
    mc.setBlock(x + 2, y + 1, z - 1, block.IRON_BLOCK)
    mc.setBlock(x + 2, y + 2, z - 1, block.IRON_BLOCK)
    # 煤
    mc.setBlock(x + 2, y, z - 2, block.COAL_ORE)
    mc.setBlock(x + 2, y + 1, z - 2, block.COAL_ORE)
    mc.setBlock(x + 2, y + 2, z - 2, block.COAL_ORE)
    # 火把
    mc.setBlock(x - 2, y + 2, z, block.Block(50))

    # 鑽石
    # mc.setBlock(x, y, z - 2, block.DIAMOND_BLOCK)
    # mc.setBlock(x, y + 1, z - 2, block.DIAMOND_BLOCK)
    # mc.setBlock(x, y + 2, z - 2, block.DIAMOND_BLOCK)
    # mc.setBlock(x - 1, y, z - 2, block.DIAMOND_BLOCK)
    # mc.setBlock(x - 1, y + 1, z - 2, block.DIAMOND_BLOCK)
    # mc.setBlock(x - 1, y + 2, z - 2, block.DIAMOND_BLOCK)
    # 紅石
    # mc.setBlock(x, y, z + 2, block.REDSTONE_ORE)
    # mc.setBlock(x, y + 1, z + 2, block.REDSTONE_ORE)
    # mc.setBlock(x, y + 2, z + 2, block.REDSTONE_ORE)
    # mc.setBlock(x - 1, y, z + 2, block.REDSTONE_ORE)
    # mc.setBlock(x - 1, y + 1, z + 2, block.REDSTONE_ORE)
    # mc.setBlock(x - 1, y + 2, z + 2, block.REDSTONE_ORE)
    # 牛
    mc.spawnEntity(x + 1, y, z + 1, entity.COW)


if __name__ == '__main__':
    # 示範取得當前座標
    show_current_pos()

    # 示範建立前方單一方塊
    # demo01()

    # 作業: 製作三個互相連接的方塊
    # practice01()

    # mc.spawnEntity(100, 10, 100, entity.CHICKEN)
    home()
