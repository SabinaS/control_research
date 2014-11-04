#include <stdio.h>
#include <stdlib.h>	
#include "bang_bang_controller.h"

int 		furnace_state; 		//0 is false, 1 is true
int 		fan_state; 		//0 is false, 1 is true
int		furnace_running; 	//0 is false, 1 is true
int 		fan_running; 		//0 is false, 1 is true
int 		new_temp; 
int 		old_temp;
int 		furnace_time;
int 		fan_time;
int 		run_time;

void sendNewTemp();
void currentTempChanged(int newTemp);

void setStartTemp(int startTemp)
{
	new_temp = startTemp; 
	old_temp = startTemp;
}

// We send the newly generated temp to currentTempChanged()
void sendNewTemp()
{
	if (run_time == 100){ // preventing stackoverflow
		printf("Ran 100 times\n");
		exit(0);
	}else
		run_time++;
	
	int newTemp = generateTemp();
	currentTempChanged(newTemp); 
}

// We generate a new temp based on the furnace/fan and outside factors
int generateTemp()
{
	int newTemp = old_temp;
	if (furnace_running == 1)
		newTemp = old_temp + 1;
	else if (fan_running == 1)
		newTemp = old_temp - 1;
	
	int tempTemp = outsideFactors(newTemp);
	//printf("tempTemp: %d\n", tempTemp);
	old_temp = tempTemp;
	return tempTemp;
}

// If the furnace or fan have been running for a while the rate of
// temp change should increase.
// This mirrors the proportional PID method
int outsideFactors(int newTemp)
{
	int currTemp = newTemp; 
	if (furnace_running == 1) {
		furnace_time = updateFurnaceTime(1);
		currTemp = currTemp + furnace_time / 2;
	} else if (fan_running == 1) {
		fan_time = updateFanTime(1);
		currTemp = currTemp - fan_time / 2;
	}
	return currTemp;
}

// If the furnace has been continually on, we want to increase its time
// so we can change the temperature proportionally
int updateFurnaceTime()
{
	if (furnace_running == 1)
		furnace_time++;
	return furnace_time;
}

// If the fan has been continually on, we want to increase its time
// so we can change the temperature proportionally
int updateFanTime()
{
	if (fan_running == 1)
		fan_time++;
	return fan_time;
}

// Get the furnace and fan states, then send a newTemp
void setFurnaceFanStates(int furnaceState, int fanState)
{
	furnace_running = furnaceState;
	if (furnace_running == 0)
		furnace_time = 0;
	
	fan_running = fanState;
	if (fan_running == 0)
		fan_time = 0;
	
	sendNewTemp();
}

void currentTempChanged(int newTemp){
	// We want a range where nothing is on
	if (newTemp < 68) {
		printf("Runtime: %d, Temp < 68: %d\n", run_time, newTemp);
		furnace_state = 1;
		fan_state = 0;
		setFurnaceFanStates(furnace_state, fan_state);
		//sendNewTemp(); 
	} else if (newTemp > 72) {
		printf("Runtime: %d, Temp > 72: %d\n", run_time, newTemp);
		fan_state = 1;
		furnace_state = 0;
		setFurnaceFanStates(furnace_state, fan_state);
		//sendNewTemp(); 
	} else if (newTemp == 70)
		printf("Runtime: %d, We've reached the perfect temp!\n", run_time);
		sendNewTemp();
	} else{
		printf("Runtime: %d, Temp: %d\n", run_time, newTemp);
		sendNewTemp(); 
	}
}

void main()
{
	
	/* Initialize vars */
	int init_furnace_state = 0;
	int init_fan_state = 0;
	furnace_time = 0;
	fan_time = 0;
	run_time = 0;
	
	setStartTemp(65);
	setFurnaceFanStates(init_furnace_state, init_fan_state);
	//sendNewTemp();
}


