import rospy
from sw_hw.msg import control_action
from sw_hw.msg import filtered_data
from sw_hw.msg import trajectory_data

class control:
    def _init_ (self):
        rospy.init_node('control')
        self.pub = rospy.Publisher('action', control_action, queue_size=10)
        rospy.Subscriber("ekf_data", filtered_data, feedback_callback)
        rospy.Subscriber("trajectory", trajectory_data , setpoint_callback)
        rate = rospy.Rate(10) # 10hz


    def feedback_callback():

    def setpoint_callback():


if _name_ == 'main':
    try:
        control()

    except rospy.ROSInterruptException:
        rospy.logerr('could not start')

