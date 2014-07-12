package page6.q572;

import java.util.Comparator;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), i, j = 2;
    TreeMap<Integer, Integer> m = new TreeMap<Integer, Integer>(new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2) {
        return o2-o1;
      }
    });
    while(n > 1) {
      i = 0;
      while(n%j == 0) {
        i++;
        n /= j;
      }
      if(i > 0) m.put(j, i);
      j++;
    }

    StringBuilder sb = new StringBuilder();
    for(int k : m.descendingKeySet()) {
      sb.append("*").append(k);
      if(m.get(k) > 1) sb.append("^").append(m.get(k));
    }
    System.out.println(sb.substring(1));
  }
}
