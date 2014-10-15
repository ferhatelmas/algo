package page41.q4040;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashSet<Integer> s = new HashSet<Integer>();

    for(int i=in.nextInt(); i>0; i--) {
      s.add(in.nextInt());
    }
    System.out.println(s.size());
  }
}
