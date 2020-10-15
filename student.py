#!/usr/bin python3
from teacher import PiggyParent
import sys
import time
from collections import OrderedDict
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
        self.RIGHT_DEFAULT = 76
        self.SAFE_DISTANCE = 300
        self.CLOSE_DISTANCE = 46
        self.MIDPOINT = 1325  # what servo command (1000-2000) is straight forward for your bot?
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
        for x in range(5):
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
        #Starts to shake
        for x in range (5):
            self.turn_to_deg(0)
            self.turn_to_deg(110)
            self.fwd()
            time.sleep(.3)
            self.back()
            time.sleep(.4)
            self.turn_to_deg(70)
            self.fwd()
            time.sleep(.4)
            self.back()
            time.sleep(.3)
        self.fwd(left=100, right=100)
        time.sleep(.3)
        self.back()
        time.sleep(.6)
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
        for x in range(8):
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
        for x in range(2):
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
            if self.read_distance() < 400:
                print("NOT SAFE TO DANCE!")
                return False
            else:
                self.turn_by_deg(90) 
        # After all checks have been done, we deduce it is safe
        print("Safe to drive")
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
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+351, 100):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()
        self.scan_data = OrderedDict(sorted(self.scan_data.items()))
    
    def right_or_left(self):
        """Should I turn left or right?
            Returns a 'r' or an 'l' based on scan data"""
        self.scan()
        #average up the distances on the right and left side
        left_sum = 0
        left_avg = 0
        right_sum = 0
        right_avg = 0
        for angle in self.scan_data:
            # average up the distances on the right side then left
            if angle < self.MIDPOINT:
                right_sum += self.scan_data[angle]
                right_avg += 20  
            else:
                left_sum += self.scan_data[angle]
                left_avg += 20
            
        left_avg = left_sum / left_avg
        right_avg = right_sum / right_avg

        if left_avg > right_avg:
            return 'l'
        else: 
            return 'r'


    def obstacle_count(self):
        # Gotten from the discord server
        """Does a 360 scan and returns the number of obstacles it sees"""
        # do a scan of the area in front of the robot
        self.scan()
        # FIGURE OUT HOW MANY OBSTACLES THERE WERE
        see_an_object = False
        count = 0

        for angle in self.scan_data:
            dist = self.scan_data[angle]
            if dist < self.SAFE_DISTANCE and not see_an_object:
                see_an_object = True
                count += 1
                print("~~~~ I SEE SOMETHING!!! ~~~~~")
            elif dist > self.SAFE_DISTANCE and see_an_object:
                see_an_object = False
                print("I guess the object ended")

            print("ANGLE:  %d  |  DIST: %d" % (angle, dist))
        print("\nI saw %d objects" % count)

    def quick_check(self):
        """ Moves the servo to 3 angles and preforms a distance check """
        # loop 3 times and move the servo
        for ang in range(self.MIDPOINT - 100, self.MIDPOINT + 101, 100):
            self.servo(ang)
            time.sleep(.1)
            if self.read_distance() < self.SAFE_DISTANCE:
                return False
        # if the three-part check didn't freak out
        return True
    
    def turn_until_clear(self):
        """ Rotate right until no obstacle is seen """
        print("Will turn into clear")
        # make sure servo is straight
        self.servo(self.MIDPOINT)
        while self.read_distance() < self.SAFE_DISTANCE:
            self.left(primary= 70, counter= 0)
            time.sleep(.05)
        # stop motion before we end the method
        self.stop()

    def nav(self):
        """ Auto-pilot program """
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        exit_ang = self.get_heading()
        turn_count = 0

        self.fwd()
        while True:
            if not self.quick_check():
                turn_count += 1
                self.stop()
                #self.turn_until_clear()
                if turn_count > 3 and turn_count % 4 == 0:
                    self.turn_to_deg(exit_ang)
                elif 'l' in self.right_or_left():
                    self.turn_by_deg(-45)
                else:
                    self.turn_by_deg(45)
            else:
                self.fwd()
            time.sleep(.01)
        


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
