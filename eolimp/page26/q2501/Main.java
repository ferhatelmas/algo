package page26.q2501;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), r = in.nextInt(), sum = 0;
    int[] buf = new int[n];
    for(int i=0; i<n; i++) {
      buf[i] = in.nextInt();
      sum += buf[i];
    }
    double area = Math.PI * r * r;
    for(int i : buf)
      System.out.format(Locale.US, "%.9f\n", (area/sum)*i);
  }
}
