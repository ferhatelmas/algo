package page5.q463;

import java.util.Comparator;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(), c = in.nextInt();
    TreeSet<Long> s = new TreeSet<Long>(new Comparator<Long>() {
      @Override
      public int compare(Long o1, Long o2) {
        return o2 - o1 > 0 ? 1 : (o2.equals(o1) ? 0 : -1);
      }
    });
    s.add(sum(a, b, c));
    s.add(sum(a, c, b));
    s.add(sum(b, c, a));
    System.out.println(s.size() == 1 ? "NO" : "YES");
    for(long i : s.descendingSet())
      System.out.println(i);
  }

  private static long sum(int a, int b, int c) {
    String as = String.valueOf(a), bs = String.valueOf(b), cs  = String.valueOf(c);
    int m = Math.max(as.length(), bs.length());
    String abs = doSum(fill(as, m), fill(bs, m));
    m = Math.max(abs.length(), cs.length());
    return Long.parseLong(doSum(fill(abs, m), fill(cs, m)));
  }

  private static String fill(String s, int l) {
    StringBuilder sb = new StringBuilder(l-s.length());
    for(int i=sb.capacity(); i>0; i--) sb.append('0');
    return sb.append(s).toString();
  }

  private static String doSum(String a, String b) {
    StringBuilder sb = new StringBuilder();
    for(int i=0, l=a.length(); i<l; i++)
      sb.append(a.charAt(i) - '0' + b.charAt(i) - '0');
    return sb.toString();
  }
}
