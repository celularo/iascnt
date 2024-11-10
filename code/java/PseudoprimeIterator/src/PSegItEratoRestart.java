import java.util.ArrayList;
import java.util.Iterator;

public class PSegItEratoRestart implements Iterator<Long> {
    private final int BFSZ = 1 << 16;
    private final int BFBTS = BFSZ * 32;
    private final int BFRNG = BFBTS * 2;
    private long bi = -1;
    private long lowi = 0;
    private final ArrayList<Integer> bpa = new ArrayList<>();
    private Iterator<Long> bps;
    private final int[] buf = new int[BFSZ];

    private Boolean myrest;

    private Long myrestfactor;

    public PSegItEratoRestart(Boolean restart, Long bound_old) {
        this.myrest = restart;
        this.myrestfactor = (long) Math.floor(bound_old / (this.BFRNG));
    }

    @Override
    public boolean hasNext() {
        return true;
    }

    @Override
    public Long next() {
        if (this.myrest) {
            this.bi = 0;
            this.lowi += this.myrestfactor * BFBTS;
            System.out.println(this.lowi);
            this.myrest = false;
            return this.next();
        }
        if (this.bi < 1) {
            if (this.bi < 0) {
                this.bi = 0;
                return 2L;
            }
            long nxt = 3 + (this.lowi << 1) + BFRNG;
            if (this.lowi <= 0) {
                for (int i = 0, p = 3, sqr = 9; sqr < nxt; i++, p += 2, sqr = p * p)
                    if ((this.buf[i >>> 5] & (1 << (i & 31))) == 0)
                        for (int j = (sqr - 3) >> 1; j < BFBTS; j += p)
                            this.buf[j >>> 5] |= 1 << (j & 31);
            } else {

                for (int i = 0; i < this.buf.length && buf[i] != 0; i++)
                    this.buf[i] = 0;

                if (this.bpa.isEmpty()) {
                    this.bps = new PSegItEratoRestart(false, 0L);
                    this.bps.next();
                    this.bpa.add(this.bps.next().intValue());
                }
                for (long p = this.bpa.get(this.bpa.size() - 1), sqr = p * p; sqr < nxt;
                     p = this.bps.next(), this.bpa.add((int) p), sqr = p * p)
                    ;

                for (int i = 0; i < this.bpa.size() - 1; i++) {
                    long p = this.bpa.get(i);
                    long s = (p * p - 3) >>> 1;
                    if (s >= this.lowi)
                        s -= this.lowi;
                    else {
                        long r = (this.lowi - s) % p;
                        s = (r != 0) ? p - r : 0;
                    }
                    for (int j = (int) s; j < BFBTS; j += p)
                        this.buf[j >>> 5] |= 1 << (j & 31);
                }
            }
        }
        while ((this.bi < BFBTS) &&
                ((this.buf[(int) this.bi >>> 5] & (1 << ((int) this.bi & 31))) != 0))
            this.bi++;
        if (this.bi < BFBTS)
            return 3 + ((this.lowi + this.bi++) << 1);
        else {
            this.bi = 0;
            this.lowi += BFBTS;
            return this.next();
        }
    }

}
