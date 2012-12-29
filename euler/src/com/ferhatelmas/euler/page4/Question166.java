package com.ferhatelmas.euler.page4;

public class Question166 {

  public static void main(String[] args) {
    int cnt = 0;
    for(int a0=0; a0<10; a0++)
      for(int a1=0; a1<10; a1++)
        for(int a2=0; a2<10; a2++)
          for(int a3=0; a3<10; a3++)
            for(int a4=0; a4<10; a4++)
              for(int a5=0; a5<10; a5++)
                for(int a6=0; a6<10; a6++)
                  for(int a8=0; a8<10; a8++)
                    for(int a10=0; a10<10; a10++) {
                      int r = a0 + a1 + a2 + a3;
                      int a7 = r - a4 - a5 - a6;
                      if(a7 >= 0 && a7 < 10) {
                        int a12 = r - a0 - a4 - a8;
                        if(a12 >= 0 && a12 <10) {
                          int a9 = r - a3 - a6 - a12;
                          if(a9 >= 0 && a9 < 10) {
                            int a11 = r - a8 - a9 - a10;
                            if(a11 >= 0 && a11 < 10) {
                              int a13 = r - a1 - a5 - a9;
                              if(a13 >= 0 && a13 < 10) {
                                int a14 = r - a2 - a6 - a10;
                                if(a14 >= 0 && a14 < 10) {
                                  int a15 = r - a3 - a7 - a11;
                                  if(a15 >= 0 && a15 < 10) {
                                    if(r == a12 + a13 + a14 + a15 &&
                                        r == a0 + a5 + a10 + a15) cnt++;
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }

    System.out.println(cnt);
  }
}