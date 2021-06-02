import getch
import rospy

from geometry_msgs.msg import Twist
V = 0.5 #Velocity
O = 1.0 #Omega
twist = Twist()

def forward():#
    print('W, Velocity = {}'.format(V))
    twist.linear.x = V
    twist.angular.z = 0
def backward():#
    print('S, Velocity = {}'.format(V))
    twist.linear.x = -V
    twist.angular.z = 0
def stop():#
    print('Spacebar, Stopped')
    twist.linear.x = 0
    twist.angular.z = 0
def turn_left():#
    print('A, Omega = {}'.format(O))
    twist.angular.z = -O
    twist.linear.x = 0
def trun_right():#
    print('D, Omega = {}'.format(O))
    twist.angular.z = O
    twist.linear.x = 0
    
def main():
    pub = rospy.Publisher('/Putang/cmd_vel',Twist,queue_size=1)
    rospy.init_node('keyboard_control',anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        k=ord(getch.getch())
        if k==119: #W
            forward()
        elif k==97: #A
            turn_left()
        elif k==115: #S
            backward()
        elif k==100: #D
            trun_right()
        elif k==32: #Spacebar
            stop()
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    kt = main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)