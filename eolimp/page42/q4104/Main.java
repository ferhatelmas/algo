package page42.q4104;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashSet<Integer> s = new HashSet<Integer>();
    int n = in.nextInt();

    while(n-- > 0)
      s.add(in.nextInt());
    System.out.println(s.size());
  }
}
