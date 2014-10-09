public class Thermostat implements CurrentTempChanged
{
    private Environment env;

    public Thermostat()
    {
        env = new Environment(this);
    }

    /* 70 is our optimal temp. */
    @Override
    public void currentTempChanged(int newTemp)
    {
        boolean furnaceState = env.getFurnaceState();
        boolean fanState = env.getFanState();

        System.out.println("Thermostat newTemp: " + newTemp);

        // We want a range where nothing is on
        if (newTemp < 68) {
            furnaceState = true;
            fanState = false;
        } else if (newTemp > 72) {
            fanState = true;
            furnaceState = false;
        } else if (newTemp == 70)
            System.out.println("We've reached the perfect temp!");

        // Send the new furnace and fan states to Environment
        env.setFurnaceFanStates(furnaceState, fanState);
    }
}
