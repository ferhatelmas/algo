package page9.q830;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int m = in.nextInt(), n =in.nextInt();
    boolean s[] = new boolean[n+1], f = false;
    Arrays.fill(s, true);
    for(int i=2; i<s.length; i++) {
      if(s[i]) {
        if(i >= m) {
          System.out.println(i);
          f = true;
        }
        for (int j = 2 * i; j < s.length; j += i)
          s[j] = false;
      }
    }
    if(!f) System.out.println("Absent");
  }
}
