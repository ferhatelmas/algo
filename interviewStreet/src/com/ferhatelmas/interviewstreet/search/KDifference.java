package com.ferhatelmas.interviewstreet.search;

import java.util.Arrays;
import java.util.Scanner;

public class KDifference {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int K = in.nextInt();

        int [] data = new int[N];

        for(int i=0; i<N; i++) data[i] = in.nextInt();

        Arrays.sort(data);

        int i, j, diff, cnt = 0;
        for(i=0; i<N-1; i++) {

            for(j=i+1; j<N; j++) {

                diff = data[j] - data[i];
                if(diff == K) {
                    cnt++;
                    break;
                } else if(diff > K){
                    break;
                }

            }

        }

        System.out.println(cnt);

    }

}

