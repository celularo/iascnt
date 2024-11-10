public class StrongPseudoPrimeTester {
    public static void test_pseudo_for_strong_psp(PseudoPrime pseudo) {
        pseudo.getMyPredecessorFactorOdd();
        pseudo.getMyPFOModPow();
        pseudo.getMyPPO2PowerForSPSP();
        pseudo.setMyStrongPseudoPrimeProperty(false);
        if (pseudo.myPFOModPow.intValue() == 1 || pseudo.myPPO2PowerForSPSP.intValue() != -1)
            pseudo.setMyStrongPseudoPrimeProperty(true);
    }
}
