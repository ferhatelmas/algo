package page74.q7340;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    HashSet<Character> s = new HashSet<Character>();
    for(char c : new Scanner(System.in).next().toCharArray())
      s.add(c);
    System.out.println(s.size());
  }
}
