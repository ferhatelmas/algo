package page7.q606;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), sum = 0;
    for(int i=n; i<9999; i++)
      sum += getChange(i);
    System.out.println(sum);
  }

  private static int getChange(int n) {
    char[] c1 = String.valueOf(n).toCharArray(),
           c2 = String.valueOf(n+1).toCharArray();

    int cnt = 0;
    for(int i=0; i<c1.length; i++)
      cnt += (c1[i] != c2[i] ? 1 : 0);
    return cnt;
  }
}
