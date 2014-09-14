package page20.q1957;

import java.util.Scanner;
import java.util.TreeSet;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    TreeSet<Integer> t = new TreeSet<Integer>();
    int n = in.nextInt();

    while(n-- > 0) t.add(in.nextInt());
    t.pollLast();
    System.out.println(t.pollLast());
  }
}
