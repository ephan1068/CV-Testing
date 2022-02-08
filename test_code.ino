#include "Enes100.h"
#include "Tank.h"
#include <math.h>


float i = Tank.readDistanceSensor(1); 
done = false;
float x = 0;
/* The code inside void setup() runs only once, before the code in void loop(). */
void setup() {
	Enes100.begin("Team Name Here", MATERIAL, 3, 8, 9); // Required before you can use any other Enes100 functions.
	Tank.begin(); // Required before you can use any other Tank functions.
}

/* The code in void loop() runs repeatedly forever */ 
void loop() { 
	Enes100.updateLocation();
	int xCoord = Enes100.location.x; //can store values of OTV
	
	//turn to face the left
	if(abs(Enes100.location.theta) > 1 && Enes100.location.x < 1.5){	
		turnLeft(0);
	}
	Enes100.updateLocation();
	//While not at x coord keep moving
	while(Enes100.location.x < 2) {
		Enes100.print("OTV is at");
		Enes100.updateLocation(); //What happens if we take this out?
		Enes100.println(Enes100.location.x);
		setBothMotors(200);	
	}
	
	//while not at y coord keep moving
	while (abs(Enes100.location.y - Enes100.destination.y) > .01) {
		Enes100.updateLocation();
		//if OTV is above destination turn to face down
		if((Enes100.location.y > Enes100.destination.y) && abs(Enes100.location.theta) < 1) {
			turnRight(-1.5);
		}
		//if OTV is below destnation turn to face up
		if((Enes100.location.y < Enes100.destination.y) && abs(Enes100.location.theta) < 1) {
			turnLeft(1.5);
		}
		Enes100.updateLocation();
		//move	
		setBothMotors(20);
	setBothMotors(0);
	
}

/* Another example function that prints pi. */
void printPi() {
	Enes100.println(M_PI);  // M_PI is from the math.h library above.
}
void setBothMotors(int speed) {
	Tank.setLeftMotorPWM(speed);
	Tank.setRightMotorPWM(speed);
}
// turns the OSV clockwise to face the given theta value given
void turnRight(double theta){
	if(abs(Enes100.location.theta) < abs(theta)){ //if we are facing downwards
		while((abs(Enes100.location.theta) -.1) < abs(theta)){
			Enes100.updateLocation();
			Tank.setLeftMotorPWM(200);
			Tank.setRightMotorPWM(-200);
		}	
	}else{//if OSV is facing up
		while((abs(Enes100.location.theta) -.01) > abs(theta)){
			Enes100.updateLocation();
			Tank.setLeftMotorPWM(200);
			Tank.setRightMotorPWM(-200);
		}	
	}
	
	setBothMotors(0);
}
//turns OSV counter-clockwise to face given theta value
void turnLeft(double theta){
	if(abs(Enes100.location.theta) < abs(theta)){ //if OSV is facing down
		while((abs(Enes100.location.theta) -.1) < abs(theta)){
			Enes100.updateLocation();
			Tank.setLeftMotorPWM(-100);
			Tank.setRightMotorPWM(100);
		}	
	}else{//if OSV facing up
		while((abs(Enes100.location.theta) -.01) > abs(theta)){
			Enes100.updateLocation();
			Tank.setLeftMotorPWM(-100);
			Tank.setRightMotorPWM(100);
		}	
	}
	
	setBothMotors(0);
}
void startAndEnd(){
	turnRight(3);
	turnRight(0);
}

void moveFoward(double distance){
	if(Enes100.location.x < distance){
		while(Enes100.location.x - distance < 0){
			Enes100.updateLocation();
			setBothMotors(250);
		}
	}else{
		while(Enes100.location.x - distance > 0){
			Enes100.updateLocation();
			setBothMotors(250);
		}
	}
	
	setBothMotors(0);
}

void moveUpDown(double coord){
	Enes100.println(Enes100.location.y);
	if(Enes100.location.y < coord){
		while(Enes100.location.y - coord < 0){
			Enes100.updateLocation();
			setBothMotors(250);
			Enes100.println(Enes100.location.y);
		}
	}else{
		while(Enes100.location.y - coord > 0){
			Enes100.updateLocation();
			setBothMotors(250);
			Enes100.println(Enes100.location.y);
		}
	}
	setBothMotors(0);
}
