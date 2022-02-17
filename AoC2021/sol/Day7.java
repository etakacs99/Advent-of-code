public class Day7 {
    public String calculateFuel(String fileName, boolean isB) {
        InputScanner scanner = new InputScanner(fileName);
        long[] crabDist = scanner.ReadDay7();
        long[] sumOfSteps = new long[crabDist.length];

        for (int i = 0; i < sumOfSteps.length; i++) {
            for (int j = 0; j < crabDist.length; j++) {
                if (isB) {
                    long step = Math.abs(j - i);
                    sumOfSteps[i] += (crabDist[j] * (step * (step + 1)) / 2);
                } else {
                    sumOfSteps[i] += (Math.abs(j - i) * crabDist[j]);
                }
            }
        }

        long leastStep = sumOfSteps[0];
        for (int i = 1; i < sumOfSteps.length; i++) {
            if (leastStep > sumOfSteps[i]) {
                leastStep = sumOfSteps[i];
            }
        }
        return "The question was:\n" +
                " Determine the horizontal position that the crabs can align to using the least fuel possible.\n How much fuel must they spend to align to that position?\n"
                + "The answer is: \n " +
                leastStep + " fuel must be spend to aling to that position.";
    }
}
