import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class StrongTestLauncher {
    public static void launchStrongTester(Long bas, Long bound) {
        Connection conny = SQLiteConnect.connect();
        SQLiteQueryApp sqlitequery = new SQLiteQueryApp(conny);
        List<PSPDataOnSQLite> list = null;
        try {
            list = sqlitequery.getListForBaseAndBound(bas, bound);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        int count = list.size();
        Iterator<PSPDataOnSQLite> iterator = list.iterator();
        System.out.println("Hits: " + count);
        int counter = 0;
        List<PseudoPrime> strongs = new ArrayList<>();
        while (iterator.hasNext() == true) {
            counter++;
            PSPDataOnSQLite nextPSP = iterator.next();
            PseudoPrime testpseu = new PseudoPrime(nextPSP.val, nextPSP.base);
            StrongPseudoPrimeTester.test_pseudo_for_strong_psp(testpseu);
            if (testpseu.myStrongPseudoPrimeProperty == true) {
                strongs.add(testpseu);
            }
        }
        System.out.println("Testresults: " + strongs.size());
        StrongOutputService outp = new StrongOutputService(strongs.iterator());
        outp.Write2SQLiteStrongs();
    }

    public static void launchTypeTester(String bundle, Long bas, Long bound) {
        Connection conny = SQLiteConnect.connect();
        SQLiteQueryApp sqlitequery = new SQLiteQueryApp(conny);
        List<PSPDataOnSQLite> list = null;
        try {
            list = sqlitequery.getListForBundleAndBound(bundle, bound);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        int count = list.size();
        Iterator<PSPDataOnSQLite> iterator = list.iterator();
        System.out.println("Hits: " + count);
        int counter = 0;
        List<PseudoPrime> pseudos = new ArrayList<>();
        while (iterator.hasNext() == true) {
            counter++;
            PSPDataOnSQLite nextPSP = iterator.next();
            PseudoPrime testpseu = new PseudoPrime(nextPSP.val, bas);
            if (testpseu.getMyPseudoPrimeProperty()) {
                pseudos.add(testpseu);
            }
        }
        System.out.println("Testresults: " + pseudos.size());
        StrongOutputService outp = new StrongOutputService(pseudos.iterator());
        outp.Write2SQLiteTypes(bound);
    }
}
