import java.util.*;
import java.lang.*;
import java.io.*;

public class BangBangController
{
	public static final int setpoint = 70; 
	public static boolean boiler_state = false; 
	
	public static void main (String[] args) throws java.lang.Exception
	{
		// start with any temperature
		changeBoiler(65); 
	}
	
	public static void changeBoiler(int current_temp){
		//int current_temp = temp; 
		
		if(current_temp == setpoint){
			System.out.println("Perfect temperature of 70!"); 
			/*System.out.println("equal");
			if(boiler_state == true){
				int new_temp = adjust_temp(true, current_temp);
				System.out.println("true"); 
				changeBoiler(new_temp);
			}
			else if(boiler_state == false){
				int new_temp = adjust_temp(false, current_temp);
				changeBoiler(new_temp); 
			}*/
		}else{
			if( (current_temp < setpoint) && (current_temp > 60) ){
				if(boiler_state == true){
					System.out.println("current temperature: " + current_temp);
					int moretemp = current_temp + 1; 
					changeBoiler(moretemp); 
				}else{
					System.out.println("current temperature: " + current_temp);
					int lesstemp = current_temp -1; 
					changeBoiler(lesstemp); 
				}
			}else if(current_temp == 60){
				System.out.println("reached minimum of 60");
				boiler_state = true; 
				int new_temp = adjust_temp(true, current_temp);
				changeBoiler(new_temp);
			}else if( (current_temp > setpoint) && (current_temp < 80)){
				if(boiler_state == true){
					System.out.println("current temperature: " + current_temp);
					int moretemp = current_temp + 1; 
					changeBoiler(moretemp);
				}else{
					System.out.println("current temperature " + current_temp);
					int lesstemp = current_temp-1; 
					changeBoiler(lesstemp);
				}
			}else if(current_temp == 80){
				System.out.println("reached maximum of 80");
				boiler_state = false; 
				int new_temp = adjust_temp(false, current_temp);
				changeBoiler(new_temp); 
			}
		}
	}
	
	public static int adjust_temp(boolean up_down, int current_temp){
		int temp = current_temp; 
		if(up_down == true){
			temp++; 
		}
		else if(up_down == false){
			temp--; 
		}
		return temp; 
	}
}
