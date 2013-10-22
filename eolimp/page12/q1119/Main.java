package page12.q1119;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.next().trim();
    int n = in.nextInt();

    StringBuilder sb = new StringBuilder();
    for(int i=n; i>0; i--) {
      for(int j=i-1; j>0; j--)
        sb.append(" ");
      for(int j=2*(n-i)+1; j>0; j--)
        sb.append(s);
      sb.append("\n");
    }
    System.out.println(sb.length()-n);
    System.out.print(sb.toString());
  }
}
