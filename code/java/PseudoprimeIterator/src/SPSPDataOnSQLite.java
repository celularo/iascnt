import java.math.BigInteger;

public class SPSPDataOnSQLite {
    public int key = 0;
    public Long val = 1L;
    public String source = "Testerclass";
    public String insertTime = null;
    public Long base = 1L;
    public Long core = 1L;
    public Long absDepth = 1L;
    public Long coreModPow = 1L;
    public Long succDepth = 1L;
    public Boolean Property = false;

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

    public String toString() {
        return this.key + "|" + this.val + "|" + this.source + "|" + this.insertTime + "|" +
                +this.base + "|";
    }
}
