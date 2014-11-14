package page40.q3966;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    HashSet<Integer> s = new HashSet<Integer>();
    for(int i=0; i<n; i++)
      s.add(in.nextInt());

    int t = in.nextInt();
    while(t-- > 0) {
      System.out.println(s.contains(in.nextInt()) ? "YES" : "NO");
    }
  }
}
