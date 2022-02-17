import java.util.List;

public class Day5 {
    private int[][] drawing = new int[1000][1000];

    public void drawLines(String fileName, boolean isB) {
        InputScanner scanner = new InputScanner(fileName);
        List<Line> input = scanner.ReadDay5();

        for (Line line : input) {
            if (line.isHorizontal()) {
                int start = 0;
                int end = 0;
                if (line.from.x > line.to.x) {
                    start = line.to.x;
                    end = line.from.x;
                } else {
                    start = line.from.x;
                    end = line.to.x;
                }
                for (int i = start; i <= end; i++) {
                    drawing[i][line.from.y]++;
                }
            } else if (line.isVertical()) {
                int start = 0;
                int end = 0;
                if (line.from.y > line.to.y) {
                    start = line.to.y;
                    end = line.from.y;
                } else {
                    start = line.from.y;
                    end = line.to.y;
                }

                for (int i = start; i <= end; i++) {
                    drawing[line.from.x][i]++;
                }
            } else if (isB && line.isDiagonal()) {
                if ((line.from.x < line.to.x && line.from.y < line.to.y) ||
                        (line.from.x > line.to.x && line.from.y > line.to.y)) {
                    int startX = 0;
                    int endX = 0;
                    int startY = 0;
                    int endY = 0;
                    if (line.from.x > line.to.x) {
                        startX = line.to.x;
                        endX = line.from.x;
                        startY = line.to.y;
                        endY = line.from.y;
                    } else {
                        startX = line.from.x;
                        endX = line.to.x;
                        startY = line.from.y;
                        endY = line.to.y;
                    }
                    for (int i = startX, j = startY; i <= endX && j <= endY; i++, j++) {
                        drawing[i][j]++;
                    }

                } else {
                    int startX = 0;
                    int endX = 0;
                    int startY = 0;
                    int endY = 0;
                    if (line.from.x > line.to.x) {
                        startX = line.to.x;
                        endX = line.from.x;
                        startY = line.to.y;
                        endY = line.from.y;
                    } else {
                        startX = line.from.x;
                        endX = line.to.x;
                        startY = line.from.y;
                        endY = line.to.y;
                    }
                    for (int i = startX, j = startY; i <= endX && j >= endY; i++, j--) {
                        drawing[i][j]++;
                    }
                }
            }
        }
    }

    public String sumOfLineOverlaps(String fileName, boolean isA) {
        if (isA) {
            drawLines(fileName, false);
        } else {
            drawLines(fileName, true);
        }
        int sum = 0;

        for (int i = 0; i < drawing.length; i++) {
            for (int j = 0; j < drawing[i].length; j++) {
                if (drawing[i][j] >= 2) {
                    sum++;
                }
            }
        }
        return "The question was:\n" +
                " Consider only horizontal and vertical lines.\n At how many points do at least two lines overlap?\n"
                + "The answer is: \n " +
                " At " + sum + " poinst do at least two lines overlap.";
    }
}
