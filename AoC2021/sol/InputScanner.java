import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class InputScanner {
    private final File myFile;

    public InputScanner(String fileName) {
        myFile = new File(fileName);
    }

    public List<Integer> ReadDay1() {
        List<Integer> list = new ArrayList<>();

        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                list.add(Integer.parseInt(data));
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return list;
    }

    public List<Pair> ReadDay2() {
        List<Pair> list = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String[] data = myReader.nextLine().split(" ");

                Pair myPair = new Pair(Long.parseLong(data[1]), data[0]);
                list.add(myPair);
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return list;
    }

    public List<String> ReadDay3() {
        List<String> list = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                list.add(data);
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return list;
    }

    public BingoInput ReadDay4() {
        BingoInput bingoInput = new BingoInput();
        try (Scanner myReader = new Scanner(myFile)) {
            String[] line = myReader.nextLine().split(",");
            List<Integer> numbers = new ArrayList<>();
            for (int i = 0; i < line.length; i++) {
                numbers.add(Integer.parseInt(line[i]));
            }

            bingoInput.numbers = numbers;
            String boardLine = myReader.nextLine();
            List<PairDay4> list = new ArrayList<>();
            while (boardLine != null && myReader.hasNextLine()) {
                if (!boardLine.isEmpty()) {
                    PairDay4 board = new PairDay4();
                    for (int i = 0; i < 5; i++) {
                        board.addRow(i, boardLine);
                        if (myReader.hasNext()) {
                            boardLine = myReader.nextLine();
                        } else {
                            break;
                        }
                    }
                    list.add(board);
                } else {
                    boardLine = myReader.nextLine();
                }
            }
            bingoInput.boards = list;

        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return bingoInput;
    }

    public List<Line> ReadDay5() {
        List<Line> lines = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String[] inputLine = myReader.nextLine().split(" -> ");
                String[] from = inputLine[0].split(",");
                String[] to = inputLine[1].split(",");

                Coordinate f = new Coordinate(Integer.parseInt(from[0]), Integer.parseInt(from[1]));
                Coordinate t = new Coordinate(Integer.parseInt(to[0]), Integer.parseInt(to[1]));
                Line line = new Line(f, t);
                lines.add(line);
            }

        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return lines;
    }

    public List<Integer> ReadDay6A() {
        List<Integer> fishDays = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String[] inputLine = myReader.nextLine().split(",");
                for (int i = 0; i < inputLine.length; i++) {
                    fishDays.add(Integer.parseInt(inputLine[i]));
                }
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return fishDays;
    }

    public long[] ReadDay6B() {
        long[] fishDays = new long[9];
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String[] inputLine = myReader.nextLine().split(",");
                for (int i = 0; i < inputLine.length; i++) {
                    int fish = Integer.parseInt(inputLine[i]);
                    fishDays[fish]++;
                }
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return fishDays;
    }

    public long[] ReadDay7() {
        long[] crabFuel = new long[2000];
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String[] inputLine = myReader.nextLine().split(",");
                for (int i = 0; i < inputLine.length; i++) {
                    int crab = Integer.parseInt(inputLine[i]);
                    crabFuel[crab]++;
                }
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return crabFuel;
    }

    public List<List<String>> ReadDay8() {
        List<List<String>> clocks = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                List<String> clock = new ArrayList<>(14);
                String[] data = myReader.nextLine().split(" ");
                for (int ii = 0; ii < 15; ++ii) {
                    if (ii == 10) {
                        continue;
                    }
                    clock.add(data[ii]);
                }
                clocks.add(clock);
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return clocks;
    }

    public List<List<Long>> ReadDay9() {
        List<List<Long>> heightmap = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                List<Long> row = new ArrayList<>();
                String data = myReader.nextLine();
                for (int ii = 0; ii < data.length(); ++ii) {
                    row.add(Long.valueOf(String.valueOf(data.charAt(ii)), 10));
                }
                heightmap.add(row);
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return heightmap;
    }

    public List<String> ReadDay10() {
        List<String> navSystem = new ArrayList<>();
        try (Scanner myReader = new Scanner(myFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                navSystem.add(data);
            }
        } catch (NumberFormatException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured: ");
            e.printStackTrace();
        }
        return navSystem;
    }
}