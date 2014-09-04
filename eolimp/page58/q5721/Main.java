package page58.q5721;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt();
    PriorityQueue<Integer> pq = new PriorityQueue<Integer>(n, new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2) {
        return o2 - o1;
      }
    });
    if(k > n) System.out.println(-1);
    else {
      while(n-- > 0) pq.add(in.nextInt());

      while(k-- > 1) pq.poll();
      System.out.println(pq.poll());
    }
  }
}
