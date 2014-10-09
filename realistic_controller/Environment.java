public class Environment implements FurnaceFanStates
{
    private CurrentTempChanged curr;
    private static boolean     furnace_running = false;
    private static boolean     fan_running     = false;
    private static int         oldTemp         = 0;
    private static int         furnaceTime     = 0;    /* The total time the furnace has been
                                                         * running continuously */
    private static int         fanTime         = 0;    /* The total time the fan has been running
                                                         * continuously */
    private static int         runtime         = 0;    /* The total time the system has been
                                                         * running continuously */

    public Environment(CurrentTempChanged temp)
    {
        curr = temp;
    }

    // We begin with a starting temp
    public void setStartTemp(int startTemp)
    {
        Environment.oldTemp = startTemp;
    }

    // We send the newly generated temp to the Thermostat
    public void sendNewTemp()
    {
        if (Environment.runtime == 100) // preventing stackoverflow
            System.exit(0);
        else
            Environment.runtime++;

        int newTemp = generateTemp();
        curr.currentTempChanged(newTemp);
    }

    // We generate a new temp based on the furnace/fan and outside factors
    public int generateTemp()
    {
        int newTemp = Environment.oldTemp;

        if (Environment.furnace_running)
            newTemp = Environment.oldTemp + 1;
        else if (Environment.fan_running)
            newTemp = Environment.oldTemp - 1;

        int tempTemp = outsideFactors(newTemp);
        Environment.oldTemp = tempTemp;

        return tempTemp;
    }

    // If the furnace or fan have been running for a while the rate of
    // temp change should increase.
    public int outsideFactors(int newTemp)
    {

        if (Environment.furnace_running) {
            Environment.furnaceTime = updateFurnaceTime(true);
            newTemp = newTemp + Environment.furnaceTime / 2;
        } else if (Environment.fan_running) {
            Environment.fanTime = updateFanTime(true);
            newTemp = newTemp - Environment.fanTime / 2;
        }

        return newTemp;
    }

    // If the furnace has been continually on, we want to increase its time
    // so we can change the temperature proportionally
    int updateFurnaceTime(boolean furnace_running)
    {
        if (furnace_running)
            Environment.furnaceTime++;
        return Environment.furnaceTime;
    }

    // If the fan has been continually on, we want to increase its time
    // so we can change the temperature proportionally
    int updateFanTime(boolean fan_running)
    {
        if (fan_running)
            Environment.fanTime++;
        return Environment.fanTime;
    }

    // Get the furnace and fan states, then send a newTemp to Thermostat
    @Override
    public void setFurnaceFanStates(boolean furnaceState, boolean fanState)
    {
        Environment.furnace_running = furnaceState;
        if (Environment.furnace_running == false)
            Environment.furnaceTime = 0;

        Environment.fan_running = fanState;
        if (Environment.fan_running == false)
            Environment.fanTime = 0;

        sendNewTemp();
    }

    public boolean getFurnaceState()
    {
        return Environment.furnace_running;
    }

    public boolean getFanState()
    {
        return Environment.fan_running;
    }
}
