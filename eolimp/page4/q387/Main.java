package page4.q387;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int w = in.nextInt(), h = in.nextInt(), r = in.nextInt(), n = in.nextInt(),
        xmin = Integer.MAX_VALUE, xmax = Integer.MIN_VALUE, ymin = xmin, ymax = xmax;

    for(int i=0; i<n; i++) {
      int x = in.nextInt(), y = in.nextInt();
      xmin = Math.min(x-r, xmin);
      xmax = Math.max(x+r, xmax);
      ymin = Math.min(y-r, ymin);
      ymax = Math.max(y+r, ymax);
    }

    System.out.println(w*h - (xmax-xmin)*(ymax-ymin));
  }
}
