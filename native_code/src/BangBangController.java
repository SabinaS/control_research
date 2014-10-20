
public class BangBangController
{

    public BangBangController()
    {
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args)
    {
        /* long start = System.currentTimeMillis(); long end = start + 1; // milliseconds while
         * (System.currentTimeMillis() < end) { CurrentTempChanged currTemp = new Thermostat();
         * Environment env = new Environment(currTemp); env.setStartTemp(65);
         * env.setFurnaceFanStates(false, false); env.sendNewTemp(); } */

        CurrentTempChanged currTemp = new Thermostat();
        Environment env = new Environment(currTemp);
        env.setStartTemp(65);
        env.setFurnaceFanStates(false, false);
        env.sendNewTemp();

    }
}
