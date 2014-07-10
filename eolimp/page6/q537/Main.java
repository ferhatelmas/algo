package page6.q537;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t;

    while((t = in.nextInt()) != 0) {
      HashSet<Integer> set = new HashSet<Integer>();
      for(int i=1; i<50; i++) set.add(i);
      for(int i=0; i<t; i++) {
        for(int j=0; j<6; j++) {
          set.remove(in.nextInt());
        }
      }
      System.out.println(set.size() == 0 ? "Yes" : "No");
    }
  }
}
