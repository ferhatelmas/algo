package com.ferhatelmas.eolimp.page2.q48;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {

  public static void main(String[] args) throws Exception{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());

    int[][] area = new int[220][220];

    int minx=220;
    int maxx=0;
    int miny=220;
    int maxy=0;
    int y, x;
    String[] s;
    for(int i=0; i<n; i++) {

      s = br.readLine().split(" ");

      y = Integer.parseInt(s[0]) + 110;
      x = Integer.parseInt(s[1]) + 110;

      area[x][y] = 1;

      if(y<minx) minx = y;
      if(x<miny) miny = x;
      if(y>maxx) maxx = y;
      if(x>maxy) maxy = x;

    }

    int perimeter = 0;
    int add = 0;
    for(int i=miny; i<=maxy; i++) {

      for(int j=minx; j<=maxx; j++) {

        if(area[i][j] == 0) add++;
        else {
          if(area[i+1][j] == 0) perimeter++;
          if(area[i-1][j] == 0) perimeter++;
          if(area[i][j+1] == 0) perimeter++;
          if(area[i][j-1] == 0) perimeter++;
        }

      }

    }

    int w = maxx-minx+1;
    int h = maxy-miny+1;
    int nh = 2*(w+h);

    while(nh<perimeter) {

      nh += 2;
      if(w>h) {
        add += w;
        h++;
      }
      else {
        add += h;
        w++;
      }

    }

    System.out.println(add);

  }
}