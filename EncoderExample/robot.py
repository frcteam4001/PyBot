import wpilib
from wpilib.drive import DifferentialDrive
import math



class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.leftMotor = wpilib.Victor(0)
        self.rightMotor = wpilib.Victor(1)

        #self.myRobot = wpilib.RobotDrive(0, 1)
        self.myRobot = DifferentialDrive(self.leftMotor, self.rightMotor)


        # joyStick 0
        self.joyStick = wpilib.Joystick(0)
        self.myRobot.setExpiration(0.1)
        self.myRobot.setSafetyEnabled(True)

        # encoders
        self.rightEncoder = wpilib.Encoder(0, 1, False, wpilib.Encoder.EncodingType.k4X)
        self.leftEncoder = wpilib.Encoder(2,3, False, wpilib.Encoder.EncodingType.k4X)

        # set up encoder
        self.drivePulsePerRotation  = 1024
        self.driveWheelRadius = 3.0
        self. driveGearRatio = 1.0/1.0
        self.driveEncoderPulsePerRot = self.drivePulsePerRotation * self.driveGearRatio
        self.driveEncoderDistPerPulse = (math.pi*2*self.driveWheelRadius)/self.driveEncoderPulsePerRot;

        self.leftEncoder.setDistancePerPulse(self.driveEncoderDistPerPulse)
        self.leftEncoder.setReverseDirection(False)
        self.rightEncoder.setDistancePerPulse(self.driveEncoderDistPerPulse)
        self.rightEncoder.setReverseDirection(False)

        self.timer = wpilib.Timer()


    def autonomousInit(self):
        '''

        :return:
        '''
        self.timer.reset()
        self.timer.start()

        print("START")
        self.printEncoderValues("Left Encoder",self.leftEncoder)
        self.printEncoderValues("Right Encoder", self.rightEncoder)



    def autonomousPeriodic(self):
        if not self.timer.hasPeriodPassed(5):
            self.leftMotor.set(0.5)
            self.rightMotor.set(0.5)
        else:
            self.leftMotor.set(0)
            self.rightMotor.set(0)
            self.timer.stop()

            print("FINISH")
            self.printEncoderValues("Left Encoder", self.leftEncoder)
            self.printEncoderValues("Right Encoder", self.rightEncoder)





    def teleopInit(self):
        """Executed at the start of teleop mode
        :return:
        """
        pass


    def teleopPeriodic(self):
        """Runs the motors with tank steering
        :return:
        """

        move = self.joyStick.getRawAxis(1)
        turn = self.joyStick.getRawAxis(4)
        self.myRobot.arcadeDrive(move, turn)


    def printEncoderValues(self, name,encoder):
        print(name)
        print()
        print("{0}: {1}".format("DistancePerPulse",encoder.getDistancePerPulse()))
        print("{0}: {1}".format("Distance", encoder.getDistance()))
        print("{0}: {1}".format("Raw Count", encoder.getRaw()))




if __name__ == '__main__':
    wpilib.run(MyRobot)