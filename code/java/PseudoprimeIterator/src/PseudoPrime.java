import java.math.BigInteger;

public class PseudoPrime {
    public BigInteger myInteger;
    public BigInteger myBasis;
    public BigInteger myPredecessor;
    private BigInteger myPseudoPrimeCondition;
    public Boolean myPseudoPrimeProperty;
    private BigInteger myPredecessorFactorOdd;
    private BigInteger myPredecessorPowerOfFactorTwo;
    public BigInteger myPFOModPow;
    public BigInteger myPPO2PowerForSPSP;
    public Boolean myStrongPseudoPrimeProperty;
    public SPSPDataOnSQLite mySQLiteData;

    public PseudoPrime(Long number, Long basis) {
        this.myInteger = BigInteger.valueOf(number);
        this.myPredecessor = this.myInteger.subtract(BigInteger.ONE);
        this.myBasis = BigInteger.valueOf(basis);
        this.mySQLiteData = new SPSPDataOnSQLite();
    }

    public void setMyPseudoPrimeProperty() {
        this.myPseudoPrimeCondition = this.myBasis.modPow(myPredecessor, myInteger);
        this.myPseudoPrimeProperty = false;
        if (this.myPseudoPrimeCondition.compareTo(BigInteger.ONE) == 0) {
            this.myPseudoPrimeProperty = true;
        }
    }

    public Boolean getMyPseudoPrimeProperty() {
        if (myPseudoPrimeProperty == null)
            setMyPseudoPrimeProperty();
        return myPseudoPrimeProperty;
    }

    public void setMyPredecessorFactorOdd() {
        myPredecessorFactorOdd = myPredecessor;
        myPredecessorPowerOfFactorTwo = BigInteger.valueOf(0);
        while (BigInteger.ZERO == myPredecessorFactorOdd.mod(BigInteger.TWO)) {
            myPredecessorFactorOdd = myPredecessorFactorOdd.divide(BigInteger.TWO);
            myPredecessorPowerOfFactorTwo = myPredecessorPowerOfFactorTwo.add(BigInteger.valueOf(1));
        }
    }

    public BigInteger getMyPredecessorFactorOdd() {
        if (myPredecessorFactorOdd == null)
            setMyPredecessorFactorOdd();
        return myPredecessorFactorOdd;
    }

    public void setMyPFOModPow() {
        myPFOModPow = myBasis.modPow(myPredecessorFactorOdd, myInteger);
    }

    public BigInteger getMyPFOModPow() {
        if (myPFOModPow == null)
            setMyPFOModPow();
        return myPFOModPow;
    }

    public void setMyPPO2PowerForSPSP() {
        myPPO2PowerForSPSP = myPredecessorPowerOfFactorTwo.subtract(BigInteger.ONE);
        while (myPPO2PowerForSPSP.compareTo(BigInteger.ZERO) >= 0) {
            BigInteger testexpo = BigInteger.TWO.pow(myPPO2PowerForSPSP.intValue());
            BigInteger testpower = myPredecessorFactorOdd.multiply(testexpo);
            BigInteger modpow = myBasis.modPow(testpower, myInteger).add(BigInteger.ONE).mod(myInteger);

            if (modpow == BigInteger.ZERO) {
                return;
            }
            myPPO2PowerForSPSP = myPPO2PowerForSPSP.subtract(BigInteger.ONE);
        }
    }

    public BigInteger getMyPPO2PowerForSPSP() {
        if (myPPO2PowerForSPSP == null)
            setMyPPO2PowerForSPSP();
        return myPPO2PowerForSPSP;
    }

    public void setMyStrongPseudoPrimeProperty(Boolean myStrongPseudoPrimeProperty) {
        this.myStrongPseudoPrimeProperty = myStrongPseudoPrimeProperty;
    }

    public void setMySQLiteData(String source) {

        this.mySQLiteData.val = this.myInteger.longValue();
        this.mySQLiteData.base = this.myBasis.longValue();
        this.mySQLiteData.source = source;
        if (myPredecessorFactorOdd != null) {
            this.mySQLiteData.core = this.myPredecessorFactorOdd.longValue();
        }
        if (myPredecessorPowerOfFactorTwo != null) {
            this.mySQLiteData.absDepth = this.myPredecessorPowerOfFactorTwo.longValue();
        }
        if (myPFOModPow != null) {
            this.mySQLiteData.coreModPow = this.myPFOModPow.longValue();
        }
        if (myPPO2PowerForSPSP != null) {
            this.mySQLiteData.succDepth = this.myPPO2PowerForSPSP.longValue();
        }
    }

    public String toString() {
        return this.myInteger + "\n" +
                "Basis: " + this.myBasis + "\n" +
                "Predecessor: " + this.myPredecessor + "\n" +
                "PseudoPrimeCondition: " + this.myPseudoPrimeCondition + "\n" +
                "PseudoPrimeProperty: " + this.myPseudoPrimeProperty + "\n" +
                "PredecessorFactorOdd: " + this.myPredecessorFactorOdd + "\n" +
                "PredecessorPowerOfFactorTwo: " + this.myPredecessorPowerOfFactorTwo + "\n" +
                "PFOModPow: " + this.myPFOModPow + "\n" +
                "PPO2PowerForSPSP: " + this.myPPO2PowerForSPSP + "\n" +
                "trongPseudoPrimeProperty: " + this.myStrongPseudoPrimeProperty + "\n";
    }
}
