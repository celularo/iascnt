import java.math.BigInteger;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Iterator;

public class StrongOutputService extends IteratorOutputService {
    private Iterator<PseudoPrime> Strongs;

    public StrongOutputService(Iterator<PseudoPrime> strongs) {
        this(null, null, null);
        Strongs = strongs;
    }

    public StrongOutputService(Iterator<Long> sieve, Long bound, BigInteger type) {
        super(sieve, bound, type, "hello");
    }

    public void Write2SQLiteStrongs() {
        Connection conny = SQLiteConnect.connect();
        try {
            conny.setAutoCommit(false);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        SQLiteInsertApp sqliteinserter = new SQLiteInsertApp(conny);
        Long counter = 0L;
        while (Strongs.hasNext() == true) {
            counter++;
            PseudoPrime nextstrong = Strongs.next();
            nextstrong.setMySQLiteData(this.getClass().getName());
            sqliteinserter.insert_spsp_into_table("spsp", counter, nextstrong.mySQLiteData.source, nextstrong.mySQLiteData);
        }
        try {
            conny.commit();
            conny.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }

    public void Write2SQLiteTypes(Long bound) {
        Connection conny = SQLiteConnect.connect();
        try {
            conny.setAutoCommit(false);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        SQLiteInsertApp sqliteinserter = new SQLiteInsertApp(conny);
        Long counter = 0L;
        while (Strongs.hasNext() == true) {
            counter++;
            PseudoPrime nextpseudo = Strongs.next();
            nextpseudo.setMySQLiteData("Transferred from psp_base_bundles");
            sqliteinserter.insert_into_table("psp", counter, nextpseudo.myInteger.longValue(), nextpseudo.mySQLiteData.source, nextpseudo.myBasis.toString(), bound);
        }
        try {
            conny.commit();
            conny.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
