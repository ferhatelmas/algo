package page5.q468;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n, p = 0, max = Integer.MAX_VALUE, min = Integer.MIN_VALUE, i = 0;
    while(in.hasNextInt()) {
      n = in.nextInt();
      if(i > 0 && (n > max || n < min)) {
        System.out.println("NO");
        return;
      } else if(i > 0) {
        if(n > p) min = Math.max(min, p);
        else max = Math.min(max, p);
      }
      i++;
      p = n;
    }
    System.out.println("YES");
  }
}
