import java.util.Iterator;

public class IteratorLongOddCompo implements Iterator<Long> {
    private Iterator<Long> sieve;
    Long firstPrime;
    Long nextPrime;
    Long lastOutputOfNext;

    public IteratorLongOddCompo(Iterator<Long> eratosieve) {
        this.sieve = eratosieve;
        firstPrime = sieve.next();
        nextPrime = sieve.next();
        lastOutputOfNext = nextPrime;
    }

    @Override
    public boolean hasNext() {
        return true;
    }

    @Override
    public Long next() {
        if (lastOutputOfNext.compareTo(nextPrime) == -1) {
            lastOutputOfNext = lastOutputOfNext + 2;
        }
        while (lastOutputOfNext.compareTo(nextPrime) == 0) {
            lastOutputOfNext = lastOutputOfNext + 2;
            Long buffer = nextPrime;
            nextPrime = sieve.next();
        }
        return lastOutputOfNext;
    }
}
