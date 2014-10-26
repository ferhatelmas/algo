package page28.q2797;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashSet<String> s = new HashSet<String>();
    int n = in.nextInt();

    while(n-- > 0) s.add(in.next());
    System.out.println(s.size());
  }
}
