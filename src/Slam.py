import rospy
import numpy as np
from sw_hw.msg import filtered_data
from sw_hw.msg import IMU_data
from sw_hw.msg import dvl_data
from sw_hw.msg import mission_loc


class slam:
    def _init_ (self):
        rospy.init_node('slam')
        self.pubs = rospy.Publisher('ekf_data', filtered_data, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        rospy.Subscriber("IMU", IMU_data, IMU_callback)
        rospy.Subscriber("depth", pressure, depth_callback)
        rospy.Subscriber("dvl", dvl_data , dvl_callback)
        rospy.Subscriber("missions", mission_loc, percept_callback)
        

        

        msg1= filtered_data()
        msg1.velocity = [1 2 3]
        msg1.orientation = [4 5 6]
        msg1.acceleration= [0 1 2]
        msg1.depth = 7
        msg1.missions= [8 9 10]  


        while not rospy.is_shutdown():
            rospy.loginfo(msg1)
            pubs.publish(msg1)
            rate.sleep()





    #def IMU_callback():


    def depth_callback():

    def dvl_callback():

    def percept_callback():



 if _name_ == 'main':
    try:
        slam()

    except rospy.ROSInterruptException:
        rospy.logerr('could not start')
       