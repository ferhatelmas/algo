import java.math.BigInteger;
import java.util.BitSet;
import java.util.Scanner;

public class Solution {

    private static int[] primes;

    private static final BigInteger mode = new BigInteger("1000007");
    private static int N;

    public static void main(String[] args) throws Exception {

        generatePrimeList(999983);
        N = new Scanner(System.in).nextInt();

        if(N == 1) {
            System.out.println(1);
        } else {
            BigInteger result = new BigInteger("1");
            for(int i=0; i<primes.length; i++) {
                if(primes[i] > N ) break;
                int cnt = getCountOfPrime(primes[i]);
                result = result.multiply(new BigInteger(String.valueOf(cnt * 2 + 1)));
                result = result.mod(mode);
            }
            System.out.println(result);
        }
    }

    private static int getCountOfPrime(int prime) {

        int n = N, cnt = 0;
        while(n >= prime) {
            n /= prime;
            cnt += n;
        }

        return cnt;
    }


    static private void generatePrimeList(int max) {
        BitSet isNotPrime = new BitSet(max+1);
        int numPrimes = 1;
        for (int i = 2; i <= max; i++) {
            if (!isNotPrime.get(i)) {
                numPrimes++;
                for (int j = i + i; j <= max; j += i) {
                    isNotPrime.set(j);
                }
            }
        }
        primes = new int[numPrimes];
        int j = 0;
        for (int i = 2; i <= max; i++) {
            if (!isNotPrime.get(i)) {
                primes[j] = i;
                j++;
            }
        }
    }

}

