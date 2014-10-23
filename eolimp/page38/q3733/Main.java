package page38.q3733;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    long lcm = 1;
    double d = Math.log(n);

    boolean b[] = new boolean[31];
    Arrays.fill(b, true);
    for(int i=2; i<b.length; i++)
      if(b[i]) {
        lcm *= Math.pow(i, (int) (d / Math.log(i)));
        for(int j=2*i; j<b.length; j+=i)
          b[j] = false;
      }
    System.out.println(lcm);
  }
}
