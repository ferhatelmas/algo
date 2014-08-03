package page58.q5798;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();

    int min = Integer.MAX_VALUE;
    for(int i=0; i<5; i++)
      for(int j=i+1; j<6; j++)
        for(int k=j+1; k<7; k++)
          for(int l=k+1; l<8; l++)
            min = Math.min(Integer.parseInt(new String(new char[]{
                s.charAt(i),
                s.charAt(j),
                s.charAt(k),
                s.charAt(l),
            })), min);
    System.out.println(min);
  }
}
