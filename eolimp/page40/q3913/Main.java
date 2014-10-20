package page40.q3913;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    String ls[] = in.nextLine().split("\\s"),
           s[] = in.nextLine().split("\\s");

    StringBuilder sb = new StringBuilder();
    for(String i : ls)
      sb.append(' ').append(s[Integer.parseInt(i)]);
    System.out.println(sb.substring(1));
  }
}
