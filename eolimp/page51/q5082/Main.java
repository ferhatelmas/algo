package page51.q5082;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    StringBuilder sb = new StringBuilder();
    int n = in.nextInt(), c;
    in.nextLine();

    for(int i=0; i<n; i++) {
      String s = in.nextLine();
      c = 0;
      for(int j=2*(n-1); j>-1; j--) {
        if(s.charAt(j) == '1') c++;
      }
      sb.append(' ').append(c);
    }

    System.out.println(sb.substring(1));
  }
}
