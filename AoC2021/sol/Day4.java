import java.util.Iterator;

public class Day4 {

    public String playBingo(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        BingoInput input = scanner.ReadDay4();

        for (int i = 0; i < input.numbers.size(); i++) {
            int calledNumber = input.numbers.get(i);

            for (int j = 0; j < input.boards.size(); j++) {
                PairDay4 currentBoard = input.boards.get(j);
                currentBoard.markNumber(calledNumber);

                if (currentBoard.isWinning()) {
                    long unmarked = currentBoard.sumOfUnmarked();
                    long result = unmarked * calledNumber;
                    return "The question was:\n" +
                            " To guarantee victory against the giant squid, figure out which board will win first.\n What will your final score be if you choose that board?\n"
                            + "The answer is: \n " +
                            "The final score is: " + result;
                }
            }
        }
        return "Nobody won.";
    }

    public String lastWinner(String fileName) {
        InputScanner scanner = new InputScanner(fileName);
        BingoInput input = scanner.ReadDay4();

        for (int i = 0; i < input.numbers.size(); i++) {
            int calledNumber = input.numbers.get(i);

            Iterator<PairDay4> it = input.boards.iterator();
            if (input.boards.size() > 1) {
                while (it.hasNext()) {
                    PairDay4 currentBoard = it.next();
                    currentBoard.markNumber(calledNumber);

                    if (currentBoard.isWinning()) {
                        it.remove();
                    }
                }
            }else{
                PairDay4 currentBoard = input.boards.get(0);
                currentBoard.markNumber(calledNumber);

                if (currentBoard.isWinning()) {
                    long unmarked = currentBoard.sumOfUnmarked();
                    long result = unmarked * calledNumber;
                    return "The question was:\n" +
                            " Figure out which board will win last.\n Once it wins, what would its final score be?\n"
                            + "The answer is: \n " +
                            "Its final score would be: " + result;
                }
            }
        }
        return "Nobody won.";
    }

}
