public class PSPDataOnSQLite {
    public int key;
    public Long val;
    public String source;
    public String insertTime;
    public Long base;
    public Long bound;

    public void setKey(int key1) {
        this.key = key1;
    }

    public void setVal(Long val1) {
        this.val = val1;
    }

    public void setSource(String source1) {
        this.source = source1;
    }

    public void setInsertTime(String insertTime1) {
        this.insertTime = insertTime1;
    }

    public void setBase(Long base) {
        this.base = base;
    }

    public void setBound(Long bound) {
        this.bound = bound;
    }

    public int getKey() {
        return key;
    }

    public Long getVal() {
        return val;
    }

    public String getSource() {
        return source;
    }

    public String getInsertTime() {
        return insertTime;
    }

    public Long getBase() {
        return base;
    }

    public Long getBound() {
        return bound;
    }

    public String toString() {
        return this.key + "|" + this.val + "|" + this.source + "|" + this.insertTime + "|" +
                +this.base + "|" + this.bound + "|";
    }
}
