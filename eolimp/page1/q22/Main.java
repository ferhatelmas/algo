package page1.q22;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in=new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(), cnt = 0;

    boolean p[] = new boolean[10001];
    Arrays.fill(p, true); p[1] = false;
    for(int i=2; i<p.length; i++)
      if(p[i])
        for(int j=2*i; j<p.length; j+=i)
          p[j] = false;

    for(int i=Math.min(a, b), k=Math.max(a, b); i<=k; i++)
      if(p[i] && p[reverse(i)]) cnt++;

    System.out.println(cnt);
  }

  private static int reverse(int n) {
    int r = 0;
    while(n > 0) {
      r = 10 * r + n % 10;
      n /= 10;
    }
    return r;
  }
}
