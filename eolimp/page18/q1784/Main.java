package page18.q1784;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt();
    System.out.println(perm(new int[n], k, 0, new HashSet<Integer>()));
  }

  private static int perm(int p[], int d, int k, HashSet<Integer> s) {
    if(k == p.length) return 1;

    int sum = 0;
    for(int i=1; i<=p.length; i++) {
      if(!s.contains(i) && (k == 0 || Math.abs(p[k-1] - i) <= d)) {
        p[k] = i;
        s.add(i);
        sum += perm(p, d, k+1, s);
        s.remove(i);
      }
    }
    return sum;
  }
}
