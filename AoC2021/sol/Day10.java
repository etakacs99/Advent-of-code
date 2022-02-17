import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class Day10 {
    public String findCorruption(String fileName, boolean isB) {
        InputScanner scanner = new InputScanner(fileName);
        List<String> syntaxErrors = scanner.ReadDay10();

        long illegalScore = 0;
        List<Long> modifiedChunks = new ArrayList<>();

        for (String chunck : syntaxErrors) {
            boolean chunkIsIllegal = false;
            Stack<Character> openBracketStack = new Stack<>();

            for (int i = 0; i < chunck.length(); i++) {
                switch (chunck.charAt(i)) {
                    case '(':
                    case '[':
                    case '{':
                    case '<':
                        openBracketStack.push(chunck.charAt(i));
                        break;
                    case ')':
                        if (openBracketStack.peek() == '(') {
                            openBracketStack.pop();
                        } else {
                            illegalScore += 3;
                            chunkIsIllegal = true;
                        }
                        break;
                    case ']':
                        if (openBracketStack.peek() == '[') {
                            openBracketStack.pop();
                        } else {
                            illegalScore += 57;
                            chunkIsIllegal = true;
                        }
                        break;
                    case '}':
                        if (openBracketStack.peek() == '{') {
                            openBracketStack.pop();
                        } else {
                            illegalScore += 1197;
                            chunkIsIllegal = true;
                        }
                        break;
                    case '>':
                        if (openBracketStack.peek() == '<') {
                            openBracketStack.pop();
                        } else {
                            illegalScore += 25137;
                            chunkIsIllegal = true;
                        }
                        break;
                }
                if (chunkIsIllegal) {
                    break;
                }
            }
            if (isB) {
                if (!chunkIsIllegal) {
                    long sumOfAddedBrackets = 0;
                    while (!openBracketStack.empty()) {
                        char bracket = openBracketStack.pop();
                        sumOfAddedBrackets *= 5;
                        switch (bracket) {
                            case '(':
                                sumOfAddedBrackets += 1;
                                break;
                            case '{':
                                sumOfAddedBrackets += 3;
                                break;
                            case '<':
                                sumOfAddedBrackets += 4;
                                break;
                            case '[':
                                sumOfAddedBrackets += 2;
                                break;
                        }
                    }
                    modifiedChunks.add(sumOfAddedBrackets);
                }
            }
        }
        if (!isB) {
            return "The question was:\n" +
                    " Find the first illegal character in each corrupted line of the navigation subsystem.\n What is the total syntax error score for those errors?\n"
                    + "The answer is: \n " +
                    " The total syntax error score for those errors is: " + illegalScore;

        } else {
            Collections.sort(modifiedChunks);
            long middleScore = modifiedChunks.get(modifiedChunks.size() / 2);

            return "The question was:\n" +
                    " Find the completion string for each incomplete line, score the completion strings, and sort the scores.\n What is the middle score?\n"
                    + "The answer is: \n " +
                    " The middle score is: " + middleScore;
        }
    }
}
