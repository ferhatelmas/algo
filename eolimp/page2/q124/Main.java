package page2.q124;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt = 1;
    boolean[] sieve = new boolean[n+1];

    Arrays.fill(sieve, true);
    for(int i=2; i<sieve.length; i++)
      if(sieve[i]) {
        int z = n, c = 0;
        while(z > 0) {
          z /= i;
          c += z;
        }
        cnt *= (c+1);
        for(int j=i; j<sieve.length; j+=i)
          sieve[j] = false;
      }
    System.out.println(cnt);
  }
}
