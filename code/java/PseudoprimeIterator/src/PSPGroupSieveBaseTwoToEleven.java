import java.math.BigInteger;
import java.util.Arrays;
import java.util.Iterator;

public class PSPGroupSieveBaseTwoToEleven implements Iterator<Long> {
    private Iterator<Long> sieve;
    private BigInteger basetwo = BigInteger.valueOf(2);
    private BigInteger basethree = BigInteger.valueOf(3);
    private BigInteger basefive = BigInteger.valueOf(5);
    private BigInteger baseseven = BigInteger.valueOf(7);
    private BigInteger baseeleven = BigInteger.valueOf(11);


    Long lastOutputOfNext;

    public PSPGroupSieveBaseTwoToEleven(Iterator<Long> eratosieve) {
        this.sieve = eratosieve;
    }

    @Override
    public boolean hasNext() {
        return true;
    }

    @Override
    public Long next() {
        Long nextNum = sieve.next();
        Boolean success = false;
        while (!success) {
            for (BigInteger bigInteger : Arrays.asList(this.basethree, this.basetwo, this.basefive, this.baseseven, this.baseeleven)) {
                if (!success) {
                    if (bigInteger.modPow(BigInteger.valueOf(nextNum).subtract(BigInteger.ONE), BigInteger.valueOf(nextNum)).compareTo(BigInteger.ONE) == 0) {
                        success = true;
                        break;
                    }
                }
            }
            if (!success) {
                nextNum = sieve.next();
            }
        }

        return nextNum;
    }
}