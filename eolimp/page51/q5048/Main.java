package page51.q5048;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), c3 = 0, c4 = 0;

    for(int i=0; i<n; i++) {
      int k = in.nextInt();
      if(k == 3) c3++;
      else if(k == 4) c4++;
    }

    if(c3 > 1 || (double)(c3 + c4) / n > 0.25)
      System.out.println("Ordinary degree");
    else
      System.out.println("Degree with honors");
  }
}
