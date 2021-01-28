import rospy
from sw_hw.msg import filtered_data
from sw_hw.msg import target_data
from sw_hw.srv import path
from sw_hw.srv import pathRequest
from sw_hw.srv import pathResponse



class mission_planning():


    def _init_ (self):

        rospy.init_node('mission_planning')
        rospy.Subscriber("ekf_data", filtered_data, feedback_callback)
        #self.pub = rospy.Publisher('targets', target_data, queue_size=10)
        rospy.Publisher('trajectory', trajectory_data, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        #self.pub = rospy.Publisher('targets', target_data, queue_size=10)


        msg2= target_data()


        def feedback_callback():
            msg= filtered_data()



            #extract states and state variance
            #call mission planner function and sent to 
            #msg2= target_data()
            msg2.target_pt = [1 2 3]


            pub.publish(msg2)

        def mission_planning(self,state, state_variance):
            #if condition specifies if we are in a mission or not
            #if we need path planning, request service from path planning
            # and returns trajectory
            #and publish this trajectory to the respective control node
            #according to the perception variance, object is detected or not



            rospy.wait_for_service('path_planning_service')
            try:

                path= rospy.ServiceProxy('path_planning_service',path)
                traj= path(state[0], state[1], state[2], state[3], state[4], state[5],state[6])


            except rospy.ServiceException, e:
                print "Service call Failed : %s" %e    





if _name_ == 'main':
    try:
        mission_planning()

    except rospy.ROSInterruptException:
        rospy.logerr('could not start')
            


