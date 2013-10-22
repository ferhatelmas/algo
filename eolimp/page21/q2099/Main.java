package page21.q2099;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] ns = new int[n];
    for(int i=0; i<n; i++) ns[i] = in.nextInt();
    HashSet<Integer> s = new HashSet<Integer>();
    int m = in.nextInt();
    for(int i=0; i<m; i++) s.add(in.nextInt());
    ArrayList<Integer> ls = new ArrayList<Integer>(n);
    for(int i : ns) if(!s.contains(i)) ls.add(i);
    System.out.println(ls.size());
    StringBuilder sb = new StringBuilder();
    for(int i : ls) sb.append(" ").append(i);
    System.out.println(sb.substring(Math.min(sb.length(), 1)));
  }
}
