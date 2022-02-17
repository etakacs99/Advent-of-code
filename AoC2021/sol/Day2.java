import java.util.List;

public class Day2 {
    private long horizontalPosition;
    private long depth;
    private long aim;

    public Day2() {
        horizontalPosition = 0;
        depth = 0;
        aim = 0;
    }

    public String getFinalHPAndDepthA(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<Pair> course = scanner.ReadDay2();

        for (Pair pair : course) {
            if (pair.getDirection().equals("forward")) {
                horizontalPosition += pair.getNumber();
            }
            if (pair.getDirection().equals("down")) {
                depth += pair.getNumber();
            }
            if (pair.getDirection().equals("up")) {
                depth -= pair.getNumber();
            }
        }

        long multiplicate = depth * horizontalPosition;

        return "The question was:\n" +
                " Calculate the horizontal position and depth you would have after following the planned course.\n What do you get if you multiply your final horizontal position by your final depth?\n"
                +
                "The answer is: \n " +
                multiplicate + " if I multiply my final horizontal position by my final depth";
    }

    public String getFinalHPAndDepthB(String fileName) {
        horizontalPosition = 0;
        depth = 0;
        aim = 0;
        InputScanner scanner = new InputScanner(fileName);
        List<Pair> course = scanner.ReadDay2();

        for (Pair pair : course) {
            if (pair.getDirection().equals("forward")) {
                horizontalPosition += pair.getNumber();
                depth += (aim*pair.getNumber());
            }
            if (pair.getDirection().equals("down")) {
                aim += pair.getNumber();
            }
            if (pair.getDirection().equals("up")) {
                aim -= pair.getNumber();
            }
        }

        long multiplicate = depth * horizontalPosition;

        return "The question was:\n" +
                " Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course.\n What do you get if you multiply your final horizontal position by your final depth?\n"
                +
                "The answer is: \n " +
                multiplicate + " if I multiply my final horizontal position by my final depth";
    }
}