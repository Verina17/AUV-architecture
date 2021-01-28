import rospy
#from sw_hw.msg import filtered_data
#from sw_hw.msg import trajectory_data

from sw_hw.srv import path
from sw_hw.srv import pathRequest
from sw_hw.srv import pathResponse

class path_planning:

    def _init_ (self):

        rospy.init_node('path_planning')
        #self.pubp = rospy.Publisher('trajectory', trajectory_data, queue_size=10)
        #rospy.Subscriber("ekf_data", filtered_data, feedback_callback)
        #rospy.Subscriber("targets", target_data, mission_callback)
        s = rospy.Service('path_planning_service', path, path_planner_handler)
        rospy.spin()


    def path_planner_handler(self,req):
        #we do processing for the req 
        #and return 2 arrays of trajectory to mission planner
        x_c= req.x_c
        ar1=[1 2 3 4 5 6 7 8 9 10]
        ar2=[1 2 3 4 5 6 7 8 9 10]
        return pathResponse(ar1, ar2)

        
    while not rospy.is_shutdown():
        
        rate.sleep()


    #def filtered_data_callback():


    #def mission_callback():
               


if _name_ == 'main':
    try:
        path_planning()

    except rospy.ROSInterruptException:
        rospy.logerr('could not start')

        