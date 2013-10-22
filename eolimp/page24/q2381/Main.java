package page24.q2381;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n;
    while((n=in.nextInt()) != -1) {
      HashSet<Integer> set = new HashSet<Integer>();
      while(n != 0) {
        set.add(n);
        n = in.nextInt();
      }
      System.out.println(count(set));
    }
  }

  private static int count(HashSet<Integer> s) {
    int cnt = 0;
    for(int n : s) if(n%2 == 0 && s.contains(n/2)) cnt++;
    return cnt;
  }
}
