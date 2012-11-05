package com.ferhatelmas.eolimp.page3.q85;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);

    int n=in.nextInt();
    int x=in.nextInt()-1;
    int y=in.nextInt()-1;
    int cnt=0;
    int i,j;
    boolean[][] buf=new boolean[n][n];
    int path=0;
    boolean flag=false;
    for(i=0; i<n; i++) for(j=0; j<n; j++) buf[i][j]=false;

    i=0; j=0;
    while(!(i==x&&j==y)) {

      if(!flag){
        buf[i][j]=true;
        if(++cnt==n*n) break;
      }

      if(path==0) {

        if(j+1<n && !buf[i][j+1]) {
          j++;
          flag=false;
        }
        else {
          path=1;
          flag=true;
        }

      } else if(path==1){

        if(i+1<n && !buf[i+1][j]) {
          i++;
          flag=false;
        }
        else {
          path=2;
          flag=true;
        }

      } else if(path==2){

        if(j-1>-1 && !buf[i][j-1]) {
          j--;
          flag=false;
        }
        else {
          path=3;
          flag=true;
        }

      } else {

        if(i-1>-1 && !buf[i-1][j]) {
          i--;
          flag=false;
        }
        else {
          path=0;
          flag=true;
        }
      }

    }

    System.out.println(cnt+1);

  }

}