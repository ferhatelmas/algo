package page40.q3935;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), t = n;
    StringBuilder sb = new StringBuilder();
    while(t-- > 0)
      sb.insert(0, in.next()).insert(0, ' ');
    System.out.println(n > 0 ? sb.substring(1) : "");
  }
}
