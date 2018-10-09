from sys import exit
from random import randint
				
class Map:
	
	def central_corridor(self):    
		action = input(">")
	
		if action == "shoot!":
			print("quick on the draw you yank out your blaster and fire it at the gothon. ")   #快拉，你拔出你的爆破枪，向gothon开火
			print("his clown costume is flowing and moving around his body, which throws ")   #他的小丑服装是流动和移动在他的身体，扔
			print("off your aim. your laser hits his costume but misses him entirely. this")  #
			print("completely ruins his brand new costume his mother bought him, which")
			print("makes him fly into an insane rage and blast you repeatedly in the face untill")
			print("you are dead. then he eats you. ")
			print("快拉，你拔出你的爆破枪，向gothon开火。\n他的小丑服装是流动和移动在他的身体，这抛出了你的目标。\n你的激光击中了他的衣服，但完全错过了他。这完全毁掉了他妈妈给他买的新衣服，\n这让他勃然大怒，不停地打你的脸，直到“你死了”。然后他吃了你。")
			print(death)
		
		elif action == "dodge!":
			print("like a world class boxer you dodge, weave, slip and slide right")
			print("as the gothon's blaster cranks a laser past your head. ")
			print("in the middle of your artful dodge your foot slips and you")
			print("bang your head on the metal wall and pass out. ")
			print("you wake up shortly after only to die as the gothon stomps on ")
			print("your head and eats you. ")
			print("就像一个世界级的拳击手，你躲避、编织、滑动、向右滑动，\n就像gothon的爆破器在你头上发射激光一样。在你巧妙地避开你的脚滑，\n你的头撞在金属墙和昏倒。你醒来后不久就死了，gothon跺着你的头并吃掉了你")
			self.death()
		
		elif action == "tell a joke":
			print("lucky for you they made you learn gothon insults in the caademy. ")
			print("you tell the one gothon joke you know: ")
			print("lbhe zbgure vf fb sng, sadfsf akkf sdfk sdfkj asdfkj asdkfj . ")
			print("the gothon stops, tries not to laugh, then busts out laughing and can't move. ")
			print("while he's laughing you run up and shoot him square in the head")
			print("putting him down, then jump through the weapon armory door. ")
			print("幸运的是，他们让你在学院学会了gothon侮辱性语言。\n打印(“你讲一个你知道的gothon笑话:\nlbhe zbgure vf fb sng, sadfsf akkf sdfk sdfkj asdfkj asdkfj。\nothon停下来，试着不笑，然后突然大笑起来，动弹不得。\n当他在笑的时候，你跑过去对着他的脑袋开枪\n把他放下，然后跳进武器库的门。")
			self.laser_weapon_armory()

		else:
			print("dose not compute(计算)!")
			self.central_corridor()
	def laser_weapon_armory(self):
		print("you do a dive roll into the weapon armory, crouch and scan the room")
		print("you stand up and run to the far side of the room and find the")
		print("nentron bomb in its container. there's a keypad lock on the box")
		print("and you need the code to get the bomb out. if you get the code")
		print("wrong 10 times then the lock closes forever and you can't")
		print("get the bomb. the code is 3 digits. ")
		print("你做一个俯冲翻滚到武器库里，蹲下然后扫视整个房间\n你站起来，跑到房间的另一边去找\n在它的容器内的nentron炸弹。盒子上有一个键盘锁\n你需要代码把炸弹弄出来。如果你得到代码\n错了10次锁就永远关闭了，你不能炸弹。代码是3位数字。")
		
		code = "%d%d%d"%(randint(1,9), randint(1,9),randint(1,9))
		print(code)
		guess = input("[keypad]>")
		guesses = 0
		
		while guess != code and guesses < 10:
			print("bzzzzeddd!")
			guesses += 1
			guess = input("[keypad]>")
			
		if guess == code:
			print("the container clicks open and the seal breaks, letting gas out. ")
			print("you grab the nentron bomb and run as fast as you can to the")
			print("bridge where you must place it in the right spot. ")
			print("容器喀哒一声打开，密封破裂，气体泄漏。\n你抓住nentron炸弹，以最快的速度跑向桥，你必须把它放在正确的位置。")
			self.the_bridge()
			
		else:
			print("the lock buzzes one last time and then you hear a sickening")
			print("melting sound as the mechanism is fused together. ")
			print("you decide to sit there, and finally the gothons blow up the")
			print("ship from their ship and you die. ")
			print("锁响了最后一次，然后你听到一阵恶心的声音\n熔融的声音，因为机制是融合在一起。\n你决定坐在那里，最后哥顿人炸毁了离开他们的船，你就会死")
			self.death()

	def the_bridge(self):
		print("you burst onto the bridge with the neutron destrut bomb")
		print("under your arm and surprise 5 gothons who are trying to")
		print("take control of the ship. each of them has an even uglier")
		print("clown costume than the last. they haven't pulled their")
		print("weapons out yet, as they see the active bomb under your")
		print("arm and don't want to set it off. ")
		print("你用中子去支撑炸弹冲上了桥在你的手臂下，给5个试图这么做的哥顿人一个惊喜控制这艘船。\n他们每个人都有一个更丑的比上次的小丑戏服多。\n他们还没有退出武器还在，因为他们看到了你下面的炸弹手臂，不想引爆它。")
		
		action = input(">")
		
		if action == "throw the bomb":
			print("in a panic you throw the bomb at the group of gothons")
			print("and make a leap for the door. right as you drop it a ")
			print("gothon shoots you right in the back killing you. ")
			print("as you die you see another gothon frantically try to disarm")
			print("the bomb. you die knowing they will probably blow up when")
			print("it goes off. ")
			print("你惊慌失措地把炸弹扔向一群哥顿人。向门口跳过去。就在你放下它的时候gothon朝你后背开枪，杀了你。\n当你死的时候，你会看到另一只蜥蜴疯狂地试图解除武装炸弹。你死的时候知道他们可能会爆炸它离开。")
			self.death()
			
		elif action == 'slowly place the bomb':
			print("you point your blaster at the bomb under your arm")
			print("and the gothons put their hands up and start to sweat. ")
			print("you inch backward to the door, open it, and then carefully")
			print("place the bomb on the floor, pointing your blaster at it. ")
			print("you then jump back through the door, punch the close button")
			print("and blast the lock so the gothons can't get out. ")
			print("now that the bomb is placed you run to the escape pod to ")
			print("get off this tin can. ")
			print("你把炸弹对准手臂下的炸弹,哥顿人举起手开始出汗。\n你向门后退一步，打开它，然后小心翼翼把炸弹放在地板上，用你的爆破枪对准它。然后你跳回门，按下关闭按钮把锁炸了，哥顿人就出不去了。\n既然炸弹被放置好了，你就跑到逃生舱去把这个罐头拿开。")
			self.escape_pod()
			
		else:
			print("dose not compute!")
			return 'the_bridge'
			self.except_pod()
		
	def escape_pod(self):
		print("you rush through the ship desperately trying to make it to")
		print("the escape pod before the whole ship explodes. it seems like")
		print("hardly any gothons are on the ship, so your run is clear of")
		print("interference. you get to the chamber with the escape pods, and")
		print("now need to pick one to take. some of them could be damaged")
		print("but you don't have time to look. there's 5 pods, which one")
		print("do you take ?")
		print("你拼命地闯过那条船，想闯过去,整个飞船爆炸前的逃生舱。似乎船上几乎没有哥顿人，所以你逃不掉干扰。\n你带着逃生舱来到房间现在需要选择一个。其中一些可能会受损但你没有时间去看。\n有5个分离舱，哪一个“你拿吗?”")
			
		good_pod = randint(1,5)
		print(good_pod)
		guess = input("[pod #]>")
		
		if int(guess) != good_pod:
			print("you jump into pod %s and hit the eject button. "% guess)
			print("the pod escapes out into the void of space, then")
			print("into jam jelly. ")
			print("进入pod  并单击弹出按钮。这样一来，豆荚就逃到了太空中果酱果酱。")
			self.death()
		else:
			print("you jump into pod %s and hit the eject button. "% guess)
			print("the pod easily slides out into space heading to")
			print("the planet below. as it flies to the planet, you look")
			print("back and see your ship implode then explode like a ")
			print("bright star, taking out the gothon ship at the same")
			print("time. you won!")
			print("你跳进吊舱，按弹出按钮。\n圆荚体很容易滑出，进入太空下面的行星。当它飞向地球时，你看回来看看你的飞船爆炸然后像爆炸一样爆炸一颗明亮的星，同时带着gothon飞船时间。你赢了!")
			exit(0)	


			
class Engine(Map):	
			
	def play(self):
		print("the gothons of planet percal #25 have invaded your ship and destroyed ")  #percal #25星球上的哥顿人入侵了你的飞船并摧毁了它
		print("your entire crew. you are the last surviving member and your last. ")    #全体船员。你是最后一个幸存的成员，也是最后一个
		print("mission is to get the nentron destrut bomb from the weapons armory, ")   #任务是从武器库里取出nentron去支撑炸弹
		print("put it in the bridge, and blow the ship up after getting into an ")      #把它放在桥上，然后把船炸了
		print("escape pod. ")                                                           #逃生
		print("\n")
		print("you're running down the central corridor to the weapons armory when")   #你跑到中央走廊去武器库的时候
		print("a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")  #一只蜥蜴跳出来，红色的有鳞的皮肤，深色的脏牙和邪恶的小丑服装
		print("flowing around his hate filled body. he's blocking the door to the ")       #在他充满仇恨的身体周围流动。他把门堵上了
		print("armory and about to pull a weapon to blast you. ")                           #军械库准备用武器来炸你
		print("行星percal 25的哥顿人入侵了你的飞船并摧毁了它。\n你是最后一个幸存的成员，也是最后一个。任务是让nentron从武器库里拆下炸弹，把它放在舰桥上，然后在进入逃生舱后炸掉飞船。\n你跑到中央走廊去武器库的时候一只蜥蜴跳出来，红色的鳞片皮肤，深色的脏牙，邪恶的小丑服装在他充满仇恨的身体周围流动。\n他挡住了军械库的门，准备用武器来炸你。")
		self.central_corridor()
		
	def death(self):
		quips = ["you died. you kinda suck at this. ",
			"nice job, you died ...jackass. ",
			"such a luser. ",
			"i have a small puppy that's better at this. "]   
	
		print(quips[randint(0,len(quips)-1)])
		exit(1)			
		
sam = Engine()
sam.play()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		