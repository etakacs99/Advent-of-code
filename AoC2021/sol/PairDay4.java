import java.util.Arrays;

public class PairDay4 {
    final int[][] table = new int[5][5];
    final boolean[][] marks = new boolean[5][5];

    public void addRow(int row, String elements) {
        String[] elems = elements.split("\\s+");
        int i = 0, j = 0;
        while (i != 5) {
            if (!elems[j].isEmpty()) {
                table[row][i] = Integer.parseInt(elems[j]);
                ++i;
            }
            ++j;
        }
    }

    public void markNumber(int number) {
        for (int j = 0; j < 5; j++) {
            for (int i = 0; i < 5; i++) {
                if (table[j][i] == number) {
                    marks[j][i] = true;
                }
            }
        }
    }

    public boolean isWinning() {
        for (int i = 0; i < 5; i++) {
            int rowSum = 0, colSum = 0;
            for (int j = 0; j < 5; j++) {
                if (marks[i][j]) {
                    rowSum++;
                }
                
                if (marks[j][i]) {
                    colSum++;
                }
            }
            if (rowSum == 5 || colSum == 5) {
                return true;
            }
        }
        return false;
    }

    public int sumOfUnmarked() {
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!marks[i][j]) {
                    sum += table[i][j];
                }
            }
        }
        return sum;
    }

    @Override
    public String toString() {
        StringBuilder b = new StringBuilder();
        for (int[] row : table) {
            b.append(Arrays.toString(row));
        }
        b.append("\n\n");
        for (boolean[] row : marks) {
            b.append(Arrays.toString(row));
        }
        return b.toString();
    }
}
