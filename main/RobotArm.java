package main;

import com.fazecast.jSerialComm.*;

import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.PrintStream;

public class RobotArm {
	
	private OutputStream out;
	
	public RobotArm() {
		SerialPort port = SerialPort.getCommPort("/dev/ttyS4");
		port.openPort();

		out = port.getOutputStream();
		
		System.out.println(port.isOpen()); // true
	}
	
	public void move(int servo, int position, int time) throws InterruptedException {
		
		// PrintWriter to write strings
		try (PrintWriter p = new PrintWriter(out)) {
			// Test write - not working
			p.print("#1P1500T1000\r\n");
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
}
