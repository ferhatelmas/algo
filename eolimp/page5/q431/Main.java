package page5.q431;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int w, h;
    while((w=in.nextInt()) != 0 && ((h=in.nextInt()) != 0)) {
      in.nextLine();
      char buf[][] = new char[h][w];
      for(int i=0; i<h; i++) {
        String s = in.nextLine();
        for(int j=0; j<w; j++)
          buf[i][j] = s.charAt(j);
      }
      System.out.println(solve(buf, h, w));
    }
  }

  private static int solve(char[][] buf, int h, int w) {
    int cnt = 0, curr = 1;

    while(curr > cnt) {
      cnt = curr;
      for(int i=0; i<h; i++) {
        for(int j=0; j<w; j++) {
          if(buf[i][j] == '.' && ((i<h-1 && buf[i+1][j] == '@') ||
                                  (i>0 && buf[i-1][j] == '@') ||
                                  (j<w-1 && buf[i][j+1] == '@') ||
                                  (j>0 && buf[i][j-1] == '@'))) {
            buf[i][j] = '@';
            curr++;
          }
        }
      }
    }
    return cnt;
  }
}
