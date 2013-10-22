package page24.q2323;

import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    in.nextLine();
    HashSet<String> ss = new HashSet<String>();
    Collections.addAll(ss, in.nextLine().split(" "));
    System.out.println(ss.size());
  }
}
