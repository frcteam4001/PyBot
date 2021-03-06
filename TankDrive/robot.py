import wpilib
from wpilib.drive import DifferentialDrive



class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.leftMotor = wpilib.Victor(0)
        self.rightMotor = wpilib.Victor(1)

        #self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot = DifferentialDrive(self.leftMotor, self.rightMotor)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

        self.myRobot.setExpiration(0.1)
        self.myRobot.setSafetyEnabled(True)



    def autonomousInit(self):
        '''

        :return:
        '''
        pass


    def autonomousPeriodic(self):
        pass



    def teleopInit(self):
        """Executed at the start of teleop mode
        :return:
        """
        pass


    def teleopPeriodic(self):
        """Runs the motors with tank steering
        :return:
        """

        self.myRobot.tankDrive(self.leftStick.getY(), self.rightStick.getY())


if __name__ == '__main__':
    wpilib.run(MyRobot)