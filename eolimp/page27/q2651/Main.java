package page27.q2651;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt(), l = n/2;

    int ks[] = new int[k], buf[] = new int[k];
    Arrays.fill(ks, 0);
    for(int i=0; i<n; i++) {
      int min = 1000, max = 0;
      for(int j=0; j<k; j++) {
        buf[j] = in.nextInt();
        min = Math.min(min, buf[j]);
        max = Math.max(max, buf[j]);
      }

      for(int j=0; j<k; j++) {
        if(buf[j] == max) ks[j] = -1;
        else if(buf[j] == min) if(ks[j] >= 0) ks[j]++;
      }
    }

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<k; i++) if(ks[i] > l) sb.append(' ').append(i+1);
    String s = sb.toString();
    System.out.println(s.isEmpty() ? 0 : s.substring(1));

  }
}
