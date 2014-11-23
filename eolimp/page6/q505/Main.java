package page6.q505;

import java.util.Comparator;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int m, n;

    while((m = in.nextInt()) != 0 && (n = in.nextInt()) != 0) {
      char c[][] = new char[m][n];
      in.nextLine();
      for(int i=0; i<m; i++) {
        String s = in.nextLine();
        for(int j=0; j<n; j++)
          c[i][j] = s.charAt(j);
      }

      TreeMap<Integer, Integer> results = solve(c);
      StringBuilder sb = new StringBuilder();
      for(int k : results.descendingKeySet())
        sb.append(' ').append(k).append('-').append(results.get(k));
      System.out.println(sb.length() == 0 ? "" : sb.substring(1));
    }
  }

  private static TreeMap<Integer, Integer> solve(char c[][]) {
    TreeMap<Integer, Integer> t = new TreeMap<Integer, Integer>(new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2) {
        return o2-o1;
      }
    });
    int cnt = 0;
    for(int i=0; i<c.length; i++) {
      cnt = 0;
      for(int j=0; j<c[0].length; j++) {
        if(c[i][j] == '.') cnt++;
        else {
          if(cnt > 1) t.put(cnt, 1 + (t.containsKey(cnt) ? t.get(cnt) : 0));
          cnt = 0;
        }
      }
      if(cnt > 1) t.put(cnt, 1 + (t.containsKey(cnt) ? t.get(cnt) : 0));
    }

    for(int i=0; i<c[0].length; i++) {
      cnt = 0;
      for(int j=0; j<c.length; j++) {
        if(c[j][i] == '.') cnt++;
        else {
          if(cnt > 1) t.put(cnt, 1 + (t.containsKey(cnt) ? t.get(cnt) : 0));
          cnt = 0;
        }
      }
      if(cnt > 1) t.put(cnt, 1 + (t.containsKey(cnt) ? t.get(cnt) : 0));
    }

    return t;
  }

  private static void traverse(char c[][], int m, int n, TreeMap<Integer, Integer> t) {

  }
}
