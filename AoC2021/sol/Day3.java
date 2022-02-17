import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Day3 {
    private long[] numberOfZeros;
    private long[] numberOfOnes;

    public String lifeSupportRating(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<String> binaryNumbers = scanner.ReadDay3();

        List<String> oxygen = new ArrayList<>(binaryNumbers);
        List<String> co2 = new ArrayList<>(binaryNumbers);

        int idx = 0;

        while (oxygen.size() != 1) {
            int ones = 0, zeros = 0;
            for (String num : oxygen) {
                if (num.charAt(idx) == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }
            Iterator<String> iterator = oxygen.iterator();
            while (iterator.hasNext()) {
                String current = iterator.next();
                if (ones >= zeros) {
                    if (current.charAt(idx) == '0') {
                        iterator.remove();
                    }
                } else {
                    if (current.charAt(idx) == '1') {
                        iterator.remove();
                    }
                }
            }
            ++idx;
        }

        idx = 0;
        while (co2.size() != 1) {
            int ones = 0, zeros = 0;
            for (String num : co2) {
                if (num.charAt(idx) == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }
            Iterator<String> iterator = co2.iterator();
            while (iterator.hasNext()) {
                String current = iterator.next();
                if (ones >= zeros) {
                    if (current.charAt(idx) == '1') {
                        iterator.remove();
                    }
                } else {
                    if (current.charAt(idx) == '0') {
                        iterator.remove();
                    }
                }
            }
            ++idx;
        }

        long answer = Long.parseLong(oxygen.get(0), 2) * Long.parseLong(co2.get(0), 2);

        return "The question was:\n" +
                " What is the life support rating of the submarine?"
                +
                "The answer is: \n " +
                answer + " is the life support rating of the submarine.";
    }

    private void countCommonBits(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<String> binaryNumbers = scanner.ReadDay3();
        numberOfZeros = new long[binaryNumbers.get(0).length()];
        numberOfOnes = new long[binaryNumbers.get(0).length()];
        for (String num : binaryNumbers) {
            for (int i = 0; i < num.length(); i++) {
                if (num.charAt(i) == '0') {
                    numberOfZeros[i]++;
                } else {
                    numberOfOnes[i]++;
                }
            }
        }
    }

    public String calcOfTPC(String fileName) {
        countCommonBits(fileName);
        StringBuffer gammaBuffer = new StringBuffer(numberOfOnes.length);
        StringBuffer epsilonBuffer = new StringBuffer(numberOfOnes.length);
        for (int i = 0; i < numberOfOnes.length; i++) {
            if (numberOfOnes[i] > numberOfZeros[i]) {
                gammaBuffer.append('1');
                epsilonBuffer.append('0');
            } else {
                gammaBuffer.append('0');
                epsilonBuffer.append('1');
            }
        }

        long gamma = Long.parseLong(gammaBuffer.toString(), 2);
        long epsilon = Long.parseLong(epsilonBuffer.toString(), 2);

        long multiplicate = gamma * epsilon;

        return "The question was:\n" +
                " What is the power consumption of the submarine?"
                +
                "The answer is: \n " +
                multiplicate + " is the power consumption of the submarine.";
    }
}
