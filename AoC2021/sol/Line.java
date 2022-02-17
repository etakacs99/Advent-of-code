public class Line {
    final Coordinate from;
    final Coordinate to;

    public Line(Coordinate from, Coordinate to){
        this.to = to;
        this.from = from;
    }

    public boolean isHorizontal(){
        if(to.y == from.y){
            return true;
        }
        return false;
    }

    public boolean isVertical(){
        if(to.x == from.x){
            return true;
        }
        return false;
    }

    public boolean isDiagonal(){
        return Math.abs(from.x - to.x) == Math.abs(from.y - to.y);
    }
}
