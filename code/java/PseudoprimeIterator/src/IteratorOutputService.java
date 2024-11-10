import java.math.BigInteger;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Iterator;

public class IteratorOutputService {
    private Iterator<Long> SieveEngine;
    private Long SieveUpTo;
    private BigInteger PSPType;
    private String Bases;

    public IteratorOutputService(Iterator<Long> sieve, Long bound, BigInteger type, String bases) {
        this.SieveEngine = sieve;
        this.SieveUpTo = bound;
        this.PSPType = type;
        this.Bases = bases;
    }

    public void PrintlnFirstTsd() {
        for (int i = 0; i < 1000; i++) {
            Long nextNum = SieveEngine.next();
            System.out.println(i + ": " + nextNum);
        }

    }

    public void PrintlnTotalNumberOfMembersInTime() {
        long strt = System.currentTimeMillis();
        int count = 0;
        while (SieveEngine.next() <= SieveUpTo) count++;
        long elpsd = System.currentTimeMillis() - strt;
        System.out.println("Found " + count + " primes up to " + SieveUpTo + " in " + elpsd + " milliseconds.");
    }

    public void Write2SQLiteAllFirst() {

        Connection conny = SQLiteConnect.connect();
        try {
            conny.setAutoCommit(false);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        SQLiteInsertApp sqliteinserter = new SQLiteInsertApp(conny);
        for (Long i = 0L; i < SieveUpTo; i++) {
            Long nextNum = SieveEngine.next();
            sqliteinserter.insert_into_table("psp", i, nextNum,
                    this.SieveEngine.getClass().getName().concat("//Basis: ").concat(this.PSPType.toString()).concat("//Bound: ").concat(this.SieveUpTo.toString()),
                    this.PSPType.toString(), this.SieveUpTo);
        }
        try {
            conny.commit();
            conny.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

    public void Write2SQLiteBundleUpTo() {

        Connection conny = SQLiteConnect.connect();
        try {
            conny.setAutoCommit(false);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        SQLiteInsertApp sqliteinserter = new SQLiteInsertApp(conny);
        Long counter = 0L;
        Long nextNum = 0L;
        double buffie = 0;
        while (nextNum <= SieveUpTo) {
            nextNum = SieveEngine.next();
            counter++;
            sqliteinserter.insert_into_table("psp_base_bundles", counter, nextNum,
                    this.SieveEngine.getClass().getName().concat("//Basis: ").concat(this.Bases).concat("//Bound: ").concat(this.SieveUpTo.toString()),
                    this.Bases, this.SieveUpTo);
        }
        try {
            conny.commit();
            conny.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }
}
