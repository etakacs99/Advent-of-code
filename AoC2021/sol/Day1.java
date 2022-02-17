import java.util.ArrayList;
import java.util.List;


public class Day1 {

    public String LargerThanPrevious(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<Integer> measurements = scanner.ReadDay1();
        int numberOfLTP = 0;
        Integer prev = 0;
        for (Integer depth : measurements) {
            if (prev != 0 && prev < depth) {
                numberOfLTP++;
            }
            prev = depth;
        }
        return "The question was:\n" +
                " How many measurements are larger than the previous measurement?\n" +
                "The answer is: \n " +
                numberOfLTP + " measurements are larger than the previous measurement.";
    }

    public String SumsLargerThanPrevious(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<Integer> measurements = scanner.ReadDay1();
        int numOfSums = 0;

        List<Integer> sumsOf3Measurments = new ArrayList<>();

        sumsOf3Measurments.add(measurements.get(0));
        sumsOf3Measurments.add(measurements.get(1));
        sumsOf3Measurments.add(measurements.get(2));
        int prev = sumsOf3Measurments.get(0) + sumsOf3Measurments.get(1) + sumsOf3Measurments.get(2);

        for (int i = 3; i < measurements.size(); i++) {
            int current = sumsOf3Measurments.get(1) + sumsOf3Measurments.get(2) + measurements.get(i);
            if (prev < current) {
                numOfSums++;
            }
            sumsOf3Measurments.remove(0);
            sumsOf3Measurments.add(measurements.get(i));
            prev = current;
        }
        return "The question was:\n" +
                " Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?\n"
                +
                "The answer is: \n " +
                numOfSums + " sums are larger than the previous sum.";
    }

}
