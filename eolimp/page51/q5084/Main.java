package page51.q5084;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    StringBuilder sb = new StringBuilder();
    int n = in.nextInt();

    for(int i=n; i>1; i--) {
      sb.append(' ').append(in.next());
    }
    sb.insert(0, in.next());
    System.out.println(sb.toString());
  }
}
