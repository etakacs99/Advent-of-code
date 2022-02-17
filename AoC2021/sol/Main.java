import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int choise;
            do {
                System.out
                        .println("Choose between day [1-24].\n"
                                + "If you want to exit enter 0.\n"
                                + "Enter the number:");
                choise = Integer.parseInt(scanner.nextLine());
                menu(choise);
                System.out.println("----------------------------------------------------");
            } while (choise != 0);
        }
    }

    public static void menu(int choise) {
        switch (choise) {
            case 0:
                System.out.println("Exiting...");
                System.exit(0);
                break;
            case 1:
                System.out.println("DAY 1/A:");
                Day1 day1 = new Day1();
                System.out.println(day1.LargerThanPrevious("inputs/day_1.txt"));

                System.out.println("DAY 1/B:");
                System.out.println(day1.SumsLargerThanPrevious("inputs/day_1.txt"));
                break;
            case 2:
                System.out.println("DAY 2/A:");
                Day2 day2 = new Day2();
                System.out.println(day2.getFinalHPAndDepthA("inputs/day_2.txt"));

                System.out.println("DAY 2/B:");
                System.out.println(day2.getFinalHPAndDepthB("inputs/day_2.txt"));
                break;
            case 3:
                System.out.println("DAY 3/A:");
                Day3 day3 = new Day3();
                System.out.println(day3.calcOfTPC("inputs/day_3.txt"));

                System.out.println("DAY 3/B:");
                System.out.println(day3.lifeSupportRating("inputs/day_3.txt"));
                break;
            case 4:
                System.out.println("DAY 4/A:");
                Day4 day4 = new Day4();
                System.out.println(day4.playBingo("inputs/day_4.txt"));

                System.out.println("DAY 4/B:");
                System.out.println(day4.lastWinner("inputs/day_4.txt"));
                break;
            case 5:
                System.out.println("DAY 5/A:");
                Day5 day5A = new Day5();
                System.out.println(day5A.sumOfLineOverlaps("inputs/day_5.txt", true));

                System.out.println("DAY 5/B:");
                Day5 day5B = new Day5();
                System.out.println(day5B.sumOfLineOverlaps("inputs/day_5.txt", false));
                break;
            case 6: 
                System.out.println("DAY 6/A:");
                Day6 day6 = new Day6();
                System.out.println(day6.calcFishAfterDaysA("inputs/day_6.txt", 80));

                System.out.println("DAY 6/B:");
                System.out.println(day6.calcFishAfterDaysB("inputs/day_6.txt", 256));
                break;
            case 7: 
                System.out.println("DAY 7/A:");
                Day7 day7A = new Day7();
                System.out.println(day7A.calculateFuel("inputs/day_7.txt", false));

                System.out.println("DAY 7/B:");
                Day7 day7B = new Day7();
                System.out.println(day7B.calculateFuel("inputs/day_7.txt", true));
                break;
            case 8:
                System.out.println("DAY 8/A:");
                Day8 day8 = new Day8();
                System.out.println(day8.calculateEasyDigits("inputs/day_8.txt"));

                System.out.println("DAY 8/B:\n //TODO\n");
                break;
            case 9:
                System.out.println("DAY 9/A:");
                Day9 day9 = new Day9();
                System.out.println(day9.findLowPoints("inputs/day_9.txt"));

                System.out.println("DAY 9/B:\n //TODO\n");

                break;
            case 10: 
                System.out.println("DAY 10/A:");
                Day10 day10 = new Day10();
                System.out.println(day10.findCorruption("inputs/day_10.txt",false));

                System.out.println("DAY 10/B:");
                System.out.println(day10.findCorruption("inputs/day_10.txt",true));
                break;
        }
    }
}