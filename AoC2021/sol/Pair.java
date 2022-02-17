public class Pair {
    private long number;
    private String direction;

    public Pair(long number, String direction){
        this.number = number;
        this.direction = direction;
    }

    public long getNumber(){
        return number;
    }

    public String getDirection(){
        return direction;
    }
}
