package page8.q749;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String ss[] = in.nextLine().split(":"), p[] = in.nextLine().split(":");
    long sum = 0;

    for(int i=0; i<3; i++) sum += Math.pow(60, 2-i) * Integer.parseInt(ss[i]);
    for(int i=0; i<p.length; i++) sum += Math.pow(60, p.length-1-i) * Integer.parseInt(p[i]);

    long s, m, h, d;
    d = sum / (3600 * 24);
    sum -= d * 3600 * 24;
    h = sum / 3600;
    sum -= h * 3600;
    m = sum / 60;
    sum -= m * 60;
    s = sum;

    System.out.printf("%02d:%02d:%02d", h, m, s);
    if(d > 0)
      System.out.println("+" + d + " days");
    else
      System.out.println();
  }
}
