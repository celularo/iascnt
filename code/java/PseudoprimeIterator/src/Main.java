import java.math.BigInteger;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        if (args.length > 1) {
            Long bnd = Long.valueOf(args[1].replaceAll("_", ""));
            Long old = Long.valueOf(args[2].replaceAll("_", ""));
            switch (args[0]) {
                case "bundle":
                    System.out.println("Argument bundle");
                    PageSegLongLauncher.launchPSegItRestart(bnd, BigInteger.valueOf(1), old);
                    break;
                case "types":
                    System.out.println("Argument types");
                    String bundle = "2-11";
                    for (Long bas : Arrays.asList(2L, 3L, 5L, 7L, 11L)) {
                        StrongTestLauncher.launchTypeTester(bundle, bas, bnd);
                    }
                    break;
                case "spsp":
                    System.out.println("Argument spsp");
                    for (Long bas : Arrays.asList(2L, 3L, 5L, 7L, 11L)) {
                        StrongTestLauncher.launchStrongTester(bas, bnd);
                    }
                    break;
                default:
                    System.out.println("Argument missing");
                    break;
            }
        } else {
            System.out.println("Argument missing");
        }
    }
}
