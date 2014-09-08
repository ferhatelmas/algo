package page48.q4730;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt()+1;
    BigInteger ns[] = new BigInteger[n+1];
    ns[0] = BigInteger.ZERO; ns[1] = BigInteger.ONE;
    int i = 2;
    while(i <= n) {
      ns[i] = ns[i-1].add(ns[i-2]);
      i++;
    }
    System.out.println(ns[n].toString());
  }
}
