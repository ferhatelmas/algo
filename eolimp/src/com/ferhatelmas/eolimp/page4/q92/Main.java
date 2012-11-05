package com.ferhatelmas.eolimp.page4.q92;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws Exception {

    Scanner in= new Scanner(System.in);

    ArrayList<Integer> buf=new ArrayList<Integer>();
    ArrayList<Integer> res=new ArrayList<Integer>();

    int t=in.nextInt();

    int i,j,k;
    int time, size, tmp, val, sum;
    for(i=0; i<t; i++) {
      time=in.nextInt();
      size=in.nextInt();
      buf.clear();
      for(j=0; j<size; j++) {
        tmp=in.nextInt();
        for(k=0; k<buf.size(); k++) {
          val=buf.get(k);
          if(tmp>val) break;
        }
        if(k==buf.size()) buf.add(tmp);
        else buf.add(k, tmp);
      }

      sum=0;
      for(j=0; j<Math.min(time, size); j++)
        sum+=buf.get(j);

      res.add(sum);
    }

    for(int ss : res) System.out.println(ss);
  }

}