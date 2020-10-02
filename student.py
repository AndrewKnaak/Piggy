#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        if not self.safe_to_dance():
            return False # SHUT IT DOWN
        for x in range(1):
            self.checkrotate()
            self.spinandshake()
            self.wheeliewiggle()
            self.fwdbackparty()
            self.entireflex()

    def checkrotate(self):
        """Checks to the left and right with head, then spins"""
        print("checkrotate activated")
        # Head movement first
        self.servo(1500)
        time.sleep(1)
        self.servo(1200)
        time.sleep(.5)
        self.servo(1800)
        time.sleep(.5)
        # Starting to rotate here
        self.fwd()
        time.sleep(.5)
        if self in range(5):
            self.turn_by_deg(720)
            self.turn_by_deg(-720)
        self.stop()

    def spinandshake(self):
        """Spins for fun, then starts to shake"""
        print("spinandshake activated")
        #Face forward
        self.turn_to_deg(0)
        #Starting to spin
        self.right(primary=100, counter=0)
        time.sleep(1)
        self.stop()
        self.left(primary=100, counter=0)
        time.sleep(1)
        self.stop()
        #Starts to shake, maybe?
        for x in range (5):
            self.turn_to_deg(0)
            self.turn_to_deg(110)
            self.fwd()
            time.sleep(.3)
            self.back()
            time.sleep(.3)
            self.turn_to_deg(70)
            self.fwd()
            time.sleep(.3)
            self.back()
            time.sleep(.3)
        # Quinn's shuffle code with my own touch is after this
        for x in range(5):
            self.left(primary=-60, counter=-20)
            time.sleep(.3)
            self.right(primary=-60, counter=-20)
            time.sleep(.3)
        # Going forward again
        for x in range(5):
            self.left(primary=60, counter=20)
            time.sleep(.3)
            self.right(primary=60, counter=20)
            time.sleep(.3)
        self.stop()
    
    def wheeliewiggle(self):
        """Do a wheelie then wiggle to the right and go back to orgin""" 
        "Wheelie"
        print("wheeliewiggle activated")
        for x in range(3):
                self.turn_to_deg(0)
                self.fwd(left=100,right=100)
                time.sleep(1)
                self.fwd(left=-100,right=-100)
                time.sleep(.2)
                self.back()
                time.sleep(.8)
        self.fwd()
        time.sleep(.5)
        # Going to the right by wiggling
        for x in range(5):
            self.turn_to_deg(80)
            self.fwd()
            time.sleep(.5)
            self.turn_to_deg(100)
            self.back()
            time.sleep(.5)
        # Returning to original position before going to the right 
        for x in range(5):
            self.turn_to_deg(100)
            self.fwd()
            time.sleep(.5)
            self.turn_to_deg(80)
            self.back()
            time.sleep(.5)
        self.stop()

    def fwdbackparty(self):
        """Go back and forth to make a wiggle, then wiggle side to side, and then do a few circles"""
        print("fwdbackparty activated")
        # Doing the wiggle motion 8 times
        if self in range(8):
            self.fwd()
            time.sleep(.4)
            self.left()
            time.sleep(.2)
            self.back()
            time.sleep(.4)
            self.right()
            time.sleep(.2)
            self.turn_to_deg(0)
        # Time for some mini
        if self in range(2):
            self.right(primary=0, counter=-50)
            time.sleep(.5)
            self.right(primary=0, counter=-70)
            time.sleep(.5)
            self.right(primary=0, counter=-90)
            time.sleep(.5)
            self.right(primary=100, counter=0)
            time.sleep(1)
            self.right(primary=0, counter=-100)
            time.sleep(1)
            self.turn_to_deg(0)
        self.stop()




    def entireflex(self):
        """Moves his wheels and head simultaneously"""
        print("entireflex activated")
        self.fwd()
        time.sleep(.1)
        self.servo(1500)
        time.sleep(.25)
        self.right()
        time.sleep(.1)
        self.deg_fwd(180)
        time.sleep(.5)
        self.servo(1200)
        time.sleep(.5)
        self.deg_fwd(0)
        time.sleep(.5)
        self.servo(1800)
        time.sleep(.5)
        self.left()
        time.sleep(1.)
        self.turn_to_deg(0)
        self.stop()

        




    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        # Check for all fail/early-termination conditions
        for _ in range(4):
            if self.read_distance() < 600:
                print("NOT SAFE TO DANCE!")
                return False
            else:
                self.turn_by_deg(90) 
        # After all checks have been done, we deduce it is safe
        print("I AM THE BEST PROGRAMMER TO EVER LIVE")
        return True
    

    
    def shake(self):
        self.deg_fwd(720)
        self.stop()


    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
