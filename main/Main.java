package main;

public class Main {

	public static void main(String[] args) {
		RobotArm robot = new RobotArm();
		
		try {
			robot.move(1, 2500, 2500);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

}
