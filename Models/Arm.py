'''
Date:           03-08-2018
Creator:        Thijs Zijlstra
Version:        3.2
Description:    Arm inverse kinematics
'''
import numpy as np
import scipy.optimize


class Arm3Link:

    def __init__(self, q=None, q0=None, L=None):
        """Set up the basic parameters of the arm.
        All lists are in order [shoulder, elbow, wrist].

        q : np.array
            the initial joint angles of the arm
        q0 : np.array
            the default (resting state) joint configuration
        L : np.array
            the arm segment lengths
        """
        # initial joint angles
        self.q = [.3, .3, 0, 0, 0, 0] if q is None else q
        # some default arm positions
        self.q0 = np.array([np.pi/4, np.pi/4, np.pi/4, np.pi/4, np.pi/4, np.pi/4 ]) if q0 is None else q0
        # arm segment lengths
        self.L = np.array([1, 1, 1, 1, 1, 1]) if L is None else L

        self.max_angles = [np.pi, np.pi, np.pi/4, np.pi/4, np.pi/4, np.pi/4]
        self.min_angles = [0, 0, -np.pi/4, np.pi/4, np.pi/4, np.pi/4]

    def get_xy(self, q=None):
        """Returns the corresponding hand xy coordinates for
        a given set of joint angle values [shoulder, elbow, wrist],
        and the above defined arm segment lengths, L

        q : np.array
            the list of current joint angles

        returns : list
            the [x,y] position of the arm
        """
        if q is None:
            q = self.q

        x = self.L[0]*np.cos(q[0]) + \
            self.L[1]*np.cos(q[0]+q[1]) + \
            self.L[2]*np.cos(np.sum(q))

        y = self.L[0]*np.sin(q[0]) + \
            self.L[1]*np.sin(q[0]+q[1]) + \
            self.L[2]*np.sin(np.sum(q))

        return [x, y]

    def inv_kin(self, xy):
        """
        find the inverse kinematics for a 3 link arm with there joints to the desired position
        xy : tuple
            the desired xy position of the arm

        returns : list
            the optimal [shoulder, elbow, wrist] angle configuration
        """

        def distance_to_default(q, *args):
            """
            Calculate the distance between the joint space and the start position
            q : np.array
                the list of current joint angles

            returns : scalar
                euclidean distance to the default arm position
            """
            # weights found with trial and error,
            # get some wrist bend, but not much
            weight = [1, 1, 1.3, 1, 1, 1]
            return np.sqrt(np.sum([(qi - q0i)**2 * wi
                           for qi, q0i, wi in zip(q, self.q0, weight)]))

        def x_constraint(q, xy):
            """
            Return corresponding constraint for an arm segment

            q : np.array
                the list of current joint angles
            xy : np.array
                current xy position (not used)

            returns : np.array
                the difference between current and desired x position
            """
            x = (self.L[0]*np.cos(q[0]) + self.L[1]*np.cos(q[0]+q[1]) +
                 self.L[2]*np.cos(np.sum(q))) - xy[0]
            return x

        def y_constraint(q, xy):
            """
            Return corresponding constraint for an arm segment

            q : np.array
                the list of current joint angles
            xy : np.array
                current xy position (not used)
            returns : np.array
                the difference between current and desired y position
            """
            y = (self.L[0]*np.sin(q[0]) + self.L[1]*np.sin(q[0]+q[1]) +
                 self.L[2]*np.sin(np.sum(q))) - xy[1]
            return y

        def joint_limits_upper_constraint(q, xy):
            """Used in the function minimization such that the output from
            this function must be greater than 0 to be successfully passed.

            q : np.array
                the current joint angles
            xy : np.array
                current xy position (not used)

            returns : np.array
                all > 0 if constraint matched
            """
            return self.max_angles - q

        def joint_limits_lower_constraint(q, xy):
            """Used in the function minimization such that the output from
            this function must be greater than 0 to be successfully passed.

            q : np.array
                the current joint angles
            xy : np.array
                current xy position (not used)

            returns : np.array
                all > 0 if constraint matched
            """
            return q - self.min_angles

        return scipy.optimize.fmin_slsqp(
            func=distance_to_default,
            x0=self.q,
            eqcons=[x_constraint,
                    y_constraint],
            ieqcons=[joint_limits_upper_constraint,
                     joint_limits_lower_constraint],
            args=(xy,),
            iprint=0)  # iprint=0 suppresses output


if __name__ == '__Arm__':
        Arm3Link()