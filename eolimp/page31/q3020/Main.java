package page31.q3020;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s;
    while(!(s = in.nextLine()).equals("#")) {
      System.out.println(s.replaceAll("%", "%25")
                          .replaceAll(" ", "%20")
                          .replaceAll("!", "%21")
                          .replaceAll("\\$", "%24")
                          .replaceAll("\\(", "%28")
                          .replaceAll("\\)", "%29")
                          .replaceAll("\\*", "%2a"));
    }
  }
}
