package page70.q6958;

import java.util.Scanner;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Pattern p = Pattern.compile("da+dd?(i|y)");

    while(in.hasNextLine()) {
      System.out.println(p.matcher(in.nextLine()).matches() ? "She called me!!!" : "Cooing");
    }
  }
}
