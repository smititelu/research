import Router
import math
from math import sqrt

hysteresis = 4

class ModuleClass:
	def handover_trigger_child_init(self, arg):
		print 'Hello, child!'
		return 1

	def handover_trigger_function(self, msg, args):
#		Router.Logger.LM_INFO("args = " + args + "\n")
		pos = [float(int(x)) for x in args.split()]

		posX_first = pos[0]
		posY_first = pos[1]
		posX_last = pos[len(pos) - 2]
		posY_last = pos[len(pos) - 1]
#		Router.Logger.LM_INFO(str(posX_first) + " " + str(posY_first) + " " + str(posX_last) + " " + str(posY_last) + "\n")

		euclid = math.sqrt((posX_last - posX_first) * (posX_last - posX_first) + (posY_last - posY_first) * (posY_last - posY_first))
		Router.Logger.LM_DBG("euclidian distance=" + str(euclid) + "\n")

		if (euclid > hysteresis):
			Router.Logger.LM_DBG("euclidian distance=" + str(euclid) + " outside perimeter=" + str(hysteresis) + " HANDOVER !!!\n")
			return 17

		return 1


def handover_trigger_mod_init():
	print 'Hello, module!'
	x = ModuleClass()
	return x
