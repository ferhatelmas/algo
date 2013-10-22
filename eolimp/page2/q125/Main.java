package page2.q125;

import java.util.Scanner;

public class Main {


  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);

    int h1=in.nextInt();
    int m1=in.nextInt();
    int s1=in.nextInt();

    int h2=in.nextInt();
    int m2=in.nextInt();
    int s2=in.nextInt();

    h2-=h1;
    m2-=m1;
    s2-=s1;

    if(s2<0) {
      s2+=60;
      m2--;
    }

    if(m2<0) {
      m2+=60;
      h2--;
    }

    System.out.println(h2 + " " + m2 + " " + s2);
  }

}