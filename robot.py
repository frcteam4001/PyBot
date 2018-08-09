import wpilib


class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations

        self.leftMotor = wpilib.Victor(0)
        self.rightMotor = wpilib.Victor(1)

        #self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot = wpilib.DifferentialDrive(self.leftMotor, self.rightMotor)

        # joyStick 0
        self.joyStick = wpilib.Joystick(0)
        self.myRobot.setExpiration(0.1)



    def autonomousInit(self):
        '''

        :return:
        '''
        pass


    def autonomousPeriodic(self):
        pass



    def teleopInit(self):
        '''
        Executed at the start of teleop mode
        '''
        self.myRobot.setSafetyEnabled(True)


    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''

        move = self.joyStick.getRawAxis(1)
        turn = self.joyStick.getRawAxis(4)
        self.myRobot.arcadeDrive(move, turn)


if __name__ == '__main__':
    wpilib.run(MyRobot)