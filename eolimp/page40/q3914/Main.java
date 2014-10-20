package page40.q3914;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int l = in.nextInt(), k = in.nextInt();
    int n = in.nextInt(), c = 0, j = 0;

    while(j < n) {
      int m = in.nextInt();
      if(c + m*k > l) break;
      else c += m*k;
      j++;
    }
    System.out.println(j);
  }
}
