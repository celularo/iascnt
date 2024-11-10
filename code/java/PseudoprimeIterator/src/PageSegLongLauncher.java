import java.math.BigInteger;
import java.util.Iterator;

public class PageSegLongLauncher {
    public static void launchPSegItRestart(Long bound, BigInteger PSPType, Long bound_old) {
        Boolean restart = true;
        Iterator<Long> gen = new PSegItEratoRestart(restart, bound_old);
        Iterator<Long> oddcompo = new IteratorLongOddCompo(gen);
        Iterator<Long> pspsieve = new PSPGroupSieveBaseTwoToEleven(oddcompo);
        IteratorOutputService output = new IteratorOutputService(pspsieve, bound, PSPType, "2-11");
        output.Write2SQLiteBundleUpTo();
    }
}
