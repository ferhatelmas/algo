package page17.q1670;

import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt(),
        dist[][] = new int[n][n], inf = -1;
    for(int r[] : dist) Arrays.fill(r, inf);

    while(k-- > 0) {
      dist[in.nextInt()-1][in.nextInt()-1] = in.nextInt();
    }

    for(int l=0; l<n; l++) {
      for(int i=0; i<n; i++) {
        if(dist[i][l] == inf) continue;
        for(int j=0; j<n; j++) {
          if(dist[l][j] != inf &&
             (dist[i][j] == inf || dist[i][j] > dist[i][l] + dist[l][j])) {
            dist[i][j] = dist[i][l] + dist[l][j];
          }
        }
      }
    }

    double sum = 0; int c = 0;
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        if(i != j && dist[i][j] != inf) {
          sum += dist[i][j];
          c++;
        }
      }
    }
    System.out.printf(Locale.US, "%.6f\n", sum / c);
  }
}
