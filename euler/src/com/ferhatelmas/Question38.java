package com.ferhatelmas;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/4/12
 * Time: 9:19 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question38 {

    static Pattern pattern1 = Pattern.compile(".*(\\d).*\\1.*");
    static Pattern pattern2 = Pattern.compile(".*0.*");

    public static void main(String[] args) {

        for(int i=9999; i>0; i--) {

            if(isPanDigital(getMux(i))) {
                System.out.println(i);
                break;
            }

        }

    }
    
    private static String getMux(int num) {
        
        StringBuilder sb = new StringBuilder();
        int i= 1;
        
        while(sb.length() < 9) {
            sb.append(num * i);
            i++;
        }
        
        return sb.toString();
    }

    private static boolean isPanDigital(String s) {

        if(s.length() != 9) return false;
        Matcher matcher1 = pattern1.matcher(s);
        Matcher matcher2 = pattern2.matcher(s);

        return !(matcher1.matches() || matcher2.matches());
    }

}
