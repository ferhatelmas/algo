package page54.q5337;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    HashSet<String> s = new HashSet<String>();
    while(n-- > 0)
      s.add(in.next());
    System.out.println(s.size());
  }
}
