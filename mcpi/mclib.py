# general imports
import sys, time
# Minecraft imports
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3

# chat wrapper
def chat(msg):
	mc.postToChat(msg)

# switch viewpoint
def cameraFollow(state):
  if state == True:
    mc.camera.setFollow()
  else:
    mc.camera.setNormal()

# save the game state as a checkpoint
def save():
  mc.saveCheckpoint()

# restore the game state from a checkpoint
def restore():
  mc.restoreCheckpoint()

# player tile position wrapper (integer x,y,z return)
def myPos():
	return mc.player.getTilePos()

# get the block type at a location
def getBlock(x,z):
  y = mc.getHeight(x,z)
  return mc.getBlock(x,y-1,z)

# move player to a new location
def moveTo(x,z):
  y = mc.getHeight(x,z)
  mc.player.setTilePos(x,y,z)

# move player relative to current position
def moveRelative(xinc,zinc):
  x,y,z = mc.player.getTilePos()
  y = mc.getHeight(x+xinc,z+zinc)
  mc.player.setTilePos(x+xinc,y,z+zinc)

# determine of the player have moved to a new tile
def hasPlayerMoved(x,y,z):
  newx,newy,newz = mc.player.getTilePos()
  if newx!=x or newy!=y or newz!=z:
    # player has moved so return new location
    return newx, newy, newz
  # no change
  return False

# peek at a new location
def peekAt(newx,newz):
  # get the current position
  x,y,z = myPos()
  # move to new position
  moveTo(newx,newz)
  # wait for 10 seconds
  chat("You have 10 seconds to look around...")
  time.sleep(10)
  # return to original location
  moveTo(x,z)

# drill down and return block list
def drillDown():
  blocks = []
  x,y,z = myPos()
  while y >= 0:
    y = y - 1
    blocks.append(mc.getBlock(x,y,z))
  return blocks

def cuboid(x,y,z,width,depth,material):
  mc.setBlocks(x-width, y, z-width, x+width, y+depth, z+width, material)

def room(x,y,z,width,depth,material):
  # create solid cuboid
  cuboid(x,y,z,width,depth,material)
  # fill with air
  cuboid(x,y+1,z,width-2,depth-2,block.AIR)

# create minecraft instance
mc = minecraft.Minecraft.create()

