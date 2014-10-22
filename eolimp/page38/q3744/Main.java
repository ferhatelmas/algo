package page38.q3744;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int f[] = {1, 2, 6, 24, 120};

    String s;
    while(!"0".equals(s = in.next())) {
      int sum = 0;
      for(int i=0, l=s.length(); i<l; i++)
        sum += (s.charAt(l-1-i) - '0') * f[i];
      System.out.println(sum);
    }
  }
}
