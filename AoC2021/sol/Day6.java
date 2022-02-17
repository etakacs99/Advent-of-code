import java.util.ArrayList;
import java.util.List;

public class Day6 {

    public String calcFishAfterDaysA(String fileName, int days) {
        InputScanner scanner = new InputScanner(fileName);
        List<Integer> fishDays = scanner.ReadDay6A();
        List<Integer> newFishes = new ArrayList<>();
        for (int i = 0; i < days; i++) {
            for (int j = 0; j < fishDays.size(); j++) {
                int value = fishDays.get(j);
                if (value == 0) {
                    fishDays.set(j, 6);
                    newFishes.add(8);
                } else {
                    fishDays.set(j, value - 1);
                }
            }
            fishDays.addAll(newFishes);
            newFishes.clear();
        }

        return "The question was:\n" +
                " Find a way to simulate lanternfish.\n How many lanternfish would there be after 80 days?\n"
                + "The answer is: \n " +
                fishDays.size() + " lanternfish would there be after 80 days.";
    }

    public String calcFishAfterDaysB(String fileName, int days) {
        InputScanner scanner = new InputScanner(fileName);
        long[] fishDays = scanner.ReadDay6B();
        for (int i = 0; i < days; i++) {
            long shifted = fishDays[0];
            for (int j = 1; j < fishDays.length; j++) {
                fishDays[j - 1] = fishDays[j];
            }
            fishDays[6] += shifted;
            fishDays[8] = shifted;
        }

        long sum = 0;
        for(int ii = 0; ii < fishDays.length; ii++){
            sum += fishDays[ii];
        }

        return "The question was:\n" +
                " Find a way to simulate lanternfish.\n How many lanternfish would there be after 256 days?\n"
                + "The answer is: \n " +
                sum + " lanternfish would there be after 80 days.";
    }

}
