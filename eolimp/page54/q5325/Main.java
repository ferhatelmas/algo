package page54.q5325;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    StringBuilder sb = new StringBuilder();
    for(int i=1; i<=n; i++)
      sb.append(' ').append(i);
    System.out.println(sb.length() == 0 ? "" : sb.substring(1));
  }
}
