import java.util.List;

public class Day8 {
    
    public String calculateEasyDigits(String fileName){
        InputScanner scanner = new InputScanner(fileName);
        List<List<String>> clocks = scanner.ReadDay8();
        long sumOfEasyDigits = 0;
        for (List<String> list : clocks) {
            for(int i = 10; i < list.size(); i++) {
                int length = list.get(i).length();
                if(length == 2 || length == 4 || length == 3|| length == 7){
                    sumOfEasyDigits++;
                }
            }
        }

        return "The question was:\n" +
                " In the output values, how many times do digits 1, 4, 7, or 8 appear?\n"
                + "The answer is: \n " +
                sumOfEasyDigits + " times do the digits 1, 4, 7, or 8 appear."; 
    }
}
