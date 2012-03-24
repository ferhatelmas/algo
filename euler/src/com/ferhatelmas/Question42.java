package com.ferhatelmas;

import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/4/12
 * Time: 10:21 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question42 {

    private static List<Integer> list = new ArrayList<Integer>();

    public static void main(String[] args) throws Exception{

        for(int i=0; i<21; i++) {

            list.add((int)(0.5 * i * (i + 1)));

        }
        
        Scanner sc = new Scanner(new FileInputStream("words.txt")).useDelimiter(",");
        
        int cnt = 0;
        while(sc.hasNext()) {
            
            String s = sc.next();
            int val = getVal(s);
            
            if(list.contains(val)) cnt++;
            
        }

        System.out.println(cnt);

    }
    
    
    private static int getVal(String s) {
        
        s = s.substring(1, s.length()-1);

        int sum = 0;
        
        for(int i=0; i<s.length(); i++) {
            
            sum += (s.charAt(i)-'A'+1);
            
        }

        return sum;
        
    }
    
    
}
