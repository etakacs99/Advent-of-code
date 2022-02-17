import java.util.ArrayList;
import java.util.List;

public class Day9 {

    private boolean LegalCoordinates(List<List<Long>> heightmap, int x, int y) {
        return x >= 0 && x < heightmap.size() && y >= 0 && y < heightmap.get(x).size();
    }

    public String findLowPoints(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        List<List<Long>> heightmap = scanner.ReadDay9();
        List<Coordinate> lowPoints = new ArrayList<>();

        for (int i = 0; i < heightmap.size(); i++) {
            for (int j = 0; j < heightmap.get(i).size(); j++) {
                long current = heightmap.get(i).get(j);
                int trueNeighbours = 0;
                int count = 0;
                if (LegalCoordinates(heightmap, i - 1, j)) {
                    ++trueNeighbours;
                    if (heightmap.get(i - 1).get(j) > current) {
                        ++count;
                    }
                }
                if (LegalCoordinates(heightmap, i, j - 1)) {
                    ++trueNeighbours;
                    if (heightmap.get(i).get(j - 1) > current) {
                        ++count;
                    }
                }
                if (LegalCoordinates(heightmap, i + 1, j)) {
                    ++trueNeighbours;
                    if (heightmap.get(i + 1).get(j) > current) {
                        ++count;
                    }
                }
                if (LegalCoordinates(heightmap, i, j + 1)) {
                    ++trueNeighbours;
                    if (heightmap.get(i).get(j + 1) > current) {
                        ++count;
                    }
                }
                if (count == trueNeighbours) {
                    lowPoints.add(new Coordinate(i, j));
                }
            }
        }

        long sum = 0;
        for (Coordinate lowPoint : lowPoints) {
            sum += heightmap.get(lowPoint.x).get(lowPoint.y) + 1;
        }
        return "The question was:\n" +
                " Find all of the low points on your heightmap.\n What is the sum of the risk levels of all low points on your heightmap?\n"
                + "The answer is: \n " +
                sum + " is the sum of the risk levels of all low points on my heightmap.";
    }

}
